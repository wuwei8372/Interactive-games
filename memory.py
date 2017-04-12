# implementation of card game - Memory

import simplegui
import random
LIST = range(8)
list2 = range(8)
LIST.extend(list2)
random.shuffle(LIST)
exposed = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
state = 0
times = 0
set_time = "Turns = " + str(times)

# helper function to initialize globals
def new_game():
    global set_time, times, exposed
    times = 0
    random.shuffle(LIST)
    state = 0
    for i in range(len(exposed)):
        exposed[i] = False
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    which = (pos [0] // 50)
    global state,first_card,second_card,first,second, times, set_time
    
    if state == 0:
        if exposed[which] == False:
            exposed[which] = True
        state = 1
        first = which
        first_card = LIST[which]
    elif state == 1:
        if exposed[which] == False:
            exposed[which] = True
        second = which
        second_card = LIST[which]
        state = 2
        times += 1
        set_time = "Turns = " + str(times)
        print set_time
    else:
        if exposed[which] == False:
            exposed[which] = True
        if first_card != second_card:
            exposed[first] = False
            exposed[second] = False
        first = which
        first_card = LIST[which]
        state = 1
            
    

    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global set_time
    for i in range(len(LIST)):
        if exposed[i]:
            canvas.draw_text(str(LIST[i]), ((25 + 50 * i) - 12.5, 50+12.5), 25, "Red") 
        else:
            canvas.draw_line(((25 + 50 * i),0), ((25 + 50 * i),100), 50, "Green")
    label.set_text(set_time)
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")



# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
