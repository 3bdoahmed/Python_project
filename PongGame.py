#import turtle module
import turtle 

#inialaze the screen 
wind = turtle.Screen()
wind.title("PONG Game By AbdelRahman") #set the title of screen
wind.bgcolor("black") # set the color background of screen 
wind.setup(width=800 , height=600) # set the hight and width of screen
wind.tracer(0) # stops the windwo updates

#madrab_1
madrab1=turtle.Turtle() #to create an object from module turtle
madrab1.speed(0) # to set speed as fastest when the turtle drow the ship
madrab1.shape("square") # to chose the ship of madrab
madrab1.shapesize(stretch_wid=5 , stretch_len=1) # to stretch the width and hight 
madrab1.color("blue") # set the color of madrab1
madrab1.penup() # to stop turtle drowen the lins when the madrab move
madrab1.goto(-350,0) # set the place of madrab when it start

#madrab_2
madrab2=turtle.Turtle() #to create an object from module turtle
madrab2.speed(0) # to set speed as fastest when the turtle drow the ship
madrab2.shape("square") # to chose the ship of madrab
madrab2.shapesize(stretch_wid=5 , stretch_len=1) # to stretch the width and hight 
madrab2.color("red") # set the color of madrab2
madrab2.penup() # to stop turtle drowen the lins when the madrab move
madrab2.goto(350,0) # set the postion of madrab when it start

# ball
ball=turtle.Turtle() #to create an object from module turtle
ball.speed(0) # to set speed as fastest when the turtle drow the ship
ball.shape("square") # to chose the ship of ball
ball.color("white") # set the color of ball
ball.penup() # to stop turtle drowen the lins when the ball move
ball.goto(0,0) # set the postion of ball when it start
ball.dx= .5 # the delta of x is increase by 2.5 pixels
ball.dy= .5 # the delta of y is increase by 2.5 pixels

# score
score1 =0 
score2 =0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
# this code will write the score of evry player it will start with zero 
score.write("player_A : 0  player_B :0 ", align="center", font= ("coarier", 24, "normal"))

# functions madrab_1 up and down
def madrab1_up():
    y= madrab1.ycor() # get the Y coordinate of madrab1
    y +=20 # set the y of madrab1 to increse by 20
    madrab1.sety(y) # set the y of madrab1 to be the new y coordinate

def madrab1_down():
    y= madrab1.ycor() # get the Y coordinate of madrab1
    y -=20    # set the y of madrab1 to decrese by 20
    madrab1.sety(y) # set the y of madrab1 to be the new y coordinate

# functions madrab_1 up and down
def madrab2_up():
    y= madrab2.ycor() # get the Y coordinate of madrab2
    y +=20     # set the y of madrab2 to increse by 20
    madrab2.sety(y) # set the y of madrab2 to be the new y coordinate

def madrab2_down():
    y= madrab2.ycor() # get the Y coordinate of madrab2
    y -=20     # set the y of madrab2 to decrese by 20
    madrab2.sety(y) # set the y of madrab2 to be the new y coordinate

# keyborad bindings
wind.listen() # tell the window to expect the keyboard input
wind.onkeypress(madrab1_up,"w") # when pressing w the func madrab1_up is invoked
wind.onkeypress(madrab1_down,"s") # when pressing s the func madrab1_down is invoked
wind.onkeypress(madrab2_up,"Up")  # when pressing Up the func madrab2_up is invoked
wind.onkeypress(madrab2_down,"Down") # when pressing Down the func madrab2_down is invoked

# main GAME Loop
while True:
    wind.update() # update the window every loop start

    # move the ball
    ball.setx(ball.xcor() + ball.dx) # ball starts at 0 and everytime loop run ----->> + dx at x-axis
    ball.sety(ball.ycor() + ball.dy) # ball starts at 0 and everytime loop run ----->> + dy at y-axis

    # border check ---->> top border +300px , bottom border -300px , ball 20px
    if ball.ycor() >290: # if ball at top border
        ball.sety(290) # set y coordanate at 290
        ball.dy *= -1 # reverse the direction of ball
    if ball.ycor() < -290:  # if ball at bottom border
        ball.sety(-290)
        ball.dy *= -1

    # border check ---->> right border +400px , lift border -400px , ball 20px
    if ball.xcor() > 390: # if ball at right border 
        ball.goto(0,0) # set the ball at center of window
        ball.dx *= -1
        score1 +=1 # increase plyar A when player B lose the ball
        score.clear()  # to clear the score
        score.write("player_A : {}  player_B :{} ".format(score1,score2), align="center", font= ("coarier", 24, "normal"))
    if ball.xcor() < -390: # if ball at lift border 
        ball.goto(0,0) # set the ball at center of window
        ball.dx *= -1
        score2 +=1 # increase plyar B when player A lose the ball
        score.clear() # to clear the score
        # this code use var score1 & score2 to update the score by use .format(score1,score2)
        score.write("player_A : {}  player_B :{} ".format(score1,score2), align="center", font= ("coarier", 24, "normal"))
    
    # tasadom madrab and ball
    # if the ball collesion with and madrab it will back in reverse direction 
    if (ball.xcor() >340 and ball.xcor() <350) and (ball.ycor() < madrab2.ycor() +40 and ball.ycor() > madrab2.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < madrab1.ycor() +40 and ball.ycor() > madrab1.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1