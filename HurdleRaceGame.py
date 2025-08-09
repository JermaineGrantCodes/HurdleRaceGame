# Defining a function to rotate robot when the right is clear
def rotate():
    turn_left()
    turn_left()
    turn_left()

# While loop which runs aslong as condition is true. In this case whilst the goal is not met.
while not at_goal(): # Using a nested if-statement to test if the front is clear move forward, and if the right is clear to rotate.
    if front_is_clear() == True:
        move()
        if right_is_clear() == True:
            rotate()
    elif wall_in_front() == True: # Using an elif-statement which rotates robot leftmost if facing a wall.
        turn_left()
