# IPL Data Analysis Program - Enhanced Version
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from datetime import datetime

# Try to import colorama for colors, if not available, use ANSI codes
try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    HAS_COLORAMA = True
except ImportError:
    # ANSI color codes for Windows
    class Fore:
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        RESET = '\033[0m'
    class Style:
        BRIGHT = '\033[1m'
        DIM = '\033[2m'
        RESET_ALL = '\033[0m'
    HAS_COLORAMA = False

csv_file = 'matchanalysis.csv'

# Color functions for easy use
def print_colored(text, color=Fore.WHITE, style=Style.RESET_ALL):
    """Print colored text"""
    print(f"{color}{style}{text}{Style.RESET_ALL}")

def print_header(text, width=80):
    """Print a formatted header"""
    border = "═" * width
    print_colored(border, Fore.CYAN, Style.BRIGHT)
    print_colored(f"{text:^{width}}", Fore.YELLOW, Style.BRIGHT)
    print_colored(border, Fore.CYAN, Style.BRIGHT)

def print_box(text, color=Fore.CYAN):
    """Print text in a box"""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines) if lines else 0
    border = "═" * (max_len + 4)
    print_colored(f"╔{border}╗", color)
    for line in lines:
        print_colored(f"║  {line:<{max_len}}  ║", color)
    print_colored(f"╚{border}╝", color)

def print_separator(char="─", length=80):
    """Print a separator line"""
    print_colored(char * length, Fore.CYAN)

def print_success(text):
    """Print success message"""
    print_colored(f"✓ {text}", Fore.GREEN, Style.BRIGHT)

def print_error(text):
    """Print error message"""
    print_colored(f"✗ {text}", Fore.RED, Style.BRIGHT)

def print_info(text):
    """Print info message"""
    print_colored(f"ℹ {text}", Fore.BLUE, Style.BRIGHT)

def print_warning(text):
    """Print warning message"""
    print_colored(f"⚠ {text}", Fore.YELLOW, Style.BRIGHT)

def introduction():
    """Display welcome introduction"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # ASCII Art Title
    title = """
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║     ██╗██╗██████╗      █████╗ ████████╗ █████╗ ███╗   ██╗      ║
    ║     ██║██║██╔══██╗    ██╔══██╗╚══██╔══╝██╔══██╗████╗  ██║      ║
    ║     ██║██║██████╔╝    ███████║   ██║   ███████║██╔██║ ██╔██╗     ║
    ║     ██║██║██╔═══╝     ██╔══██║   ██║   ██╔══██║██║╚██╗██║╚██╗    ║
    ║     ██║██║██║         ██║  ██║   ██║   ██║  ██║██║ ╚████║ ╚████╗ ║
    ║     ╚═╝╚═╝╚═╝         ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═══╝ ║
    ║                                                                  ║
    ║              📊 DATA ANALYSIS & VISUALIZATION SYSTEM 📊          ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
    """
    print_colored(title, Fore.CYAN, Style.BRIGHT)
    
    print_header("WELCOME TO IPL DATA ANALYSIS PROGRAM", 80)
    print()
    
    msg = f"""
    {Fore.YELLOW}🏏 Cricket is one of the most popular games in INDIA! 🏏{Style.RESET_ALL}
    
    {Fore.WHITE}The Indian Premier League (IPL) is a professional Twenty20 cricket league.
    It is the most-attended cricket league in the world!
    
    {Fore.CYAN}📈 In this project, we will analyze the dataset of IPL matches 
    played during 2008-2019 using Python Pandas and Matplotlib for 
    data visualization.{Style.RESET_ALL}
    
    {Fore.GREEN}✨ Features: ✨{Style.RESET_ALL}
    • Comprehensive data analysis
    • Interactive data visualization
    • Statistical insights
    • Beautiful graphs and charts
    """
    
    print(msg)
    print_separator("═", 80)
    input(f'\n{Fore.YELLOW}{Style.BRIGHT}Press Enter to continue...{Style.RESET_ALL}')

def made_by():
    """Display credits"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print_header("PROJECT CREDITS", 80)
    print()
    
    credits = f"""
    {Fore.CYAN}╔══════════════════════════════════════════════════════════════╗{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                              {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}  {Fore.YELLOW}📝 IPL Data Analysis made by:{Style.RESET_ALL}                              {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}     {Fore.GREEN}Ishan Bansal{Style.RESET_ALL}                              {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                              {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}  {Fore.YELLOW}🏫 School Name:{Style.RESET_ALL} {Fore.WHITE}St. Anselm's Pink City School{Style.RESET_ALL}              {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                              {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}  {Fore.YELLOW}📅 Session:{Style.RESET_ALL} {Fore.WHITE}2021-22{Style.RESET_ALL}                                        {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}║{Style.RESET_ALL}                                                              {Fore.CYAN}║{Style.RESET_ALL}
    {Fore.CYAN}╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
    """
    
    print(credits)
    print()
    input(f'{Fore.YELLOW}{Style.BRIGHT}Press Enter to continue...{Style.RESET_ALL}')

def clear():
    """Clear screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def read_csv_file():
    """Read and display CSV file"""
    try:
        print_header("READING CSV FILE", 80)
        print_info("Loading data from matchanalysis.csv...")
        print()
        
        ipl = pd.read_csv(csv_file, sep=",", header=0)
        ipl.drop(ipl.columns[ipl.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
        
        print_success(f"Successfully loaded {len(ipl)} records!")
        print()
        print_separator()
        print()
        
        # Display with better formatting
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', None)
        pd.set_option('display.max_colwidth', 30)
        print(ipl.to_string())
        
        print()
        print_separator()
        print_success(f"Total Records: {len(ipl)} | Total Columns: {len(ipl.columns)}")
        
    except FileNotFoundError:
        print_error(f"File '{csv_file}' not found!")
    except Exception as e:
        print_error(f"Error reading CSV file: {e}")

def clean_dataframe(df):
    """Helper function to clean unnamed columns from dataframe"""
    df = df.copy()
    df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
    return df

def validate_year(year):
    """Helper function to validate year input"""
    return 2008 <= year <= 2019

def data_analysis_menu():
    """Main data analysis menu"""
    # Load CSV once at the start
    try:
        print_info("Loading data...")
        ipl = pd.read_csv(csv_file, sep=",", header=0)
        df = clean_dataframe(pd.DataFrame(ipl))
        # Convert numeric columns to proper types
        numeric_cols = ['season', 'win_by_runs', 'win_by_wickets', 'dl_applied']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        print_success("Data loaded successfully!")
    except FileNotFoundError:
        print_error(f"File '{csv_file}' not found!")
        return
    except Exception as e:
        print_error(f"Error loading CSV file: {e}")
        return
    
    while True:
        clear()
        print_header("📊 DATA ANALYSIS MENU 📊", 80)
        print()
        
        menu_items = [
            ("1", "📋 WHOLE DATAFRAME", Fore.CYAN),
            ("2", "📑 DISPLAY COLUMNS", Fore.CYAN),
            ("3", "⬆️  DISPLAY TOP ROWS", Fore.CYAN),
            ("4", "⬇️  DISPLAY BOTTOM ROWS", Fore.CYAN),
            ("5", "🔍 DISPLAY SPECIFIC COLUMN", Fore.CYAN),
            ("6", "➕ ADD A NEW RECORD", Fore.GREEN),
            ("7", "📝 ADD A NEW COLUMN", Fore.GREEN),
            ("8", "🗑️  DELETE A COLUMN", Fore.RED),
            ("9", "❌ DELETE A RECORD", Fore.RED),
            ("10", "📅 TOTAL MATCHES IN A SEASON", Fore.YELLOW),
            ("11", "🏆 WINNER OF THE SEASON", Fore.YELLOW),
            ("12", "⭐ BEST PLAYER OF THE MATCH", Fore.YELLOW),
            ("13", "🏃 MATCH WIN BY MAXIMUM RUNS", Fore.MAGENTA),
            ("14", "🏃 MATCHES WIN BY MINIMUM RUNS", Fore.MAGENTA),
            ("15", "🎯 MATCH WIN BY MAXIMUM WICKETS", Fore.MAGENTA),
            ("16", "🎯 MATCHES WIN BY MINIMUM WICKETS", Fore.MAGENTA),
            ("17", "📊 MATCHES WON BY EACH TEAM", Fore.BLUE),
            ("18", "🪙 TOSS WINS BY EACH TEAM", Fore.BLUE),
            ("19", "📈 DATA SUMMARY", Fore.CYAN),
            ("20", "🔍 SEARCH MATCHES", Fore.MAGENTA),
            ("21", "⚔️  HEAD-TO-HEAD TEAM COMPARISON", Fore.YELLOW),
            ("22", "👤 PLAYER STATISTICS", Fore.CYAN),
            ("23", "🏟️  VENUE STATISTICS", Fore.BLUE),
            ("24", "💾 EXPORT DATA TO CSV", Fore.GREEN),
            ("25", "📊 ADVANCED STATISTICS", Fore.MAGENTA),
            ("26", "🚪 EXIT (To Main Menu)", Fore.RED),
        ]
        
        for num, item, color in menu_items:
            print_colored(f"  {num:>3}. {item}", color)
        
        print()
        print_separator()
        
        try:
            choice = int(input(f"{Fore.YELLOW}{Style.BRIGHT}Enter Choice (1-26): {Style.RESET_ALL}"))
        except ValueError:
            print_error("INVALID CHOICE - Please enter a number")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
            continue
            
        if choice == 1:
            print_header("WHOLE DATAFRAME", 80)
            df = clean_dataframe(df)
            pd.set_option('display.max_rows', 50)
            print(df.to_string())
            print()
            print_success(f"Displaying {len(df)} records")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

        elif choice == 2:
            print_header("DATAFRAME COLUMNS", 80)
            columns = df.columns.tolist()
            print()
            for i, col in enumerate(columns, 1):
                print_colored(f"  {i:>2}. {col}", Fore.CYAN)
            print()
            print_success(f"Total Columns: {len(columns)}")
            input(f'\n{Fore.YELLOW}Press any key to continue...{Style.RESET_ALL}')

        elif choice == 3:
            try:
                num_rows = int(input(f'{Fore.CYAN}Enter Total rows you want to show: {Style.RESET_ALL}'))
                df = clean_dataframe(df)
                print_header(f"TOP {num_rows} ROWS", 80)
                print()
                print(df.head(num_rows).to_string())
                print()
            except ValueError:
                print_error("Invalid input! Please enter a number.")
            input(f'\n{Fore.YELLOW}Press any key to continue...{Style.RESET_ALL}')
                
        elif choice == 4:
            try:
                num_rows = int(input(f'{Fore.CYAN}Enter Total rows you want to show: {Style.RESET_ALL}'))
                df = clean_dataframe(df)
                print_header(f"BOTTOM {num_rows} ROWS", 80)
                print()
                print(df.tail(num_rows).to_string())
                print()
            except ValueError:
                print_error("Invalid input! Please enter a number.")
            input(f'\n{Fore.YELLOW}Press any key to continue...{Style.RESET_ALL}')
                
        elif choice == 5:
            print_header("DISPLAY SPECIFIC COLUMN", 80)
            print()
            print_colored("Available Columns:", Fore.YELLOW, Style.BRIGHT)
            for i, col in enumerate(df.columns.tolist(), 1):
                print_colored(f"  {i:>2}. {col}", Fore.CYAN)
            print()
            col_name = input(f'{Fore.CYAN}Enter Column Name: {Style.RESET_ALL}')
            if col_name in df.columns:
                print()
                print_separator()
                print_colored(f"Column: {col_name}", Fore.YELLOW, Style.BRIGHT)
                print_separator()
                print(df[col_name].to_string())
                print()
            else:
                print_error(f"Column '{col_name}' not found!")
            input(f'\n{Fore.YELLOW}Press any key to continue...{Style.RESET_ALL}')
                
        elif choice == 6:
            print_header("ADD NEW RECORD", 80)
            try:
                print_info("Enter match details:")
                print()
                match_id = input(f'{Fore.CYAN}Match ID: {Style.RESET_ALL}')
                season = input(f'{Fore.CYAN}IPL Season: {Style.RESET_ALL}')
                city = input(f'{Fore.CYAN}City Name: {Style.RESET_ALL}')
                date = input(f'{Fore.CYAN}Match Date: {Style.RESET_ALL}')
                team1 = input(f'{Fore.CYAN}Team 1 Name: {Style.RESET_ALL}')
                team2 = input(f'{Fore.CYAN}Team 2 Name: {Style.RESET_ALL}')
                toss_winner = input(f'{Fore.CYAN}Toss Winner: {Style.RESET_ALL}')
                toss_decision = input(f'{Fore.CYAN}Toss Decision: {Style.RESET_ALL}')
                result = input(f'{Fore.CYAN}Result (Normal/tie/DL): {Style.RESET_ALL}')
                dl_applied = input(f'{Fore.CYAN}DL Applied (0/1): {Style.RESET_ALL}')
                winner = input(f'{Fore.CYAN}Winner Team: {Style.RESET_ALL}')
                win_by_runs = input(f'{Fore.CYAN}Win By Runs: {Style.RESET_ALL}')
                win_by_wickets = input(f'{Fore.CYAN}Win By Wickets: {Style.RESET_ALL}')
                player_of_match = input(f'{Fore.CYAN}Player of Match: {Style.RESET_ALL}')
                venue = input(f'{Fore.CYAN}Venue: {Style.RESET_ALL}')
                
                data = {'id': match_id, 'season': season, 'city': city, 'date': date, 
                       'team1': team1, 'team2': team2, 'toss_winner': toss_winner,
                       'toss_decision': toss_decision, 'result': result, 'dl_applied': dl_applied,
                       'winner': winner, 'win_by_runs': win_by_runs, 'win_by_wickets': win_by_wickets,
                       'player_of_match': player_of_match, 'venue': venue}
                new_row = pd.DataFrame([data])
                df = pd.concat([df, new_row], ignore_index=True)
                df = clean_dataframe(df)
                print()
                print_success("Record added successfully!")
                print()
                print(df.tail(1).to_string())
            except Exception as e:
                print_error(f"Error adding record: {e}")
            input(f'\n{Fore.YELLOW}Press any key to continue...{Style.RESET_ALL}')
                
        elif choice == 7:
            print_header("ADD NEW COLUMN", 80)
            col_name = input(f'{Fore.CYAN}Enter new column name: {Style.RESET_ALL}')
            col_value = input(f'{Fore.CYAN}Enter default column value: {Style.RESET_ALL}')
            df[col_name] = col_value
            df = clean_dataframe(df)
            print()
            print_success(f"Column '{col_name}' added successfully!")
            print()
            print(df.head().to_string())
            input(f'\n{Fore.YELLOW}Press any key to continue...{Style.RESET_ALL}')

        elif choice == 8:
            print_header("DELETE COLUMN", 80)
            print_colored("Available Columns:", Fore.YELLOW, Style.BRIGHT)
            for i, col in enumerate(df.columns.tolist(), 1):
                print_colored(f"  {i:>2}. {col}", Fore.CYAN)
            print()
            col_name = input(f'{Fore.CYAN}Enter column name to delete: {Style.RESET_ALL}')
            if col_name in df.columns:
                df = df.drop(columns=[col_name])
                df = clean_dataframe(df)
                print()
                print_success(f"Column '{col_name}' deleted successfully!")
                print()
                print(df.head().to_string())
            else:
                print_error(f"Column '{col_name}' not found!")
            input(f'\n{Fore.YELLOW}Press any key to continue...{Style.RESET_ALL}')

        elif choice == 9:
            print_header("DELETE RECORD", 80)
            try:
                print_info(f"Total records: {len(df)}")
                index_no = int(input(f'{Fore.CYAN}Enter Index Number to delete (0-{len(df)-1}): {Style.RESET_ALL}'))
                if 0 <= index_no < len(df):
                    deleted_record = df.iloc[index_no]
                    df = df.drop(df.index[index_no])
                    df = clean_dataframe(df)
                    print()
                    print_success("Record deleted successfully!")
                    print()
                    print_colored("Deleted Record:", Fore.YELLOW, Style.BRIGHT)
                    print(deleted_record.to_string())
                else:
                    print_error(f"Invalid index! Please enter a number between 0 and {len(df)-1}")
            except ValueError:
                print_error("Invalid input! Please enter a number.")
            input(f'\n{Fore.YELLOW}Press any key to continue...{Style.RESET_ALL}')
            
        elif choice == 10:
            try:
                year = int(input(f'{Fore.CYAN}Enter Year (2008-2019): {Style.RESET_ALL}'))
                if validate_year(year):
                    dfseason = df[df['season'] == year]
                    matches = len(dfseason)
                    print()
                    print_header(f"SEASON {year} STATISTICS", 80)
                    print()
                    print_colored(f"📅 Season: {year}", Fore.YELLOW, Style.BRIGHT)
                    print_colored(f"🏏 Total Matches: {matches}", Fore.GREEN, Style.BRIGHT)
                    print()
                else:
                    print_error("Enter year between 2008 and 2019")
            except (ValueError, KeyError) as e:
                print_error(f"Error: {e}")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
            
        elif choice == 11:
            try:
                year = int(input(f'{Fore.CYAN}Enter Year (2008-2019): {Style.RESET_ALL}'))
                if validate_year(year):
                    dfseason = df[df['season'] == year]
                    winner_mode = dfseason['winner'].mode()
                    print()
                    print_header(f"SEASON {year} WINNER", 80)
                    print()
                    if len(winner_mode) > 0:
                        print_colored(f"🏆 Winner of {year}: {winner_mode.iloc[0]}", Fore.GREEN, Style.BRIGHT)
                    else:
                        print_warning(f"No winner data found for {year}")
                else:
                    print_error("Enter year between 2008 and 2019")
            except ValueError:
                print_error("Invalid input! Please enter a number.")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
                
        elif choice == 12:
            try:
                year = int(input(f'{Fore.CYAN}Enter Year (2008-2019): {Style.RESET_ALL}'))
                if validate_year(year):
                    dfseason = df[df['season'] == year]
                    player_mode = dfseason['player_of_match'].mode()
                    print()
                    print_header(f"SEASON {year} BEST PLAYER", 80)
                    print()
                    if len(player_mode) > 0:
                        print_colored(f"⭐ Best Player of {year}: {player_mode.iloc[0]}", Fore.YELLOW, Style.BRIGHT)
                    else:
                        print_warning(f"No player data found for {year}")
                else:
                    print_error("Enter year between 2008 and 2019")
            except ValueError:
                print_error("Invalid input! Please enter a number.")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

        elif choice == 13:
            try:
                year = int(input(f'{Fore.CYAN}Enter Year (2008-2019): {Style.RESET_ALL}'))
                if validate_year(year):
                    dfseason = df[df['season'] == year].copy()
                    dfseason = clean_dataframe(dfseason)
                    runs_wins = dfseason[dfseason['win_by_runs'] > 0]
                    print()
                    print_header(f"MAXIMUM RUNS WIN - {year}", 80)
                    print()
                    if len(runs_wins) > 0:
                        max_idx = runs_wins['win_by_runs'].idxmax()
                        match = dfseason.loc[max_idx]
                        print_colored(f"🏆 Maximum Win by Runs: {match['win_by_runs']}", Fore.GREEN, Style.BRIGHT)
                        print()
                        print(match.to_string())
                    else:
                        print_warning(f"No matches won by runs found for {year}")
                else:
                    print_error("Enter year between 2008 and 2019")
            except (ValueError, KeyError) as e:
                print_error(f"Error: {e}")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
                
        elif choice == 14:
            try:
                year = int(input(f'{Fore.CYAN}Enter Year (2008-2019): {Style.RESET_ALL}'))
                if validate_year(year):
                    dfseason = df[df['season'] == year].copy()
                    dfseason = clean_dataframe(dfseason)
                    runs_wins = dfseason[dfseason['win_by_runs'] > 0]
                    print()
                    print_header(f"MINIMUM RUNS WIN - {year}", 80)
                    print()
                    if len(runs_wins) > 0:
                        min_idx = runs_wins['win_by_runs'].idxmin()
                        match = dfseason.loc[min_idx]
                        print_colored(f"🏃 Minimum Win by Runs: {match['win_by_runs']}", Fore.YELLOW, Style.BRIGHT)
                        print()
                        print(match.to_string())
                    else:
                        print_warning(f"No matches won by runs found for {year}")
                else:
                    print_error("Enter year between 2008 and 2019")
            except (ValueError, KeyError) as e:
                print_error(f"Error: {e}")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

        elif choice == 15:
            try:
                year = int(input(f'{Fore.CYAN}Enter Year (2008-2019): {Style.RESET_ALL}'))
                if validate_year(year):
                    dfseason = df[df['season'] == year].copy()
                    dfseason = clean_dataframe(dfseason)
                    wickets_wins = dfseason[dfseason['win_by_wickets'] > 0]
                    print()
                    print_header(f"MAXIMUM WICKETS WIN - {year}", 80)
                    print()
                    if len(wickets_wins) > 0:
                        max_idx = wickets_wins['win_by_wickets'].idxmax()
                        match = dfseason.loc[max_idx]
                        print_colored(f"🎯 Maximum Win by Wickets: {match['win_by_wickets']}", Fore.GREEN, Style.BRIGHT)
                        print()
                        print(match.to_string())
                    else:
                        print_warning(f"No matches won by wickets found for {year}")
                else:
                    print_error("Enter year between 2008 and 2019")
            except (ValueError, KeyError) as e:
                print_error(f"Error: {e}")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
            
        elif choice == 16:
            try:
                year = int(input(f'{Fore.CYAN}Enter Year (2008-2019): {Style.RESET_ALL}'))
                if validate_year(year):
                    dfseason = df[df['season'] == year].copy()
                    dfseason = clean_dataframe(dfseason)
                    wickets_wins = dfseason[dfseason['win_by_wickets'] > 0]
                    print()
                    print_header(f"MINIMUM WICKETS WIN - {year}", 80)
                    print()
                    if len(wickets_wins) > 0:
                        min_idx = wickets_wins['win_by_wickets'].idxmin()
                        match = dfseason.loc[min_idx]
                        print_colored(f"🎯 Minimum Win by Wickets: {match['win_by_wickets']}", Fore.YELLOW, Style.BRIGHT)
                        print()
                        print(match.to_string())
                    else:
                        print_warning(f"No matches won by wickets found for {year}")
                else:
                    print_error("Enter year between 2008 and 2019")
            except (ValueError, KeyError) as e:
                print_error(f"Error: {e}")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
                
        elif choice == 17:
            try:
                year = int(input(f'{Fore.CYAN}Enter Year (2008-2019): {Style.RESET_ALL}'))
                if validate_year(year):
                    dfseason = df[df['season'] == year]
                    dfseason = clean_dataframe(dfseason)
                    wins = dfseason['winner'].value_counts()
                    print()
                    print_header(f"MATCHES WON BY EACH TEAM - {year}", 80)
                    print()
                    for team, count in wins.items():
                        print_colored(f"  {team:<40} {count:>3} wins", Fore.GREEN)
                    print()
                    print_success(f"Total Teams: {len(wins)}")
                else:
                    print_error("Enter year between 2008 and 2019")
            except ValueError:
                print_error("Invalid input! Please enter a number.")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
                    
                
        elif choice == 18:
            try:
                year = int(input(f'{Fore.CYAN}Enter Year (2008-2019): {Style.RESET_ALL}'))
                if validate_year(year):
                    dfseason = df[df['season'] == year]
                    toss_wins = dfseason['toss_winner'].value_counts()
                    print()
                    print_header(f"TOSS WINS BY EACH TEAM - {year}", 80)
                    print()
                    for team, count in toss_wins.items():
                        print_colored(f"  {team:<40} {count:>3} toss wins", Fore.CYAN)
                    print()
                    print_success(f"Total Teams: {len(toss_wins)}")
                else:
                    print_error("Enter year between 2008 and 2019")
            except ValueError:
                print_error("Invalid input! Please enter a number.")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

                 
        elif choice == 19:
            print_header("DATA SUMMARY", 80)
            print()
            print(df.describe().to_string())
            print()
            print_separator()
            print_colored(f"Total Records: {len(df)}", Fore.GREEN, Style.BRIGHT)
            print_colored(f"Total Columns: {len(df.columns)}", Fore.GREEN, Style.BRIGHT)
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
                
        elif choice == 20:
            # Search matches
            print_header("SEARCH MATCHES", 80)
            print()
            print_colored("Search Options:", Fore.YELLOW, Style.BRIGHT)
            print_colored("1. Search by Team", Fore.CYAN)
            print_colored("2. Search by Player", Fore.CYAN)
            print_colored("3. Search by Venue", Fore.CYAN)
            print_colored("4. Search by Season", Fore.CYAN)
            print()
            search_choice = input(f'{Fore.CYAN}Enter search option (1-4): {Style.RESET_ALL}')
            
            if search_choice == '1':
                team_name = input(f'{Fore.CYAN}Enter Team Name: {Style.RESET_ALL}')
                results = df[(df['team1'] == team_name) | (df['team2'] == team_name) | (df['winner'] == team_name)]
                print()
                print_header(f"MATCHES FOR {team_name.upper()}", 80)
                print()
                if len(results) > 0:
                    print(results[['season', 'date', 'team1', 'team2', 'winner', 'venue']].to_string())
                    print()
                    print_success(f"Total Matches: {len(results)}")
                else:
                    print_warning(f"No matches found for {team_name}")
                    
            elif search_choice == '2':
                player_name = input(f'{Fore.CYAN}Enter Player Name: {Style.RESET_ALL}')
                results = df[df['player_of_match'].str.contains(player_name, case=False, na=False)]
                print()
                print_header(f"MATCHES - {player_name.upper()} AS PLAYER OF MATCH", 80)
                print()
                if len(results) > 0:
                    print(results[['season', 'date', 'team1', 'team2', 'winner', 'player_of_match']].to_string())
                    print()
                    print_success(f"Total Matches: {len(results)}")
                else:
                    print_warning(f"No matches found for {player_name}")
                    
            elif search_choice == '3':
                venue_name = input(f'{Fore.CYAN}Enter Venue Name: {Style.RESET_ALL}')
                results = df[df['venue'].str.contains(venue_name, case=False, na=False)]
                print()
                print_header(f"MATCHES AT {venue_name.upper()}", 80)
                print()
                if len(results) > 0:
                    print(results[['season', 'date', 'team1', 'team2', 'winner', 'venue']].to_string())
                    print()
                    print_success(f"Total Matches: {len(results)}")
                else:
                    print_warning(f"No matches found at {venue_name}")
                    
            elif search_choice == '4':
                try:
                    season = int(input(f'{Fore.CYAN}Enter Season (2008-2019): {Style.RESET_ALL}'))
                    results = df[df['season'] == season]
                    print()
                    print_header(f"MATCHES IN SEASON {season}", 80)
                    print()
                    if len(results) > 0:
                        print(results[['date', 'team1', 'team2', 'winner', 'venue', 'player_of_match']].to_string())
                        print()
                        print_success(f"Total Matches: {len(results)}")
                    else:
                        print_warning(f"No matches found for season {season}")
                except ValueError:
                    print_error("Invalid input! Please enter a number.")
            else:
                print_error("Invalid search option!")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

        elif choice == 21:
            # Head-to-head team comparison
            print_header("HEAD-TO-HEAD TEAM COMPARISON", 80)
            print()
            team1 = input(f'{Fore.CYAN}Enter First Team Name: {Style.RESET_ALL}')
            team2 = input(f'{Fore.CYAN}Enter Second Team Name: {Style.RESET_ALL}')
            
            # Find matches between these two teams
            h2h = df[((df['team1'] == team1) & (df['team2'] == team2)) | 
                    ((df['team1'] == team2) & (df['team2'] == team1))]
            
            if len(h2h) > 0:
                team1_wins = len(h2h[h2h['winner'] == team1])
                team2_wins = len(h2h[h2h['winner'] == team2])
                no_result = len(h2h) - team1_wins - team2_wins
                
                print()
                print_header(f"{team1.upper()} vs {team2.upper()}", 80)
                print()
                print_colored(f"Total Matches: {len(h2h)}", Fore.YELLOW, Style.BRIGHT)
                print_colored(f"{team1} Wins: {team1_wins}", Fore.GREEN, Style.BRIGHT)
                print_colored(f"{team2} Wins: {team2_wins}", Fore.GREEN, Style.BRIGHT)
                if no_result > 0:
                    print_colored(f"No Result/Tie: {no_result}", Fore.YELLOW, Style.BRIGHT)
                print()
                print_colored("Recent Matches:", Fore.CYAN, Style.BRIGHT)
                print(h2h[['season', 'date', 'team1', 'team2', 'winner', 'venue']].tail(10).to_string())
            else:
                print_warning(f"No matches found between {team1} and {team2}")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

        elif choice == 22:
            # Player statistics
            print_header("PLAYER STATISTICS", 80)
            print()
            player_name = input(f'{Fore.CYAN}Enter Player Name: {Style.RESET_ALL}')
            player_matches = df[df['player_of_match'].str.contains(player_name, case=False, na=False)]
            
            if len(player_matches) > 0:
                print()
                print_header(f"{player_name.upper()} STATISTICS", 80)
                print()
                print_colored(f"Total Player of Match Awards: {len(player_matches)}", Fore.GREEN, Style.BRIGHT)
                print()
                
                # Awards by season
                awards_by_season = player_matches['season'].value_counts().sort_index()
                print_colored("Awards by Season:", Fore.YELLOW, Style.BRIGHT)
                for season, count in awards_by_season.items():
                    print_colored(f"  {season}: {count} award(s)", Fore.CYAN)
                print()
                
                # Teams played for
                teams = set()
                for _, match in player_matches.iterrows():
                    if player_name.lower() in match.get('team1', '').lower():
                        teams.add(match['team1'])
                    if player_name.lower() in match.get('team2', '').lower():
                        teams.add(match['team2'])
                
                if teams:
                    print_colored(f"Teams: {', '.join(teams)}", Fore.CYAN)
                print()
                print_colored("Recent Awards:", Fore.YELLOW, Style.BRIGHT)
                print(player_matches[['season', 'date', 'team1', 'team2', 'winner', 'venue']].tail(10).to_string())
            else:
                print_warning(f"No statistics found for {player_name}")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

        elif choice == 23:
            # Venue statistics
            print_header("VENUE STATISTICS", 80)
            print()
            venue_name = input(f'{Fore.CYAN}Enter Venue Name (or press Enter for all venues): {Style.RESET_ALL}')
            
            if venue_name.strip():
                venue_matches = df[df['venue'].str.contains(venue_name, case=False, na=False)]
                if len(venue_matches) > 0:
                    print()
                    print_header(f"STATISTICS FOR {venue_name.upper()}", 80)
                    print()
                    print_colored(f"Total Matches: {len(venue_matches)}", Fore.GREEN, Style.BRIGHT)
                    print()
                    
                    # Most successful team at this venue
                    winners = venue_matches['winner'].value_counts()
                    print_colored("Most Successful Teams:", Fore.YELLOW, Style.BRIGHT)
                    for team, wins in winners.head(5).items():
                        print_colored(f"  {team}: {wins} wins", Fore.CYAN)
                    print()
                    
                    # Matches by season
                    season_counts = venue_matches['season'].value_counts().sort_index()
                    print_colored("Matches by Season:", Fore.YELLOW, Style.BRIGHT)
                    for season, count in season_counts.items():
                        print_colored(f"  {season}: {count} match(es)", Fore.CYAN)
                else:
                    print_warning(f"No matches found at {venue_name}")
            else:
                # Show all venues
                venue_stats = df.groupby('venue').agg({
                    'id': 'count',
                    'winner': lambda x: x.value_counts().index[0] if len(x) > 0 else 'N/A'
                }).rename(columns={'id': 'Total Matches', 'winner': 'Most Successful Team'})
                venue_stats = venue_stats.sort_values('Total Matches', ascending=False)
                print()
                print_header("ALL VENUES STATISTICS", 80)
                print()
                print(venue_stats.to_string())
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

        elif choice == 24:
            # Export data
            print_header("EXPORT DATA TO CSV", 80)
            print()
            print_colored("Export Options:", Fore.YELLOW, Style.BRIGHT)
            print_colored("1. Export All Data", Fore.CYAN)
            print_colored("2. Export Filtered Data by Season", Fore.CYAN)
            print_colored("3. Export Filtered Data by Team", Fore.CYAN)
            print()
            export_choice = input(f'{Fore.CYAN}Enter option (1-3): {Style.RESET_ALL}')
            
            try:
                if export_choice == '1':
                    filename = input(f'{Fore.CYAN}Enter filename (without .csv): {Style.RESET_ALL}')
                    if not filename:
                        filename = 'ipl_export'
                    df.to_csv(f'{filename}.csv', index=False)
                    print_success(f"Data exported to {filename}.csv")
                    
                elif export_choice == '2':
                    year = int(input(f'{Fore.CYAN}Enter Season (2008-2019): {Style.RESET_ALL}'))
                    if validate_year(year):
                        filtered_df = df[df['season'] == year]
                        filename = input(f'{Fore.CYAN}Enter filename (without .csv): {Style.RESET_ALL}')
                        if not filename:
                            filename = f'ipl_season_{year}'
                        filtered_df.to_csv(f'{filename}.csv', index=False)
                        print_success(f"Season {year} data exported to {filename}.csv ({len(filtered_df)} records)")
                    else:
                        print_error("Invalid year!")
                        
                elif export_choice == '3':
                    team_name = input(f'{Fore.CYAN}Enter Team Name: {Style.RESET_ALL}')
                    filtered_df = df[(df['team1'] == team_name) | (df['team2'] == team_name) | (df['winner'] == team_name)]
                    if len(filtered_df) > 0:
                        filename = input(f'{Fore.CYAN}Enter filename (without .csv): {Style.RESET_ALL}')
                        if not filename:
                            filename = f'ipl_team_{team_name.replace(" ", "_")}'
                        filtered_df.to_csv(f'{filename}.csv', index=False)
                        print_success(f"Team {team_name} data exported to {filename}.csv ({len(filtered_df)} records)")
                    else:
                        print_warning(f"No data found for {team_name}")
                else:
                    print_error("Invalid option!")
            except Exception as e:
                print_error(f"Error exporting data: {e}")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

        elif choice == 25:
            # Advanced statistics
            print_header("ADVANCED STATISTICS", 80)
            print()
            print_colored("Advanced Statistics Options:", Fore.YELLOW, Style.BRIGHT)
            print_colored("1. Win Percentage by Team", Fore.CYAN)
            print_colored("2. Home vs Away Performance", Fore.CYAN)
            print_colored("3. Toss Win vs Match Win Analysis", Fore.CYAN)
            print_colored("4. Most Consistent Teams", Fore.CYAN)
            print_colored("5. Season-wise Team Performance", Fore.CYAN)
            print()
            stat_choice = input(f'{Fore.CYAN}Enter option (1-5): {Style.RESET_ALL}')
            
            if stat_choice == '1':
                # Win percentage
                print()
                print_header("WIN PERCENTAGE BY TEAM", 80)
                print()
                all_teams = set(df['team1'].unique()) | set(df['team2'].unique())
                win_stats = []
                
                for team in sorted(all_teams):
                    team_matches = df[(df['team1'] == team) | (df['team2'] == team)]
                    wins = len(team_matches[team_matches['winner'] == team])
                    total = len(team_matches)
                    if total > 0:
                        win_pct = (wins / total) * 100
                        win_stats.append({
                            'Team': team,
                            'Matches': total,
                            'Wins': wins,
                            'Losses': total - wins,
                            'Win %': f"{win_pct:.2f}%"
                        })
                
                win_df = pd.DataFrame(win_stats).sort_values('Win %', ascending=False)
                print(win_df.to_string(index=False))
                
            elif stat_choice == '2':
                # Home vs Away (using venue city correlation)
                print()
                print_header("HOME PERFORMANCE ANALYSIS", 80)
                print()
                print_info("Note: Home team is determined by venue city correlation")
                team_name = input(f'{Fore.CYAN}Enter Team Name: {Style.RESET_ALL}')
                team_matches = df[(df['team1'] == team_name) | (df['team2'] == team_name)]
                
                if len(team_matches) > 0:
                    # Simple analysis: matches where team won
                    wins = len(team_matches[team_matches['winner'] == team_name])
                    print_colored(f"Total Matches: {len(team_matches)}", Fore.GREEN, Style.BRIGHT)
                    print_colored(f"Total Wins: {wins}", Fore.GREEN, Style.BRIGHT)
                    print_colored(f"Win Percentage: {(wins/len(team_matches)*100):.2f}%", Fore.GREEN, Style.BRIGHT)
                else:
                    print_warning(f"No data found for {team_name}")
                    
            elif stat_choice == '3':
                # Toss win vs match win
                print()
                print_header("TOSS WIN vs MATCH WIN ANALYSIS", 80)
                print()
                toss_winners = df[df['toss_winner'].notna()]
                toss_and_match_wins = len(toss_winners[toss_winners['toss_winner'] == toss_winners['winner']])
                total_toss_wins = len(toss_winners)
                
                print_colored(f"Total Matches with Toss Data: {total_toss_wins}", Fore.YELLOW, Style.BRIGHT)
                print_colored(f"Matches won by Toss Winner: {toss_and_match_wins}", Fore.GREEN, Style.BRIGHT)
                print_colored(f"Win Rate after Toss Win: {(toss_and_match_wins/total_toss_wins*100):.2f}%", Fore.GREEN, Style.BRIGHT)
                print()
                
                # By team
                team_toss_analysis = {}
                for team in df['toss_winner'].unique():
                    if pd.notna(team):
                        team_toss_wins = df[df['toss_winner'] == team]
                        match_wins_after_toss = len(team_toss_wins[team_toss_wins['winner'] == team])
                        if len(team_toss_wins) > 10:  # Only teams with significant data
                            team_toss_analysis[team] = {
                                'Toss Wins': len(team_toss_wins),
                                'Match Wins After Toss': match_wins_after_toss,
                                'Win %': f"{(match_wins_after_toss/len(team_toss_wins)*100):.2f}%"
                            }
                
                if team_toss_analysis:
                    print_colored("Team-wise Toss Win Analysis:", Fore.YELLOW, Style.BRIGHT)
                    toss_df = pd.DataFrame(team_toss_analysis).T.sort_values('Win %', ascending=False)
                    print(toss_df.to_string())
                    
            elif stat_choice == '4':
                # Most consistent teams (low variance in performance)
                print()
                print_header("MOST CONSISTENT TEAMS", 80)
                print()
                all_teams = set(df['team1'].unique()) | set(df['team2'].unique())
                consistency_stats = []
                
                for team in sorted(all_teams):
                    team_seasons = df[((df['team1'] == team) | (df['team2'] == team)) & 
                                     (df['season'].notna())]
                    if len(team_seasons) > 20:  # Only teams with significant matches
                        wins_by_season = team_seasons[team_seasons['winner'] == team].groupby('season').size()
                        if len(wins_by_season) > 2:
                            avg_wins = wins_by_season.mean()
                            std_wins = wins_by_season.std()
                            consistency_stats.append({
                                'Team': team,
                                'Avg Wins/Season': f"{avg_wins:.2f}",
                                'Std Deviation': f"{std_wins:.2f}",
                                'Consistency Score': f"{(avg_wins/(std_wins+0.1)):.2f}" if std_wins > 0 else "N/A"
                            })
                
                if consistency_stats:
                    cons_df = pd.DataFrame(consistency_stats).sort_values('Consistency Score', ascending=False, na_position='last')
                    print(cons_df.to_string(index=False))
                else:
                    print_warning("Insufficient data for consistency analysis")
                    
            elif stat_choice == '5':
                # Season-wise team performance
                print()
                print_header("SEASON-WISE TEAM PERFORMANCE", 80)
                print()
                team_name = input(f'{Fore.CYAN}Enter Team Name: {Style.RESET_ALL}')
                team_matches = df[((df['team1'] == team_name) | (df['team2'] == team_name))]
                
                if len(team_matches) > 0:
                    season_performance = []
                    for season in sorted(team_matches['season'].unique()):
                        season_matches = team_matches[team_matches['season'] == season]
                        wins = len(season_matches[season_matches['winner'] == team_name])
                        total = len(season_matches)
                        season_performance.append({
                            'Season': int(season),
                            'Matches': total,
                            'Wins': wins,
                            'Win %': f"{(wins/total*100):.2f}%"
                        })
                    
                    perf_df = pd.DataFrame(season_performance)
                    print()
                    print_colored(f"Performance of {team_name}:", Fore.YELLOW, Style.BRIGHT)
                    print(perf_df.to_string(index=False))
                else:
                    print_warning(f"No data found for {team_name}")
            else:
                print_error("Invalid option!")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

        elif choice == 26:
            break
        else:
            print_error("INVALID CHOICE")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
                
def graph():
    """Graph visualization menu"""
    clear()
    try:
        print_info("Loading data for visualization...")
        ipl = pd.read_csv(csv_file, sep=",", header=0)
        df = clean_dataframe(pd.DataFrame(ipl))
        # Convert numeric columns to proper types
        numeric_cols = ['season', 'win_by_runs', 'win_by_wickets', 'dl_applied']
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors='coerce')
        print_success("Data loaded successfully!")
    except FileNotFoundError:
        print_error(f"File '{csv_file}' not found!")
        return
    except Exception as e:
        print_error(f"Error loading CSV file: {e}")
        return
        
    while True:
        clear()
        print_header("📈 GRAPH VISUALIZATION MENU 📈", 80)
        print()
        
        graph_menu = [
            ("1", "📊 Season wise Matches - Line Graph", Fore.CYAN),
            ("2", "📊 Season wise Matches - Bar Graph", Fore.CYAN),
            ("3", "📊 Season wise Matches - Horizontal Bar", Fore.CYAN),
            ("4", "🏆 Most Successful Team - Bar Graph", Fore.GREEN),
            ("5", "🏏 Match played by each Team - Line", Fore.YELLOW),
            ("6", "🏏 Match played by each Team - Bar", Fore.YELLOW),
            ("7", "🏟️  Matches per venue - Line Graph", Fore.MAGENTA),
            ("8", "🏟️  Matches per venue - Bar Graph", Fore.MAGENTA),
            ("9", "🏟️  Matches per venue - Horizontal Bar", Fore.MAGENTA),
            ("10", "🪙 Toss win by each team - Line", Fore.BLUE),
            ("11", "🪙 Toss win by each team - Bar", Fore.BLUE),
            ("12", "🪙 Toss win by each team - Horizontal Bar", Fore.BLUE),
            ("13", "🎲 Toss decision frequency - Bar Graph", Fore.CYAN),
            ("14", "🥧 Match result - PIE CHART", Fore.RED),
            ("15", "📊 Player of Match - HISTOGRAM", Fore.YELLOW),
            ("16", "🚪 Exit (Move to Main Menu)", Fore.RED),
        ]
        
        for num, item, color in graph_menu:
            print_colored(f"  {num:>3}. {item}", color)
        
        print()
        print_separator()
        
        try:
            ch = int(input(f'{Fore.YELLOW}{Style.BRIGHT}Enter Your Choice (1-16): {Style.RESET_ALL}'))
        except ValueError:
            print_error("Invalid input! Please enter a number.")
            input(f"\n{Fore.YELLOW}Press Enter to Continue...{Style.RESET_ALL}")
            continue

        try:
            if ch == 1:
                    season_counts = df['season'].value_counts().sort_index()
                    plt.figure(figsize=(12, 7), facecolor='#f0f0f0')
                    plt.plot(season_counts.index, season_counts.values, marker='o', linewidth=3, 
                            markersize=10, color='#2E86AB', markerfacecolor='#A23B72')
                    plt.xlabel('Season', fontsize=12, fontweight='bold')
                    plt.ylabel('Number of Matches', fontsize=12, fontweight='bold')
                    plt.title('Season wise Matches - Line Graph', fontsize=14, fontweight='bold', pad=20)
                    plt.grid(True, alpha=0.3, linestyle='--')
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()

            elif ch == 2:
                    season_counts = df['season'].value_counts().sort_index()
                    plt.figure(figsize=(12, 7), facecolor='#f0f0f0')
                    bars = plt.bar(season_counts.index, season_counts.values, color='#2E86AB', edgecolor='#1B4F72', linewidth=2)
                    plt.xlabel('Season', fontsize=12, fontweight='bold')
                    plt.ylabel('Number of Matches', fontsize=12, fontweight='bold')
                    plt.title('Season wise Matches - Bar Graph', fontsize=14, fontweight='bold', pad=20)
                    plt.grid(True, axis='y', alpha=0.3, linestyle='--')
                    plt.xticks(rotation=45)
                    for bar in bars:
                        height = bar.get_height()
                        plt.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}',
                                ha='center', va='bottom', fontweight='bold')
                    plt.tight_layout()
                    plt.show()
                
            elif ch == 3:
                    season_counts = df['season'].value_counts().sort_index()
                    plt.figure(figsize=(10, 8), facecolor='#f0f0f0')
                    bars = plt.barh(season_counts.index, season_counts.values, color='#A23B72', edgecolor='#6B1F3A', linewidth=2)
                    plt.xlabel('Number of Matches', fontsize=12, fontweight='bold')
                    plt.ylabel('Season', fontsize=12, fontweight='bold')
                    plt.title('Season wise Matches - Horizontal Bar', fontsize=14, fontweight='bold', pad=20)
                    plt.grid(True, axis='x', alpha=0.3, linestyle='--')
                    for i, bar in enumerate(bars):
                        width = bar.get_width()
                        plt.text(width, bar.get_y() + bar.get_height()/2., f'{int(width)}',
                                ha='left', va='center', fontweight='bold', fontsize=10)
                    plt.tight_layout()
                    plt.show()
            

            elif ch == 4:
                    winner_counts = df['winner'].value_counts()
                    plt.figure(figsize=(12, 10), facecolor='#f0f0f0')
                    bars = plt.barh(winner_counts.index, winner_counts.values, 
                                color=plt.cm.viridis(np.linspace(0, 1, len(winner_counts))), 
                                edgecolor='black', linewidth=1.5)
                    plt.xlabel('Matches Won', fontsize=12, fontweight='bold')
                    plt.ylabel('Teams', fontsize=12, fontweight='bold')
                    plt.title('Most Successful Team', fontsize=14, fontweight='bold', pad=20)
                    plt.grid(True, axis='x', alpha=0.3, linestyle='--')
                    for i, bar in enumerate(bars):
                        width = bar.get_width()
                        plt.text(width, bar.get_y() + bar.get_height()/2., f'{int(width)}',
                                ha='left', va='center', fontweight='bold', fontsize=9)
                    plt.tight_layout()
                    plt.show()


            elif ch == 5:
                team1_counts = df['team1'].value_counts()
                team2_counts = df['team2'].value_counts()
                total_matches = (team1_counts + team2_counts).sort_values(ascending=False)
                plt.figure(figsize=(14, 7), facecolor='#f0f0f0')
                plt.plot(range(len(total_matches)), total_matches.values, marker='o', 
                        linewidth=3, markersize=8, color='#F18F01')
                plt.xticks(range(len(total_matches)), total_matches.index, rotation=45, ha='right')
                plt.title('Match played by each team - Line Graph', fontsize=14, fontweight='bold', pad=20)
                plt.xlabel('Teams', fontsize=12, fontweight='bold')
                plt.ylabel('Number of Matches', fontsize=12, fontweight='bold')
                plt.grid(True, alpha=0.3, linestyle='--')
                plt.tight_layout()
                plt.show()

            elif ch == 6:
                team1_counts = df['team1'].value_counts()
                team2_counts = df['team2'].value_counts()
                total_matches = (team1_counts + team2_counts).sort_values(ascending=False)
                plt.figure(figsize=(12, 10), facecolor='#f0f0f0')
                bars = total_matches.plot(kind='barh', color=plt.cm.plasma(np.linspace(0, 1, len(total_matches))), 
                                            edgecolor='black', linewidth=1.5)
                plt.title('Match played by each team - Bar Graph', fontsize=14, fontweight='bold', pad=20)
                plt.xlabel('Number of Matches', fontsize=12, fontweight='bold')
                plt.ylabel('Teams', fontsize=12, fontweight='bold')
                plt.grid(True, axis='x', alpha=0.3, linestyle='--')
                plt.tight_layout()
                plt.show()

            elif ch == 7:
                    venue_counts = df['venue'].value_counts()
                    plt.figure(figsize=(14, 7), facecolor='#f0f0f0')
                    plt.plot(range(len(venue_counts)), venue_counts.values, marker='o', 
                            linewidth=2, markersize=6, color='#C73E1D')
                    plt.xticks(range(len(venue_counts)), venue_counts.index, rotation=90, ha='center')
                    plt.xlabel('Venue', fontsize=12, fontweight='bold')
                    plt.ylabel('Number of Matches', fontsize=12, fontweight='bold')
                    plt.title('No. of matches per venue - Line Graph', fontsize=14, fontweight='bold', pad=20)
                    plt.grid(True, alpha=0.3, linestyle='--')
                    plt.tight_layout()
                    plt.show()

            elif ch == 8:
                    venue_counts = df['venue'].value_counts()
                    plt.figure(figsize=(14, 7), facecolor='#f0f0f0')
                    bars = plt.bar(range(len(venue_counts)), venue_counts.values, 
                                color=plt.cm.Set3(np.linspace(0, 1, len(venue_counts))),
                                edgecolor='black', linewidth=1)
                    plt.xticks(range(len(venue_counts)), venue_counts.index, rotation=90, ha='center')
                    plt.xlabel('Venue', fontsize=12, fontweight='bold')
                    plt.ylabel('Number of Matches', fontsize=12, fontweight='bold')
                    plt.title('No. of matches per venue - Bar Graph', fontsize=14, fontweight='bold', pad=20)
                    plt.grid(True, axis='y', alpha=0.3, linestyle='--')
                    plt.tight_layout()
                    plt.show()

            elif ch == 9:
                    venue_counts = df['venue'].value_counts()
                    plt.figure(figsize=(12, max(10, len(venue_counts) * 0.4)), facecolor='#f0f0f0')
                    bars = plt.barh(range(len(venue_counts)), venue_counts.values,
                                color=plt.cm.tab20(np.linspace(0, 1, len(venue_counts))),
                                edgecolor='black', linewidth=1)
                    plt.yticks(range(len(venue_counts)), venue_counts.index)
                    plt.xlabel('Number of Matches', fontsize=12, fontweight='bold')
                    plt.ylabel('Venue', fontsize=12, fontweight='bold')
                    plt.title('No. of matches per venue - Horizontal Bar', fontsize=14, fontweight='bold', pad=20)
                    plt.grid(True, axis='x', alpha=0.3, linestyle='--')
                    plt.tight_layout()
                    plt.show()

            elif ch == 10:
                    toss_counts = df['toss_winner'].value_counts()
                    plt.figure(figsize=(14, 7), facecolor='#f0f0f0')
                    plt.plot(range(len(toss_counts)), toss_counts.values, marker='s', 
                            linewidth=3, markersize=8, color='#06A77D')
                    plt.xticks(range(len(toss_counts)), toss_counts.index, rotation=90, ha='center')
                    plt.xlabel('Team', fontsize=12, fontweight='bold')
                    plt.ylabel('Toss Wins', fontsize=12, fontweight='bold')
                    plt.title('No. of Toss Win by each team - Line Graph', fontsize=14, fontweight='bold', pad=20)
                    plt.grid(True, alpha=0.3, linestyle='--')
                    plt.tight_layout()
                    plt.show()

            elif ch == 11:
                    toss_counts = df['toss_winner'].value_counts()
                    plt.figure(figsize=(14, 7), facecolor='#f0f0f0')
                    bars = plt.bar(range(len(toss_counts)), toss_counts.values,
                                color=plt.cm.coolwarm(np.linspace(0, 1, len(toss_counts))),
                                edgecolor='black', linewidth=1.5)
                    plt.xticks(range(len(toss_counts)), toss_counts.index, rotation=90, ha='center')
                    plt.xlabel('Team', fontsize=12, fontweight='bold')
                    plt.ylabel('Toss Wins', fontsize=12, fontweight='bold')
                    plt.title('No. of Toss Win by each team - Bar Graph', fontsize=14, fontweight='bold', pad=20)
                    plt.grid(True, axis='y', alpha=0.3, linestyle='--')
                    for bar in bars:
                        height = bar.get_height()
                        plt.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}',
                                ha='center', va='bottom', fontweight='bold', fontsize=9)
                    plt.tight_layout()
                    plt.show()

            elif ch == 12:
                    toss_counts = df['toss_winner'].value_counts()
                    plt.figure(figsize=(12, max(10, len(toss_counts) * 0.4)), facecolor='#f0f0f0')
                    bars = plt.barh(range(len(toss_counts)), toss_counts.values,
                                color=plt.cm.RdYlGn(np.linspace(0, 1, len(toss_counts))),
                                edgecolor='black', linewidth=1.5)
                    plt.yticks(range(len(toss_counts)), toss_counts.index)
                    plt.xlabel('Toss Wins', fontsize=12, fontweight='bold')
                    plt.ylabel('Team', fontsize=12, fontweight='bold')
                    plt.title('No. of Toss Win by each team - Horizontal Bar', fontsize=14, fontweight='bold', pad=20)
                    plt.grid(True, axis='x', alpha=0.3, linestyle='--')
                    plt.tight_layout()
                    plt.show()

            elif ch == 13:
                    decision_counts = df['toss_decision'].value_counts()
                    plt.figure(figsize=(10, 7), facecolor='#f0f0f0')
                    bars = plt.bar(decision_counts.index, decision_counts.values,
                                color=['#FF6B6B', '#4ECDC4'], edgecolor='black', linewidth=2)
                    plt.xlabel('Toss Decision', fontsize=12, fontweight='bold')
                    plt.ylabel('Number of Matches', fontsize=12, fontweight='bold')
                    plt.title('No. of times which toss decision is taken', fontsize=14, fontweight='bold', pad=20)
                    plt.grid(True, axis='y', alpha=0.3, linestyle='--')
                    for bar in bars:
                        height = bar.get_height()
                        plt.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}',
                                ha='center', va='bottom', fontweight='bold', fontsize=12)
                    plt.tight_layout()
                    plt.show()

            elif ch == 14:
                    result_counts = df['result'].value_counts()
                    explode = [0.05] * len(result_counts)
                    colors = plt.cm.Pastel1(np.linspace(0, 1, len(result_counts)))
                    plt.figure(figsize=(10, 10), facecolor='#f0f0f0')
                    wedges, texts, autotexts = plt.pie(result_counts.values, labels=result_counts.index, 
                                                    autopct='%1.1f%%', explode=explode, colors=colors,
                                                    startangle=90, textprops={'fontsize': 12, 'fontweight': 'bold'})
                    for autotext in autotexts:
                        autotext.set_color('black')
                        autotext.set_fontweight('bold')
                    plt.title('Match Result Distribution - Pie Chart', fontsize=14, fontweight='bold', pad=20)
                    plt.axis('equal')
                    plt.tight_layout()
                    plt.show()


            elif ch == 15:
                    player_counts = df['player_of_match'].value_counts()
                    plt.figure(figsize=(12, 7), facecolor='#f0f0f0')
                    n, bins, patches = plt.hist(player_counts.values, bins=20, edgecolor='black', 
                                                linewidth=1.5, color='#9B59B6', alpha=0.7)
                    plt.title('No. of times player became player of the match - Histogram', 
                            fontsize=14, fontweight='bold', pad=20)
                    plt.xlabel('Number of Times', fontsize=12, fontweight='bold')
                    plt.ylabel('Frequency (Number of Players)', fontsize=12, fontweight='bold')
                    plt.grid(True, axis='y', alpha=0.3, linestyle='--')
                    plt.tight_layout()
                    plt.show()

            elif ch == 16:
                clear()
                print_header("THANK YOU FOR USING IPL DATA ANALYSIS", 80)
                print()
                print_colored("Program closed successfully!", Fore.GREEN, Style.BRIGHT)
                print_colored("Made with ❤️  by Ishan Bansal & Utkarsh Jain", Fore.CYAN, Style.BRIGHT)
                print()
                break
                
            else:
                    print_error("Enter Valid choice")
                    input(f"\n{Fore.YELLOW}Press Enter to Continue...{Style.RESET_ALL}")
        except Exception as e:
            print_error(f"Error creating graph: {e}")
            input(f"\n{Fore.YELLOW}Press Enter to Continue...{Style.RESET_ALL}")
    
def main_menu():
    """Main menu function"""
    introduction()
    made_by()
    
    while True:
        clear()
        print_header("🏏 MAIN MENU 🏏", 80)
        print()
        
        main_options = [
            ("1", "📂 Read CSV File", Fore.CYAN),
            ("2", "📊 Data Analysis Menu", Fore.GREEN),
            ("3", "📈 Graph Visualization Menu", Fore.YELLOW),
            ("4", "ℹ️  About Program", Fore.BLUE),
            ("5", "🚪 Exit Program", Fore.RED),
        ]
        
        for num, item, color in main_options:
            print_colored(f"  {num}. {item}", color, Style.BRIGHT)
        
        print()
        print_separator("═", 80)
        print()
        
        try:
            a = int(input(f'{Fore.YELLOW}{Style.BRIGHT}Enter your choice (1-5): {Style.RESET_ALL}'))
        except ValueError:
            print_error("Invalid input! Please enter a number.")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
            continue

        if a == 1:
            read_csv_file()
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

        elif a == 2:
            data_analysis_menu()

        elif a == 3:
            graph()

        elif a == 4:
            clear()
            print_header("ABOUT THE PROGRAM", 80)
            print()
            about_text = f"""
    {Fore.CYAN}IPL Data Analysis Program{Style.RESET_ALL}
    
    {Fore.YELLOW}Features:{Style.RESET_ALL}
    • Comprehensive data analysis with 26+ analysis options
    • Interactive data visualization with 16 graph types
    • Advanced statistics and insights
    • Search and filter functionality
    • Team comparison and head-to-head records
    • Player statistics and performance analysis
    • Venue analysis and statistics
    • Data export capabilities
    • Beautiful color-coded interface
    
    {Fore.YELLOW}Data Source:{Style.RESET_ALL}
    • IPL Matches: 2008-2019
    • Comprehensive match statistics
    • Team, player, and venue data
    
    {Fore.YELLOW}Technologies Used:{Style.RESET_ALL}
    • Python 3
    • Pandas (Data Analysis)
    • Matplotlib (Visualization)
    • NumPy (Numerical Operations)
    
    {Fore.GREEN}Version: 2.0{Style.RESET_ALL}
    {Fore.GREEN}Last Updated: 2024{Style.RESET_ALL}
            """
            print(about_text)
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')

        elif a == 5:
            clear()
            print_header("THANK YOU FOR USING IPL DATA ANALYSIS", 80)
            print()
            print_colored("Program closed successfully!", Fore.GREEN, Style.BRIGHT)
            print()
            print_colored("Made with ❤️  by Ishan Bansal", Fore.CYAN, Style.BRIGHT)
            print()
            break
        else:
            print_error("INVALID CHOICE")
            input(f'\n{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}')
                     
        clear()

if __name__ == "__main__":
    main_menu()
