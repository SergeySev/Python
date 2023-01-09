# template for "Stopwatch: The Game"
import simplegui

# define global variables
i = 0
num_vin = 0
num_try = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    second = time / 10
    min_A = second / 60
    global sec_D
    sec_D = time % 10
    
    look_B = time / 10
    look_B = look_B % 60
    sec_B = look_B // 10
    
    sec_C = look_B % 10
    
    a = str(min_A)
    b = str(sec_B)
    c = str(sec_C)
    global d 
    d = str(sec_D)
    
    return a + ":" + b + c + "." + d


def draw(canvas):
    global num_vin, num_try, i
    canvas.draw_text(format(i),[140, 220], 48, "Red")
    canvas.draw_text(str(num_vin) + "/" + str(num_try),[300, 50], 35, "Green")
    
def time():
    global i
    format(i)
    i = i + 1
    
def start():
    timer.start()
    
def stop():
    global num_vin, num_try, sec_D
    if sec_D == 0 and timer.is_running():
        num_vin += 1
    if timer.is_running():
        num_try += 1
    timer.stop()
    
def reset():
    timer.stop()
    global num_vin, num_try, i
    num_vin = 0
    num_try = 0
    i = 0
    


# create frame
frame = simplegui.create_frame("StopWatch", 400, 400)

# define draw handler
frame.set_draw_handler(draw)

# define event handlers for buttons; "Start", "Stop", "Reset"

frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)


# define event handler for timer with 0.1 sec interval
timer = simplegui.create_timer(100, time)


# start frame
frame.start()


# Please remember to review the grading rubric
