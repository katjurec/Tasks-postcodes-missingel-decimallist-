# Tasks-postcodes-missingel-decimallist-
Solves 3 problems - post codes generating, generating missing list elements, decimal range list generating

##CAUTION!

Data validation was not implemented. All input data should be entered exactly in a way shown below:
1) Task1:
   First code: XX-XXX
   Second code: YY-YYY
2) Task2:
   [a,b,c,d,e], n

## First problem

This program takes two strings in the following form: 
XY-ABC
where X, Y, A, B and C are any digits from 0 to 9. 
Program prints the list of all Postcodes in between the two entered as input.

## Second problem

This program takes two parameters entered as one input in the following form:
> example
1) A list of n integer elements is given, starting with 1. 
   1-n = [1,2,3,4,5,...,10]
2) User enters an incomplete list and the total number of all list elements:
   input: [2,3,7,4,9], 10
3) Program searches for missing elements and outputs them in the form of a list:
   output: [1,5,6,8,10]

## Third problem

This program outputs list of decimal elements in range from 2.0 to 5.5 with a 0.5 step.