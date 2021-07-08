"""CONSTANTS"""
QUIZ_FILE_NAME = "Keywords.txt"

def openfile():
  f = open(QUIZ_FILE_NAME)
  file_list = f.readlines()
  #mod - strip the new line characters from each line
  for i in range(len(file_list)-1):
    file_list[i] = file_list[i].strip()
  return file_list

def printfile(file_list):
  for line in file_list:
    print (line)

file_list = openfile()
printfile(file_list)