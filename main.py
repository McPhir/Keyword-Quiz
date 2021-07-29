"""CONSTANTS"""
QUIZ_FILE_NAME = "Keywords_small.txt"
QUESTION_START = "Give the key word for this description: "
CORRECT_ANSWER_REPLY = "That is correct"
INCORRECT_ANSWER_REPLY = "That is incorrect"
CORRECT_RESPONSE_START = "The correct answer is: "

def openfile():
  """opens the file and creates a list. strips off the new line character at the end ofthe lines
  """
  f = open(QUIZ_FILE_NAME)
  file_list = f.readlines()
  #mod - strip the new line characters from each line
  for i in range(len(file_list)-1):
    file_list[i] = file_list[i].strip()
  return file_list

def displayfile(file_list):
  """  prints off file , line by line
  """
  for line in file_list:
    print (line)

def do_quiz(keyterms):
  #initialize local variables
  correct = 0
  incorrect = 0
  passmark = len(keyterms)//4
  #half the length of list is the number of questions
  #half of half of the length of the list is the pass mark

  #start looping through items in the list of keyterms
  for i in range(1,len(keyterms)-1,2):
    #ask a question
    question = QUESTION_START + keyterms[i]
    #get users response
    answer = input(question).lower()
    #compare with the correct answer
    if answer == keyterms[i-1]:
      print(CORRECT_ANSWER_REPLY)
      correct += 1
    else:
      print(INCORRECT_ANSWER_REPLY)
      print(CORRECT_RESPONSE_START + keyterms[i-1])
      incorrect += 1
    #loop back to get next question

  #report back.
  print('--------------------------------')
  print(f'You answered {correct} questions correctly')
  print(f'The pass mark is {passmark}.')
  if correct >= passmark:
    print('Congratulations. You passed the test')
  else:
    print('Sorry. Unfortunately you have not passed the test. Please try again after some more study')


file_list = openfile()

print("What do you want to do.")
option = int(input("Enter 1 to display keywords and descriptions, 2 to take the quiz, 0 to quit\n"))
while option != 0:
  if option == 1:
    #disply the file
    displayfile(file_list)
  elif option == 2:
    do_quiz(file_list)
  elif option != 0:
    print('invalid option')
  print('')
  print("Do you want to play again.")
  option = int(input("Enter 1 to display keywords and descriptions, 2 to take the quiz, 0 to quit\n"))