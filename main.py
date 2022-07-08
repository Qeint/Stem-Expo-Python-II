import csv
import sys
import pandas as pd 
val = pd.read_csv('games.csv')
opname = val['opening_name']
#val is the dataset

def main():
   menu()

#Main menu
def menu():
    print("***Chess Dataset***\nMade by J.C")
    print()

    choice = input("""
                      A: See most common openings
                      B: See dataset Info
                      C: Find Average Rating
                      D: Show most effective openings
                      Q: Quit

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        op()
    elif choice == "B" or choice =="b":
        info()
    elif choice == "C" or choice =="c":
        rate()
    elif choice == "D" or choice =="d":
        ratio()
    elif choice=="Q" or choice=="q":
        sys.exit
    else:
        print("You must only select valid inputs")
        print("Please try again")
        menu()

def op():#Prints out how often an opening appears
   
   choice1 = input("\nWould you like it shown?\nA: Ascending\nB: Desending\nC: alphabetical order\nD: Reverse alphabetical order\n")
   if choice1 == "A" or choice1 =="a":
        print(opname.value_counts(ascending=True)[:20])
   elif choice1 == "B" or choice1 =="b":
     print(opname.value_counts()[:20])
   elif choice1 == "C" or choice1 =="c":
     print(opname.value_counts().sort_index(ascending=True)[:20])
   elif choice1 == "D" or choice1 =="d":
     print(opname.value_counts().sort_index(ascending=False)[:20])
    
     
    
  
    
def info(): #Prints dataset info
  print("\n\n")
  val.info()

 
def rate(): #Prints player average rating
  choice2 = input("Would you like White or Blacks mean rating?\nA: White\nB: Black\n") 
  if choice2 == "A" or choice2 =="a":
        print('\nAverage Rating of White is:',val['white_rating'].mean())
  elif choice2 == "B" or choice2=="b":  
    print('\nAverage rating of Black is:',val['black_rating'].mean())

def ratio():
#count of openings which lead to a win for black
  winning_openings_black = val['opening_name'][val['winner'] == 'black'].value_counts()

#count of openings which lead to a win for white
  winning_openings_white = val['opening_name'][val['winner'] == 'white'].value_counts()

#Collating the top 10 openings for white and black
  winning_openings_white_top10 = winning_openings_white[:10]
  winning_openings_black_top10 = winning_openings_black[:10]

#Getting the Data of the Top 10 Openings for White and Black in a separate DataFrame for each
  openingSetWhite = val[val['opening_name'].isin(winning_openings_white_top10.index)]
  openingSetBlack = val[val['opening_name'].isin(winning_openings_black_top10.index)]

#Getting the count of each opening for White in 'total_count_white'
# & Getting the count of each opening for White where White is the winner in 'total_count_white_winner'
  total_count_white = openingSetWhite.groupby('opening_name').count()
  total_count_white_winner = openingSetWhite[openingSetWhite['winner'] == 'white'].groupby('opening_name').count()

#Getting the count of each opening for Black in 'total_count_black'
# & Getting the count of each opening for Black where Black is the winner in 'total_count_black_winner'
  total_count_black = openingSetBlack.groupby('opening_name').count()
  total_count_black_winner = openingSetBlack[openingSetBlack['winner'] == 'black'].groupby('opening_name').count()

#Calculating winning percentage for the top 10 openings for Black and White each
  winning_perc_white = (total_count_white_winner/total_count_white)*100
  winning_perc_black = (total_count_black_winner/total_count_black)*100
  #Prints out the top opening based on user input
  choice3 = input("Would you like White or Blacks?\nA: White\nB: Black\n") 
  if choice3 == "A" or choice3 =="a":
        print(winning_perc_white)
  elif choice3 == "B" or choice3=="b":  
    print(winning_perc_black)







main()
#val['opening_name'].value_counts()
#print(opname.value_counts(ascending=True)[:num1]) #Prints out how many times an opening appears
#
#val.info()
#print(val.loc[8])



#ratio = val['winner']
#status = val['victory_status']



#print(val.columns)
#Add win & lost percent to each opening

#Add bar charts

#Look at top 20-50 openings

#Sources: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html https://realpython.com/pandas-python-explore-dataset/
#https://www.kaggle.com/ma7555/chess-openings-vague-analysis https://re-thought.com/pandas-value_counts/