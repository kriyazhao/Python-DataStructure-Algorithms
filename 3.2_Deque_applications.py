# ------------------------------------------------------------------------------------------------------------
# 3.2_Deque_applications.py
# Created on: 2013-04-11 13:55:52.00000
# Author: Ting Zhao
# Usage: define a function that use Deque structure. An advanced version of palinChecker() can be found in 5.1
# Description: create some functions using Deque class:
#              - palinChecker()     check if the input string is palindrome      O(n)
# ------------------------------------------------------------------------------------------------------------

from datastructure import Deque

#-----------------------------------------------------
# check Palindrome
def palinChecker(inputStr):
    palinDeque = Deque()
    for char in inputStr:
        palinDeque.addRear(char)
    while palinDeque.size() > 1:
        charRear = palinDeque.removeRear()
        charFront = palinDeque.removeFront()
        if not charRear == charFront:
            return False
    return True

print palinChecker("radar")
print palinChecker("dddsseddd")
