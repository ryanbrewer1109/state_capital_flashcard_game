# State Capital Trivia Game
import random

# Declare global variables
count = 1
num_questions = 1
score = 0
quizzed_set = set([])
review_dict = {}

capitals_dict = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix', 'Arkansas':'Little Rock', 'California':'Sacramento', 'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover', 'Florida':'Tallahassee', 'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise', 'Illinois':'Springfield', 'Indiana':'Indianapolis', 'Iowa':'Des Moines', 'Kansas':'Topeka', 'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta', 'Maryland':'Annapolis', 'Massachusetts':'Boston', 'Michigan':'Lansing', 'Minnesota':'St. Paul', 'Mississippi':'Jackson', 'Missouri':'Jefferson City', 'Montana':'Helena', 'Nebraska':'Lincoln', 'Nevada':'Carson City', 'New Hampshire':'Concord', 'New Jersey':'Trenton', 'New Mexico':'Santa Fe', 'New York':'Albany', 'North Carolina':'Raleigh', 'North Dakota':'Bismarck', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma City', 'Oregon':'Salem', 'Pennsylvania':'Harrisburg', 'Rhode Island':'Providence', 'South Carolina':'Columbia', 'South Dakota':'Pierre', 'Tennessee':'Nashville', 'Texas':'Austin', 'Utah':'Salt Lake City', 'Vermont':'Montpelier', 'Virginia':'Richmond', 'Washington':'Olympia', 'West Virginia':'Charleston', 'Wisconsin':'Madison', 'Wyoming':'Cheyenne'}

states_list = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

def main():
  global count
  global score
  global num_questions


  print('This program will test your knowledge of U.S. state capitals.')

  while(True):
    # Validate user entry is num from 1-50
    try:
      num_questions = int(input('How many quiz questions do you want to try? Enter a number between 1-50:\n'))
      if(num_questions) > 0 and (num_questions <51):
        break;
    except:
      print('Invalid entry.')
  
  print('Great, you will be asked the capitals of ' + str(num_questions) + ' states.')
  print('For each quiz question, type the name of the capital city OR type "skip" to move on to the next question.')
  print('----------------------------------------------------')

  for item in range (num_questions):
    # select a random state to quiz; do not quiz the same state twice
    rand_state = ''

    # Select a state to quiz next
    while(True):
      rand_num= random.randint(0,49)
      # do not repeatany states already quizzed
      if(rand_num  in quizzed_set):
        continue

      # Add this to the list (set) of states quizzed so far
      quizzed_set.add(rand_num)
      # DEBUG: 
      # print('Random Number = ' + str(rand_num))

      rand_state = states_list[rand_num]    
      break
        
    # Quiz the user on the randomly-selected state
    # Simulates a do-while loop by using while(True) and break statements
    while(True):
      print('')
      print('# ' + str(count) + ':')
      user_input= input('What is the capital of '+ rand_state +'? ')
      
      # Check answer and provide feedback options.
      result_code = check_answer(rand_state,user_input)

      # If user chose 'skip': 
      if(result_code == -1):
        correct_ans = capitals_dict[rand_state]
        print('The correct answer is ' + correct_ans + '.')
        continueOrQuit = input("Press Enter to continue or 'Q' to quit. ")
        if(continueOrQuit.lower() == 'q'):
          # DEBUG:
          print('You entered: ' + continueOrQuit.lower())
          return show_results()
        else:
          if(count < num_questions):
            count +=1
          break
  
      # If user gave incorrect answer:
      elif(result_code == 0):
        continue

      # If user gave correct answer:
      else:
        remaining_questions = (num_questions - count)
        status_msg ='' 
        if(remaining_questions != 1):
          status_msg = (str(remaining_questions) + " questions remaining.")
        else:
          status_msg = (str(remaining_questions) + " question remaining.")

        print((score+1), " of", count, " correct. " + status_msg)

        continueOrQuit = input("Press Enter to continue or 'Q' to quit. ")
        if(continueOrQuit.lower() == 'q'):
          score+=1
          return show_results()
        else:
          if(count < num_questions):
            count +=1
          score +=1
          break
  # End for loop
  show_results()


def check_answer(state,capital_guess):
  global score
  # Look up correct answer (capital of state)
  correct_answer = capitals_dict[state]

  # If quz question is skipped
  if(capital_guess.lower()) == 'skip':
    review_dict.update({state:correct_answer})
    return -1


  # If answer is Incorrect
  if(capital_guess.lower() != correct_answer.lower()):
    print('Sorry! Please try again.')
    review_dict[state] = correct_answer
    return 0
  # If answer is Correct
  else:
    return 1

def show_results():
  global score
  global count
  global review_dict
  print('')  
  print('----------------------------------------------------')
  print('                   S U M M A R Y                      ')
  print('----------------------------------------------------')

  print('You correctly answered ' + str(score) + ' out of ' + str(count) + ' attempted questions. Below are the states and capitals you should review before trying this test again.')
  print(review_dict)
main()
