import turtle
import time
import random
import math 

# This variable represents the x position
# of the player's paddle. Initially, it
# will be 0 (i.e. in the center). The y
# position of the paddles never changes,
# so we don't need a variable for it.
user1x = 0

# This variable represents the x position
# of the computer's paddle. Initially, it
# will be 0 (i.e. in the center)
user2x = 0

# These variables store the current x and y
# position of the ball. Their values will be
# updates on each frame, as the ball moves.
ballx = 0
bally = 0

# These variables store the current x and y
# velocity of the ball. Their values will be
# updates on each frame, as the ball moves.
ballvx = 0
ballvy = 0

# These variables store the current score 
# of the game.
user1points = 0
user2points = 0

turtle.bgcolor("black")

def draw_ball(x3, y3):
    turtle.color("green")
    turtle.penup()
    turtle.goto(x3, y3)
    turtle.pendown()
    turtle.circle(10)
   
def draw_paddle_1(x5):
    turtle.color("orange")
    turtle.penup()
    turtle.goto(user1x, -300)
    turtle.pendown()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(50)   
    
def draw_paddle_2(x6):
    turtle.color("orange")
    turtle.penup()
    turtle.goto(user2x, 300)
    turtle.pendown()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(50)
        
def score_board():
    global user1points, user2points
    
    turtle.color("purple")
    turtle.penup()
    x=250
    y=300
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write("Player Score: " + str(user1points))

    turtle.penup()
    x=-300
    y=300
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write("Computer Score: " + str(user2points))


def frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the paddles,
    the ball, and the current score.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    Hint: write this function first!
    """
    global ballx, bally, user1x, user2x
    
    draw_ball(ballx, bally)
    draw_paddle_1(user1x)
    draw_paddle_2(user2x)
    score_board()
    turtle.update()
  

def key_left():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the user's paddle
    appropriately by modifying the variable
    user1x.
    """
    global user1x
    
    if -310 < user1x:
        i = 0
        while i < 10:
            user1x += -1
            i += 1


def key_right():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the user's paddle
    appropriately by modifying the variable
    user1x.
    """
    global user1x
    
    if user1x < 310:
        i = 0
        while i < 10:
            user1x += 1
            i += 1


def reset():
    """
    signature: () -> NoneType
    Reset the global variables representing
    the position and velocity of the ball and
    the position of the paddles to their initial
    state, effectively restarting the game. The
    initial velocity of the ball should be random
    (but there there must be nonzero vertical
    velocity), but the speed of the ball should
    be the same in every game.
    """
    global user1x, user2x
    global ballvx, ballvy
    global ballx, bally
    
    user1x = 0
    user2x = 0
    ballx = 0
    bally = 0
    if user1points < 3:
        speed = 9
    if 3 <= user1points <= 6:
        speed = 10
    if user1points > 6:
        speed = 12
    ballvy = random.randint(1, 7)*random.choice([-1, 1])
    ballvx = math.sqrt(abs(speed**2 - ballvy**2))*random.choice([-1, 1])
    
         
def ai():
    """
    signature: () -> NoneType
    Perform the 'artificial intelligence' of
    the game, by moving the computer's paddle
    to an appropriate location by updating
    the user2x variable. The computer
    paddle should move towards the ball in an
    attempt to get under it.
    """
    global user2x
    
    if user1points < 3:
        if user2x < ballx:
            i = 0
            while i < 6:
                user2x += 1
                i += 1
        if user2x > ballx:
            i = 0
            while i < 6:
                user2x += -1
                i += 1               
    if 3 <= user1points <= 6:
        if user2x < ballx:
            i = 0
            while i < 8:
                user2x += 1
                i += 1
        if user2x > ballx:
            i = 0
            while i < 8:
                user2x += -1
                i += 1
    if user1points > 6:
        if user2x < ballx:
            i = 0
            while i < 10:
                user2x += 1
                i += 1
        if user2x > ballx:
            i = 0
            while i < 10:
                user2x += -1
                i += 1
        

def physics():
    """
    signature: () -> NoneType
    This function handles the physics of the game
    by updating the position and velocity of the
    ball depending on its current location. This
    function should detect if the ball has collided
    with a paddle or a wall, and if so, adjust the
    direction of the ball (as stored in the ballvx
    and ballvy variables) appropriately. If the ball
    has not collided with anything, the position of the
    ball should be updated according to its current
    velocity.
    This function should also detect if one of
    the two players has missed the ball. If so, it
    should award a point to the other player, and
    then call the reset() function to start a new
    round.
    """
    global ballx, bally
    global ballvx, ballvy
    global user1points, user2points
   
    ballx += ballvx
    bally += ballvy

    d1 = ballx - user1x
    d2 = ballx - user2x
    speed = math.sqrt((ballvx)**2+(ballvy)**2)
  
    if bally <= (-300) and 0 < d1 <= 50:
        angle1 = math.radians((7/5)*d1)
        ballvx = speed * math.sin(angle1)
        ballvy = speed * math.cos(angle1)
    if bally <= (-300) and -50 <= d1 < 0:
        angle1 = math.radians((7/5)*d1)
        ballvx = speed * math.sin(angle1)
        ballvy = speed * math.cos(angle1)
    if bally <= (-300) and ballx == user1x:
        ballvy = speed
        ballvx = 0 
        
    if bally >= (260) and 0 < d2 <= 50:
        angle2 = math.radians((7/5)*d2)
        ballvx = speed * math.sin(angle2)
        ballvy = -speed * math.cos(angle2)
    if bally >= (260) and -50 <= d2 < 0:
        angle2 = math.radians((7/5)*d2)
        ballvx = speed * math.sin(angle2)
        ballvy = -speed * math.cos(angle2)
    if 255 <= bally <= (265) and d2 == 0:
        ballvy = -speed
        ballvx = 0 

    if ballx >= 355:
        ballvx = -ballvx 
    if ballx <= -355:
        ballvx = -ballvx

    if bally >= 337:
        user1points = user1points + 1
        reset()
    if bally <= -337:
        user2points = user2points + 1
        reset()


def main():
    #signature: () -> NoneType
    #Run the pong game. You shouldn't need to
    #modify this function.
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.listen()
    reset()
    while True:
        turtle.clear()
        physics()
        ai()
        frame()
        turtle.update()
        time.sleep(0.05)

main()



