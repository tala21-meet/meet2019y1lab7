import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size.    
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 7
TIME_STEP = 200

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()
#Function to draw a part of the snake on the screen

def new_stamp():
    snake_pos = snake.pos() #Get snake’s position
    #Append the position tuple to pos_list
    pos_list.append(snake_pos)
    #snake.stamp() returns a stamp ID. Save it in some variable         
    ID= snake.stamp()
    #append that stamp ID to stamp_list.     
    stamp_list.append(ID)
#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for something in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE


     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE


     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()

#Draw a snake at the start of the game with a for loop
def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's position

snake.direction = "Up"
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400



def up():
    snake.direction="Up" #Change direction to up
    #move_snake() #Update the snake drawing 
    print("You pressed the up key!")
def down():
    snake.direction='Down'
    #move_snake()
    print('you pressed the down key!')
def left():
    snake.direction='Left'
    #move_snake()
    print('you pressed the left key!')
def right():
    snake.direction='Right'
    #move_snake()
    print('you pressed the right key!') 

#2. Make functions down(), left(), and right() that change snake.direction
####WRITE YOUR CODE HERE!!

turtle.onkeypress(up, "Up") # Create listener for up key
turtle.onkeypress(down, 'Down')
turtle.onkeypress(left,'Left')
turtle.onkeypress(right,'Right')
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()



#ADD THE LINES BELOW

turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don't forget to hide the food turtle!
for this_food_pos in food_pos:
    ####WRITE YOUR CODE HERE!!
    food.penup()
    food.goto(this_food_pos)
    food_id = food.stamp()
    food_stamps.append(food_id)
    food.hideturtle()
    

def move_snake():
    #Add new lines to the end of the function
    #Grab position of snake
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
     #Add this line to the end of the move_snake function
     ######## SPECIAL PLACE - Remember it for Part 5

    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
    else:
        remove_tail()
    
    #HINT: This if statement may be useful for Part 8

    
    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()
   
    


    # The next three lines check if the snake is hitting the 
    # right edge.

    #if new_x_pos >= RIGHT_EDGE:
    #     print("You hit the right edge! Game over!")
    #     quit()
    

     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE


     # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE

    
    #If snake.direction is up, then we want the snake to change


    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print('You moved down!')
    elif snake.direction=="Left":
        snake.goto(x_pos-SQUARE_SIZE,y_pos)
        print('You moved left!')
    elif snake.direction=="Right":
        snake.goto(x_pos+SQUARE_SIZE,y_pos)
        print('You moved right!')
   
    if my_pos in pos_list[:-1]:
        quit()

    #if new_x_pos >= RIGHT_EDGE:
    #     print("You hit the right edge! Game over!")


    # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE

    #4. Write the conditions for RIGHT and LEFT on your own
    ##### YOUR CODE HERE

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5

    #remove the last piece of the snake (Hint Functions are FUN!)

    # You should write code to check for the left, top, and bottom edges.
    #####WRITE YOUR CODE HERE


    # You should do the same for the up(), down(), left(), and right()  functions
    if len(food_stamps) <= 6 :
    	make_food()
    turtle.ontimer(move_snake,TIME_STEP) #<--Last line of function
    

def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position
    food.goto(food_x,food_y)
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    food_pos.append(food.pos())
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    food_stamps.append(food.stamp())

    
move_snake()  

    
    









turtle.mainloop()
