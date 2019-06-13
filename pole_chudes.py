#!/usr/bin/python

question = "What is short name of United States? \n"
answer = "U S A"
user_answer = "_ _ _"

name = raw_input("Hi, Enter your name and try to answer the following question: \n")
print (question)
while answer != user_answer:
  letter = raw_input("Say letter:\n")
  if len(letter) == 1:
    if letter.upper() in answer:
 	 ind = letter.upper()
	 user_answer = user_answer[:answer.index(ind)] + ind + user_answer[answer.index(ind) + 1:]
	 tmp = user_answer      
	 print (tmp)
    else:
  	print("'" + str(letter) + "' is not in answer"  ) 
  else:
	print ("You mast say one latter")
print(str(name)  + ", You won")	
