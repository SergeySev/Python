# implementation of card game - Memory

import simplegui
import random

cards = list(range(0, 8))
deck_of_cards_2 = list(range(0, 8))
cards = cards + deck_of_cards_2
random.shuffle(cards)

exposed = [False]
exposed = exposed * 16

draw_point1 = list(range(0, 800, 50))
draw_point2 = list(range(48, 850, 50))

state = 0
first_click = 0
second_click = 0

num = 0
turns = "Turns = " + str(num)

# helper function to initialize globals
def new_game():
    global state, exposed, num
    state = 0
    num = 0
    exposed = [False]
    exposed = exposed * 16
    random.shuffle(cards)
    label.set_text("Turns = " + str(num))
     
        
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, first_click, second_click, num, turns
    global cards
    click = (pos[0] // 50)
    if state == 0:
        state = 1
        first_click = click
        exposed[first_click] = True
        
    elif state == 1:
        if not exposed[click]:
            state = 2
            second_click = click
            exposed[second_click] = True
            num += 1
            label.set_text("Turns = " + str(num))
            
    elif state == 2:
        if not exposed[click]:
            if cards[first_click] != cards[second_click]:
                exposed[first_click] = False
                exposed[second_click] = False
            first_click = click
            exposed[first_click] = True
            state = 1       
    
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    for card_index in range(len(cards)):
        card_pos = 50 * card_index
        canvas.draw_text(str(cards[card_index]), (card_pos, 80), 90, "White")
        
    for i in range(len(cards)):
        if exposed[i] == False:
            canvas.draw_line((draw_point1[i], 100), (draw_point2[i], 100), 200, 'Green')


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
