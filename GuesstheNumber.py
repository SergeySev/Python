
import simplegui
import random
import math

num_range = 100
n = 7
ran = 0

def new_game():
    global num_range
    if num_range == 1:
        range100()
    else:
        range1000()


def range100():
    global n
    global num_range
    global ran
    num_range = 1
    n = 7
    ran = random.randrange(0, 100)
    print "\nNew game. Range is from 0 to 100"
    print "Number of remaining guesses is", n



def range1000():
    global n 
    global ran
    global num_range
    num_range = 2
    n = 10
    ran = random.randrange(0, 1000)
    print "\nNew game. Range is from 0 to 1000"
    print "Number of remaining guesses is", n

    
    
def input_guess(inp):
    global n
    global ran
    player_int = int(inp)
    print "\nGuess was ", player_int
        
    if player_int < ran:
        n = n - 1
        print "Number of remaining guis is", n
        print "Higher!"
        
    if player_int > ran:
        n = n - 1
        print "Number of remaining guis is", n
        print 'Lower!'
        
    if n == 0:
        print "\nSorry, but you don't have any more attempts."
        new_game()
        
    if player_int == ran:
        n = n - 1
        print "Number of remaining guis is", n
        print 'Correct!!! YOU WIN!!!\n'
        new_game()


f = simplegui.create_frame("Guess the humber", 200, 200)

f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

range100()

