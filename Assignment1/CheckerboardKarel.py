"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *
def turn_right():
    turn_left()
    turn_left()
    turn_left()







def main():
    """
    pre-condition: karel move to the beeper place
    post-condition: karel return and put down beeper
    """
    a = 0
    put_beeper()
    while True:
        while front_is_clear():
            move()
            a += 1
            if a == 2:
                put_beeper()
                a -= 2
        if not left_is_clear():
            break
        else:
            turn_left()
            move()
            a +=1
            if a ==2:
                put_beeper()
                a -=2
            turn_left()
            while front_is_clear():
                move()
                a += 1
                if a == 2:
                    put_beeper()
                    a -= 2
            if not right_is_clear():
                break
            else:
                turn_right()
                move()
                a +=1
                if a ==2:
                    put_beeper()
                    a -=2
                turn_right()











# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
