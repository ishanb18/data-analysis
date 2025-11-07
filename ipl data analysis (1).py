
#ipl data analysis program
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
csv_file='matchanalysis.csv'

def introduction():
    print("\n\n\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:-:-:-:WELCOME TO MY PROGRAM :-:-:-:-:-:-:-:-:-:-:-\t\t\t\t\t\t\t\n\n")
    print("\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:-:-:-:(IPL DATA ANALYSIS):-:-:-:-:-:-:-:-:-:-:-\t\t\t\t\t\t\t\n\n")
    msg = '''
        Cricket is one of the most popular game in INDIA. 
	The Indian Premier League (IPL) is a professional Twenty20 cricket league. 
        It is the most-attended cricket league
        In this project we will analyse the dataset of IPL matches played during (2008-2019) 
	using Python Pandas and matplotlib python module for visualization of this dataset. \n\n\n\n'''

    print(msg, end='')
    wait = input('\t\t\t\t\tPress Enter to continue.....')


def made_by():
    msg = ''' 
            IPL Data Analysis made by       : Ishan Bansal & Utkarsh Jain
            Roll No                         : 13 & 52
            School Name                     : St. Anselm's Pink City School
            session                         : 2021-22
                        
            \n\n\n
        '''


    print(msg, end='')

    wait = input('\t\t\t\tPress Enter to continue.....')


def clear():
    for x in range(5):
               print()

def read_csv_file():
    try:
        ipl=pd.read_csv(csv_file,sep=",",header=0)
        ipl.drop(ipl.columns[ipl.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        print(ipl)
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found!")
    except Exception as e:
        print(f"Error reading CSV file: {e}")

def clean_dataframe(df):
    """Helper function to clean unnamed columns from dataframe"""
    df = df.copy()
    df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    return df

def validate_year(year):
    """Helper function to validate year input"""
    return 2008 <= year <= 2019
        
def data_analysis_menu():
    # Load CSV once at the start
    try:
        ipl = pd.read_csv(csv_file, sep=",", header=0)
        df = clean_dataframe(pd.DataFrame(ipl))
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found!")
        return
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return
    
    while True:
        clear()
        print("\n\n\t\t\t\t\t\t\t________DATA ANALYSIS MENU________\t\t\t\t\t\t\t\n\n")
        print(" CHOICES ")
        print("1. WHOLE DATAFRAME\n")

        print('2. DISPLAY COLUMNS\n')
        
        print('3. DISPLAY TOP ROWS\n')
        
        print('4. DISPLAY BOTTOM ROWS\n')
        
        print('5. DISPLAY SPECIFIC COLUMN\n')
        
        print('6. ADD A NEW RECORD\n')
        
        print('7. ADD A NEW COLUMN\n')
        
        print('8. DELETE A COLUMN\n')
        
        print('9. DELETE A RECORD\n')
        
        print("10. TOTAL MATCHES IN A SEASON\n")
        
        print("11. WINNER OF THE SEASON\n")
        
        print("12. BEST PLAYER OF THE MATCH\n")

        print("13. MATCH WIN BY MAXIMUM RUNS\n")
        
        print("14. MATCHES WIN BY MINIMUM RUN IN THE SEASON\n")

        print("15. MATCH WIN BY MAXIMUM WICKETS\n")
        
        print("16. MATCHES WIN BY MINIMUM WICKET IN THE SEASON\n")
        
        print("17. NO. OF MATCHES WON BY EACH TEAM IN THE SEASON\n")
        
        print("18. NO. OF TIMES EACH TEAM WON THE TOSS\n")
        
        print("19. DATA SUMMARY\n")
        
        print("20. EXIT(To Main menu)\n")
        
        try:
            choice = int(input("Enter Choice(1-20): "))
        except ValueError:
            print("INVALID CHOICE - Please enter a number")
            wait = input('\nPress Enter to continue.....')
            continue
            
        if choice == 1:
            print("\n\nWHOLE DATAFRAME \n:")
            df = clean_dataframe(df)
            print(df)
            wait = input('\nPress Enter to continue.....')

        elif choice == 2:
            print(df.columns.tolist())
            wait = input('\n\n\n Press any key to continuee.....')

        elif choice == 3:
            try:
                num_rows = int(input('Enter Total rows you want to show :'))
                df = clean_dataframe(df)
                print(df.head(num_rows))
            except ValueError:
                print("Invalid input! Please enter a number.")
            wait = input('\n\n\n Press any key to continuee.....')
                
        elif choice == 4:
            try:
                num_rows = int(input('Enter Total rows you want to show :'))
                df = clean_dataframe(df)
                print(df.tail(num_rows))
            except ValueError:
                print("Invalid input! Please enter a number.")
            wait = input('\n\n\n Press any key to continuee.....')
                
        elif choice == 5:
            print(df.columns.tolist())
            col_name = input('Enter Column Name that You want to print : ')
            if col_name in df.columns:
                print(df[col_name])
            else:
                print(f"Column '{col_name}' not found!")
            wait = input('\n\n\n Press any key to continuee.....')
                
        elif choice == 6:
            try:
                match_id = input('Enter Match ID :')
                season = input('Enter IPL season :')
                city = input('Enter City Name :')
                date = input('Enter Match date :')
                team1 = input('Enter Team 1 Name  :')
                team2 = input('Enter Team 2 Name :')
                toss_winner = input('Enter Toss Winner :')
                toss_decision = input('Enter Toss Decision :')
                result = input('Enter Result (Normal /tie/ DL ) :')
                dl_applied = input('Enter Duckwoth Lewis Method applied (0 for No, 1 for Yes ) :) :')
                winner = input('Enter Winner Team :')
                win_by_runs = input('Enter Win By runs :')
                win_by_wickets = input('Enter Win By Wickets :')
                player_of_match = input('Enter Man of the Match Player :')
                venue = input('Enter venue : ')
                data = {'id': match_id, 'season': season, 'city': city,'date': date, 'team1': team1, 'team2': team2, 
                       'toss_winner': toss_winner,'toss_decision': toss_decision,'result': result,'dl_applied': dl_applied,
                       'winner': winner,'win_by_runs': win_by_runs,'win_by_wickets': win_by_wickets,
                       'player_of_match': player_of_match,'venue': venue}
                new_row = pd.DataFrame([data])
                df = pd.concat([df, new_row], ignore_index=True)
                df = clean_dataframe(df)
                print(df)
            except Exception as e:
                print(f"Error adding record: {e}")
            wait = input('\n\n\n Press any key to continuee.....')
                
        elif choice == 7:
            col_name = input('Enter new column name :')
            col_value = input('Enter default column value :')
            df[col_name] = col_value
            df = clean_dataframe(df)
            print(df)
            wait = input('\n\n\n Press any key to continuee.....')

        elif choice == 8:
            col_name = input('Enter column Name to delete :')
            if col_name in df.columns:
                df = df.drop(columns=[col_name])
                df = clean_dataframe(df)
                print(df)
            else:
                print(f"Column '{col_name}' not found!")
            wait = input('\n\n\n Press any key to continuee.....')

        elif choice == 9:
            try:
                index_no = int(input('Enter the Index Number that You want to delete :'))
                if 0 <= index_no < len(df):
                    df = df.drop(df.index[index_no])
                    df = clean_dataframe(df)
                    print(df)
                else:
                    print(f"Invalid index! Please enter a number between 0 and {len(df)-1}")
            except ValueError:
                print("Invalid input! Please enter a number.")
            wait = input('\n\n\n Press any key to continuee.....')
            
        elif choice == 10:
            try:
                year = int(input("Enter Year you want to see(2008 - 2019):"))
                if validate_year(year):
                    dfseason = df[df['season'] == year]
                    matches = len(dfseason)
                    print(f"Total number of matches in {year} is {matches}")
                else:
                    print("Enter year between 2008 and 2019")
            except ValueError:
                print("Invalid input! Please enter a number.")
            wait = input('\n\nPress Enter to continue.....')
            
        elif choice == 11:
            try:
                year = int(input("Enter Year you want to see(2008 - 2019):"))
                if validate_year(year):
                    dfseason = df[df['season'] == year]
                    winner_mode = dfseason['winner'].mode()
                    if len(winner_mode) > 0:
                        print(f"Winner of {year} is\n{winner_mode.iloc[0]}")
                    else:
                        print(f"No winner data found for {year}")
                else:
                    print("Enter year between 2008 and 2019")
            except ValueError:
                print("Invalid input! Please enter a number.")
            wait = input('\n\nPress Enter to continue.....')
                
        elif choice == 12:
            try:
                year = int(input("Enter Year you want to see(2008 - 2019):"))
                if validate_year(year):
                    dfseason = df[df['season'] == year]
                    player_mode = dfseason['player_of_match'].mode()
                    if len(player_mode) > 0:
                        print(f"Best player of {year} is :\n{player_mode.iloc[0]}")
                    else:
                        print(f"No player data found for {year}")
                else:
                    print("Enter year between 2008 and 2019")
            except ValueError:
                print("Invalid input! Please enter a number.")
            wait = input('\n\nPress Enter to continue.....')

        elif choice == 13:
            try:
                year = int(input("Enter Year you want to see(2008 - 2019):"))
                if validate_year(year):
                    dfseason = df[df['season'] == year].copy()
                    dfseason = clean_dataframe(dfseason)
                    # Filter matches won by runs (win_by_runs > 0)
                    runs_wins = dfseason[dfseason['win_by_runs'] > 0]
                    if len(runs_wins) > 0:
                        max_idx = runs_wins['win_by_runs'].idxmax()
                        print(dfseason.loc[max_idx])
                    else:
                        print(f"No matches won by runs found for {year}")
                else:
                    print("Enter year between 2008 and 2019")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")
            wait = input('\n\nPress Enter to continue.....')
                
        elif choice == 14:
            try:
                year = int(input("Enter Year you want to see(2008 - 2019):"))
                if validate_year(year):
                    dfseason = df[df['season'] == year].copy()
                    dfseason = clean_dataframe(dfseason)
                    # Filter matches won by runs (win_by_runs > 0)
                    runs_wins = dfseason[dfseason['win_by_runs'] > 0]
                    if len(runs_wins) > 0:
                        min_idx = runs_wins['win_by_runs'].idxmin()
                        print(dfseason.loc[min_idx])
                    else:
                        print(f"No matches won by runs found for {year}")
                else:
                    print("Enter year between 2008 and 2019")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")
            wait = input('\n\nPress Enter to continue.....')

        elif choice == 15:
            try:
                year = int(input("Enter Year you want to see(2008 - 2019):"))
                if validate_year(year):
                    dfseason = df[df['season'] == year].copy()
                    dfseason = clean_dataframe(dfseason)
                    # Filter matches won by wickets (win_by_wickets > 0)
                    wickets_wins = dfseason[dfseason['win_by_wickets'] > 0]
                    if len(wickets_wins) > 0:
                        max_idx = wickets_wins['win_by_wickets'].idxmax()
                        print(dfseason.loc[max_idx])
                    else:
                        print(f"No matches won by wickets found for {year}")
                else:
                    print("Enter year between 2008 and 2019")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")
            wait = input('\n\nPress Enter to continue.....')
            
        elif choice == 16:
            try:
                year = int(input("Enter Year you want to see(2008 - 2019):"))
                if validate_year(year):
                    dfseason = df[df['season'] == year].copy()
                    dfseason = clean_dataframe(dfseason)
                    # Filter matches won by wickets (win_by_wickets > 0)
                    wickets_wins = dfseason[dfseason['win_by_wickets'] > 0]
                    if len(wickets_wins) > 0:
                        min_idx = wickets_wins['win_by_wickets'].idxmin()
                        print(dfseason.loc[min_idx])
                    else:
                        print(f"No matches won by wickets found for {year}")
                else:
                    print("Enter year between 2008 and 2019")
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")
            wait = input('\n\nPress Enter to continue.....')
                
        elif choice == 17:
            try:
                year = int(input("Enter Year you want to see(2008 - 2019):"))
                if validate_year(year):
                    dfseason = df[df['season'] == year]
                    dfseason = clean_dataframe(dfseason)
                    print(f"No. Of Matches Win by each team in {year} are\n{dfseason['winner'].value_counts()}")
                else:
                    print("Enter year between 2008 and 2019")
            except ValueError:
                print("Invalid input! Please enter a number.")
            wait = input('\n\nPress Enter to continue.....')
                    
                
        elif choice == 18:
            try:
                year = int(input("Enter Year you want to see(2008 - 2019):"))
                if validate_year(year):
                    dfseason = df[df['season'] == year]
                    print(f"No. Of toss Win by each team in {year}\n{dfseason['toss_winner'].value_counts()}")
                else:
                    print("Enter year between 2008 and 2019")
            except ValueError:
                print("Invalid input! Please enter a number.")
            wait = input('\n\nPress Enter to continue.....')

                 
        elif choice == 19:
            print(df.describe())
            wait = input('Press Enter to continue.....')
                
        elif choice == 20:
            break
        else:
            print("INVALID CHOICE")
            wait = input('\nPress Enter to continue.....')
                
                
def graph():
    clear()
    try:
        df = pd.read_csv(csv_file)
        df = clean_dataframe(df)
    except FileNotFoundError:
        print(f"Error: File '{csv_file}' not found!")
        return
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return
        
    while True:
        clear()
        print('\n\t\t\t\tGRAPH MENU ')
        print('_'*80)
        print('\n1. Season wise Matches - Line Graph')
        print('\n2. Season wise Matches - Bar Graph')
        print('\n3. Season wise Matches - Horizontal Bar Graph')
        print('\n4. Most Successful Team - Bar Graph')
        print('\n5. Match played by each Team - Line Graph')
        print('\n6. Match played by each Team - Bar Graph')
        print('\n7. No. of matches per venue - Line Graph')
        print('\n8. No. of matches per venue - Bar Graph')
        print('\n9. No. of matches per venue - Bar Horizontal Graph')
        print('\n10. No. of toss win by each team - Line Graph')
        print('\n11. No. of toss win by each team - Bar Graph')
        print('\n12. No. of toss win by each team - Bar Horizontal Graph')
        print('\n13. No. of times which Toss decision is taken - Bar Graph')
        print('\n14. Match result - PIE CHART')
        print('\n15. no. of player became player of the match- HISTOGRAM')
        print('\n16.  Exit (Move to Main Menu)\n')
        
        try:
            ch = int(input('Enter Your Choice(1-16):'))
        except ValueError:
            print("Invalid input! Please enter a number.")
            wait = input("\n\nPress Enter to Continue......")
            continue

        try:
            if ch == 1:
                season_counts = df['season'].value_counts().sort_index()
                plt.figure(figsize=(10, 6))
                plt.plot(season_counts.index, season_counts.values, marker='o')
                plt.xlabel('Season')
                plt.ylabel('Matches')
                plt.title('Season wise Matches')
                plt.grid(True)
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()

            elif ch == 2:
                season_counts = df['season'].value_counts().sort_index()
                plt.figure(figsize=(10, 6))
                plt.bar(season_counts.index, season_counts.values)
                plt.xlabel('Season')
                plt.ylabel('Matches')
                plt.title('Season wise Matches')
                plt.grid(True, axis='y')
                plt.xticks(rotation=45)
                plt.tight_layout()
                plt.show()
            
            elif ch == 3:
                season_counts = df['season'].value_counts().sort_index()
                plt.figure(figsize=(10, 6))
                plt.barh(season_counts.index, season_counts.values)
                plt.xlabel('Matches')
                plt.ylabel('Season')
                plt.title('Season wise Matches')
                plt.grid(True, axis='x')
                plt.tight_layout()
                plt.show()
           

            elif ch == 4:
                winner_counts = df['winner'].value_counts()
                plt.figure(figsize=(10, 8))
                plt.barh(winner_counts.index, winner_counts.values)
                plt.xlabel('Matches Won')
                plt.ylabel('Teams')
                plt.title('Most Successful Team')
                plt.grid(True, axis='x')
                plt.tight_layout()
                plt.show()


            elif ch == 5:
                team1_counts = df['team1'].value_counts()
                team2_counts = df['team2'].value_counts()
                total_matches = (team1_counts + team2_counts).sort_values(ascending=False)
                plt.figure(figsize=(12, 6))
                total_matches.plot(kind='line', marker='o')
                plt.title('Match played by each team')
                plt.xlabel('Teams')
                plt.ylabel('Matches')
                plt.xticks(rotation=45)
                plt.grid(True)
                plt.tight_layout()
                plt.show()

            elif ch == 6:
                team1_counts = df['team1'].value_counts()
                team2_counts = df['team2'].value_counts()
                total_matches = (team1_counts + team2_counts).sort_values(ascending=False)
                plt.figure(figsize=(10, 8))
                total_matches.plot(kind='barh')
                plt.title('Match played by each team')
                plt.xlabel('Matches')
                plt.ylabel('Teams')
                plt.tight_layout()
                plt.show()

            elif ch == 7:
                venue_counts = df['venue'].value_counts()
                plt.figure(figsize=(12, 6))
                plt.plot(range(len(venue_counts)), venue_counts.values, marker='o')
                plt.xticks(range(len(venue_counts)), venue_counts.index, rotation=90)
                plt.xlabel('Venue')
                plt.ylabel('Matches')
                plt.title('No. of matches per venue')
                plt.grid(True)
                plt.tight_layout()
                plt.show()

            elif ch == 8:
                venue_counts = df['venue'].value_counts()
                plt.figure(figsize=(12, 6))
                plt.bar(range(len(venue_counts)), venue_counts.values)
                plt.xticks(range(len(venue_counts)), venue_counts.index, rotation=90)
                plt.xlabel('Venue')
                plt.ylabel('Matches')
                plt.title('No. of matches per venue')
                plt.grid(True, axis='y')
                plt.tight_layout()
                plt.show()

            elif ch == 9:
                venue_counts = df['venue'].value_counts()
                plt.figure(figsize=(10, max(8, len(venue_counts) * 0.3)))
                plt.barh(range(len(venue_counts)), venue_counts.values)
                plt.yticks(range(len(venue_counts)), venue_counts.index)
                plt.xlabel('Matches')
                plt.ylabel('Venue')
                plt.title('No. of matches per venue')
                plt.grid(True, axis='x')
                plt.tight_layout()
                plt.show()

            elif ch == 10:
                toss_counts = df['toss_winner'].value_counts()
                plt.figure(figsize=(12, 6))
                plt.plot(range(len(toss_counts)), toss_counts.values, marker='o')
                plt.xticks(range(len(toss_counts)), toss_counts.index, rotation=90)
                plt.xlabel('Team')
                plt.ylabel('Toss Wins')
                plt.title('No. of Toss Win by each team')
                plt.grid(True)
                plt.tight_layout()
                plt.show()

            elif ch == 11:
                toss_counts = df['toss_winner'].value_counts()
                plt.figure(figsize=(12, 6))
                plt.bar(range(len(toss_counts)), toss_counts.values)
                plt.xticks(range(len(toss_counts)), toss_counts.index, rotation=90)
                plt.xlabel('Team')
                plt.ylabel('Toss Wins')
                plt.title('No. of Toss Win by each team')
                plt.grid(True, axis='y')
                plt.tight_layout()
                plt.show()

            elif ch == 12:
                toss_counts = df['toss_winner'].value_counts()
                plt.figure(figsize=(10, max(8, len(toss_counts) * 0.3)))
                plt.barh(range(len(toss_counts)), toss_counts.values)
                plt.yticks(range(len(toss_counts)), toss_counts.index)
                plt.xlabel('Toss Wins')
                plt.ylabel('Team')
                plt.title('No. of Toss Win by each team')
                plt.grid(True, axis='x')
                plt.tight_layout()
                plt.show()

            elif ch == 13:
                decision_counts = df['toss_decision'].value_counts()
                plt.figure(figsize=(8, 6))
                plt.bar(decision_counts.index, decision_counts.values)
                plt.xlabel('Toss decision')
                plt.ylabel('Matches')
                plt.title('No. of times which toss decision is taken')
                plt.grid(True, axis='y')
                plt.tight_layout()
                plt.show()

            elif ch == 14:
                result_counts = df['result'].value_counts()
                # Create explode array dynamically
                explode = [0.1] * len(result_counts)
                colors = ['blue', 'red', 'green', 'orange', 'purple'][:len(result_counts)]
                plt.figure(figsize=(8, 8))
                plt.pie(result_counts.values, labels=result_counts.index, autopct='%.2f%%', 
                       explode=explode, colors=colors, startangle=90)
                plt.title('Match Result')
                plt.axis('equal')
                plt.tight_layout()
                plt.show()


            elif ch == 15:
                player_counts = df['player_of_match'].value_counts()
                plt.figure(figsize=(10, 6))
                plt.hist(player_counts.values, bins=20, edgecolor='black')
                plt.title('No. of times player became player of the match')
                plt.xlabel('Number of Times')
                plt.ylabel('Frequency (Number of Players)')
                plt.grid(True, axis='y')
                plt.tight_layout()
                plt.show()

                
            elif ch == 16:
                break
            else:
                print("Enter Valid choice")
                wait = input("\n\nPress Enter to Continue......")
        except Exception as e:
            print(f"Error creating graph: {e}")
            wait = input("\n\nPress Enter to Continue......")
    
def main_menu():
    introduction()
    made_by()
    while True:
        clear()
        print("\n\n\t\t\t\t\t\t\t-:-:-:-:-:-:-:-:-:-:-:MAIN MENU:-:-:-:-:-:-:-:-:-:-:-\t\t\t\t\t\t\t\n\n")
        print("ALL CHOICES ")
        print()
        print('1.  Read CSV File\n')
        print('2.  Data Analysis Menu\n')
        print('3.  Graph Menu\n')
        print('4.  Exit\n')
        try:
            a = int(input('Enter your choice(1-4) :'))
        except ValueError:
            print("Invalid input! Please enter a number.")
            wait = input('\n\n Press Enter to continue....')
            continue

        if a == 1:
            read_csv_file()
            wait = input('\n\n Press Enter to continue....')

        elif a == 2:
            data_analysis_menu()

        elif a == 3:
            graph()

        elif a == 4:
            print("PROGRAM CLOSED")
            break
        else:
            print("INVALID CHOICE")
            wait = input('\n\n Press Enter to continue....')
                     
        clear()


main_menu()
