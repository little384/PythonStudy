"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *

def turn_right():
    turn_left()
    turn_left()
    turn_left()
def karel_move():
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
    if not on_beeper():
        put_beeper()
    turn_right()
    move()
    move()
    move()
    move()
    turn_right()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
    if not on_beeper():
        put_beeper()
    turn_left()



def main():
    """
    TODO:
    """
    while front_is_clear():
        karel_move()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
