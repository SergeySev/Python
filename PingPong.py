# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
BALL_POS = [WIDTH/2, HEIGHT/2]
PAD_WIDTH = 8
PAD_HEIGHT = 80
LEFT = False
RIGHT = True

paddle1_pos = [5, 140]
half_paddle1_pos = [5, 140 + 120]

paddle2_pos = [595, 260]
half_paddle2_pos = [595, 260-120]

score1, score2 = 0, 0

paddle1_vel = 0
paddle2_vel = 0

time = 0

# initialize ball_pos and ball_vel for new bal in middle of table
def spawn_ball(direction):
    global BALL_POS, ball_vel # these are vectors stored as lists
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 140)/ 60.0, - random.randrange(60, 180) / 60.0]
    elif direction == LEFT:
        ball_vel = [-random.randrange(120, 140) / 60.0, -random.randrange(60, 180) / 60.0]
    BALL_POS = [WIDTH/2, HEIGHT/2]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_start = random.randint(1, 2)
    if spawn_start == 1: 
        spawn_ball(RIGHT)
    else:
        spawn_ball(LEFT)
    score1, score2 = 0, 0

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, BALL_POS
    global paddle1_vel, paddle2_vel, half_paddle1_pos, half_paddle2_pos
    BALL_POS[0] += ball_vel[0]
    BALL_POS[1] += ball_vel[1]
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "Green")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "Red")
        
    # bouncing off boundaries
    if BALL_POS[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif BALL_POS[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] = - ball_vel[1]
        
    #SCORE POINT    
    elif BALL_POS[0] + BALL_RADIUS > WIDTH - PAD_WIDTH:
        if half_paddle2_pos[1] < BALL_POS[1] < paddle2_pos[1]:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] = ball_vel[0] + (ball_vel[0] / 10)
            ball_vel[1] = ball_vel[1] + (ball_vel[1] / 10)
        else:
            score1 += 1
            spawn_ball(LEFT)

    elif BALL_POS[0] - BALL_RADIUS < PAD_WIDTH:
        if paddle1_pos[1] < BALL_POS[1] < half_paddle1_pos[1]:
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] = ball_vel[0] + (ball_vel[0] / 10)
            ball_vel[1] = ball_vel[1] + (ball_vel[1] / 10)
        else:
            score2 += 1
            spawn_ball(RIGHT)

    # draw ball
    canvas.draw_circle(BALL_POS, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    timer.start()
    if paddle1_pos[1] + paddle1_vel < 0 or paddle1_pos[1] + paddle1_vel > HEIGHT - 120:
        paddle1_pos[1] = paddle1_pos[1]
        half_paddle1_pos[1] = half_paddle1_pos[1]
    else:
        paddle1_pos[1] += paddle1_vel
        half_paddle1_pos[1] += paddle1_vel

    if paddle2_pos[1] + paddle2_vel > HEIGHT or paddle2_pos[1] + paddle2_vel < 120:
        paddle2_pos[1] = paddle2_pos[1]
        half_paddle2_pos[1] = half_paddle2_pos[1]
    else:
        paddle2_pos[1] += paddle2_vel
        half_paddle2_pos[1] += paddle2_vel
    
    # draw paddles   
    canvas.draw_line(paddle1_pos, half_paddle1_pos, PAD_WIDTH, 'Green') #PADD
    canvas.draw_line(paddle2_pos, half_paddle2_pos, PAD_WIDTH, 'Red') #PADD 
    
    # draw scores
    canvas.draw_text(str(score1), [150, 100], 48, "Green")
    canvas.draw_text(str(score2), [450, 100], 48, "Red")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    velocity = 5
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel += velocity
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= velocity
    elif key==simplegui.KEY_MAP["s"]:
            paddle1_vel += velocity
    elif key==simplegui.KEY_MAP["w"]:
        if paddle1_pos[1] >= 15:
            paddle1_vel -= velocity
   

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
       
    
def timer():
    global time
    time += 1

    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(10, timer)
frame.add_button("Restart", new_game, 200)

# start frame
new_game()
frame.start()
timer.start()
