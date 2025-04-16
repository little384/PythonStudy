"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *

def pick_newspaper():
    move()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
    pick_beeper()
def karel_return():
    turn_left()
    turn_left()
    move()
    move()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    put_beeper()
def main():
    """
    TODO:
    """
    pick_newspaper()
    karel_return()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
