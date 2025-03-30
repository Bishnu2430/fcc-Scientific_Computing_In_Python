# :snake: Scientific Computing with Python - FreeCodeCamp

## About the Projects

This repository contains all my solutions to the Scientific Computing with Python course from FreeCodeCamp. All were made using only Python

## Project list:

- [Arithmetic Formatter](#arithmetic-formatter)
- [Time Calculator](#time-calculator)
- [Budget App](#budget-app)
- [Polygon Area Calculator](#Polygon-Area-Calculator)
- [Probability Calculator](#probability-calculator)

## Arithmetic Formatter

This project consisted in creating a function that receives a sum or a substraction and arrenges it vertically. The function receives as a parameter the problems to arrenge and also can receive an optional parameter ( True or False) in case the user wants the results to be shown. 

### Example 

Input: 

`arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])`

Output: 

```
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

See all the requirements at [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter)

You can try my code at [Replit](https://replit.com/@PabloPerez26/boilerplate-arithmetic-formatter#arithmetic_arranger.py)

## Time Calculator

This project consisted in creating a function receives as parameters a starting time and a duration time. It will return the starting time with the duration time added 

### Example 

Input: 

`add_time("11:43 PM", "24:20", "tueSday")`

Output: 

` # Returns: 12:03 AM, Thursday (2 days later) `

See all the requirements at [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator)

You can try my code at [Replit](https://replit.com/@PabloPerez26/time-calculator#main.py)

## Budget App

This project consisted in creating a class called Budget. It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category. The class should have an instance variable called ledger that is a list. The class should also contain differents methods that will alter the budget. 

When the object is printed gives the following output:

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

There is also a function called "create_spend_chart" that creates a chart showing spending from a list of categories that receives as parameters. Here is an example of the output:

```
Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g 
```

See all the requirements at [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app)

You can try my code at [Replit](https://replit.com/@PabloPerez26/budget-app)


## Polygon Area Calculator

This project consisted in creating a class called rectangle and a subclass of rectangle called square that inhereted methods and attributes. The Rectangle class includes methods to calculate area, perimeter, diagonal, print a picture and see how many times other shapes can fit inside. 


See all the requirements at [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator)

You can try my code at [Replit](https://replit.com/@PabloPerez26/polygon-area-calculator)

## Probability Calculator

For this project, I needed to write a program to determine the approximate probability of drawing certain balls randomly from a hat. I created a Hat class that the user, when creating a instance of the class, can decide how many balls are in the hat  and of which colors they are. Then there is a function to calculate the probability of picking a group of balls from an instance of the hat class


See all the requirements at [FreeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/probability-calculator)

You can try my code at [Replit](https://replit.com/@PabloPerez26/boilerplate-probability-calculator)




