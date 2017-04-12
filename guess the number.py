# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui





# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    
    global secret_number
    secret_number = random.randrange(0, 100)
    global chance_left
    chance_left = 7
    
    # remove this when you add your code    
    


# define event handlers for control panel
def input_handler(inp):
    global guess
    guess = float(inp)
    input_guess (guess)
    if chance_left == 0:
        print "no chance left"
        new_game()
     
    


def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randrange(0,100)
    global chance_left
    chance_left = 7
    
    
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = random.randrange(0,1000)
    global chance_left
    chance_left = 10
   
    
def input_guess(guess):
    # main game logic goes here	
    guess = float (guess)
    global chance_left
    if guess < secret_number:
        print "higher"
        chance_left -= 1
        print "chance left is:", chance_left
    elif guess > secret_number:
        print "lower"
        chance_left -= 1
        print "chance left is:", chance_left
    elif guess == secret_number:
        print "correct"
        chance_left -= 1
        print "chance left is:", chance_left
        new_game()
    else:
        print "the input is invalid"
    
    # remove this when you add your code
    


    
# create frame
frame = simplegui.create_frame("guess the number", 200, 200)
inp = frame.add_input("input", input_handler, 50)

# register event handlers for control elements and start frame
button_range100 = frame.add_button("range100",range100, 50)
button_range1000 = frame.add_button("range1000",range1000,50)


# call new_game 
new_game()




# always remember to check your completed program against the grading rubric
