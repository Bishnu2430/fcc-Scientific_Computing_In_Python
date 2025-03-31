'''
# Description:
This program solves the classic Tower of Hanoi problem, a mathematical puzzle that involves moving a stack of disks from one peg to another while following specific rules. The program visually displays each step of the process.

# What It Does:

Initial Setup:
 - Uses three pegs (A, B, C).
 - The stack of disks (largest at the bottom, smallest at the top) starts on peg A.
Recursive Algorithm:
 - Moves n-1 disks from the source peg to an auxiliary peg.
 - Moves the largest remaining disk directly to the target peg.
 - Moves the n-1 disks from the auxiliary peg to the target peg.

Output:
Displays the state of all three pegs after each move.

Rules Followed:
✅ Only one disk can be moved at a time.
✅ A disk can only be placed on an empty peg or on a larger disk.
✅ The goal is to move all disks from the source peg (A) to the target peg (C).

Example Usage:
Running move(5, A, B, C) shows step-by-step moves leading to the final solution.

This program is an elegant implementation of the Tower of Hanoi, demonstrating recursion and problem-solving strategies! 🏗️🚀
'''

NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []

def move(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
        
    # move the nth disk from source to target
    target.append(source.pop())
        
    # display our progress
    print(A, B, C, '\n')
        
    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1,  auxiliary, source, target)
              
# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)