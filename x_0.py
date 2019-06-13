#!/usr/bin/python3
import sys

global win_versions
#global steps_count 
global pl1_steps
global pl2_steps
global pl1
global pl2

steps = ["1","2","3","4","5","6","7","8","9"]
new_steps = ["1","2","3","4","5","6","7","8","9"]
board = [" _ ", " _ ", " _ ", " _ ", " _ ", " _ "," _ ", " _ ", " _ "]
win_versions = {  "1" : [1,2,3],
                "2" : [4,5,6],
                "3" : [7,8,9],
                "4" : [1,4,7],
                "5" : [2,5,8],
                "6" : [3,6,9],
                "7" : [1,5,9],
                "8" : [3,5,7]
                }
pl1_steps = [ ]
pl2_steps = [ ]
steps_count = 0

def print_board():
	 print '\n'.join(''.join(board[i:i+3]) for i in xrange(0,8,3))

def step():
#	pl = input("Player1 enter number from " +  str(new_steps) + "\n")
	steps_count += 1

def elem_existence(pl):
	while pl not in new_steps:
		repeat = raw_input("enter number from list\n")
                pl = repeat
		print (new_steps)

def update_data(pl, pl_steps, symbol):
	pl_steps.append(pl) 
        index = steps.index(str(pl))
        new_steps.remove(str(pl))
        board[index] = symbol


def check_player_won(pl_steps):
 win = 0
 for i in win_versions.values():
        for j in i:
                if j in pl_steps:
                        win += 1
                if win  == 3:
                        sys.exit("You won")
			
        win = 0
def check_nobody_won():
	if new_steps == []:
		sys.exit ("Nobody won, thanks for game")

def game():
 print_board()
 while True:
	pl1 = input("Player1 enter number from " +  str(new_steps) + "\n")
	#elem_existence(pl1)	
	update_data(pl1, pl1_steps, " x ")
	print_board()
	check_player_won(pl1_steps)
	check_nobody_won()
	pl2 = input("Player2 enter number from " +  str(new_steps) + "\n")
	#elem_existence(pl2)	
        update_data(pl2, pl2_steps, " 0 ")
	print_board()
        check_player_won(pl2_steps)

def main():
	game()

if __name__ == "__main__":
	main()
