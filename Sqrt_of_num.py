'''
#Description:
This program calculates the square root of a given non-negative number using the bisection method. It ensures precision up to a specified tolerance level and provides an approximate result even when an exact value cannot be determined within the maximum allowed iterations.

#What It Does:

Input Validation:
    - Raises an error for negative inputs, as square roots of negative numbers are undefined in real numbers.
    - Directly handles inputs of 0 and 1 by returning their square roots as 0 and 1, respectively.
Bisection Method:
    - Initializes a range [low, high] where the square root lies.
    - Iteratively narrows the range by evaluating the midpoint until the squared value of the midpoint is sufficiently close to the target number (square_target).
Precision Control:
    - The precision is governed by a tolerance value (default is 1e-7), which determines how close the calculated result is to the actual square root.
    - The program also allows for a maximum number of iterations (default is 100) to prevent infinite loops.
Output:
    - Prints the calculated square root for valid inputs.
    -Warns if the method fails to converge within the allowed iterations.

Example Usage:

Input: N = 16
Output: The square root of 16 is approximately 4.0
This program is a robust and reliable solution for computing square roots of real numbers using an iterative approach.
'''


def square_root_bisection(square_target, tolerance=1e-7, max_iterations=100):
    if square_target < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    if square_target == 1:
        root = 1
        print(f'The square root of {square_target} is 1')
    elif square_target == 0:
        root = 0
        print(f'The square root of {square_target} is 0')

    else:
        low = 0
        high = max(1, square_target)
        root = None
        
        for _ in range(max_iterations):
            mid = (low + high) / 2
            square_mid = mid**2

            if abs(square_mid - square_target) < tolerance:
                root = mid
                break

            elif square_mid < square_target:
                low = mid
            else:
                high = mid

        if root is None:
            print(f"Failed to converge within {max_iterations} iterations.")
    
        else:   
            print(f'The square root of {square_target} is approximately {root}')
    
    return root

N = 16
square_root_bisection(N)