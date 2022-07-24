#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 20:09:13 2022

Author: bachpham and jasontran

Project 7.4: Admissions
"""
import matplotlib.pyplot as pyplot 

#Part 1: Getting the data
def readData(fileName): 
    """
    Reads data from fileName and returns lists of values.
    
    Parameters:
        fileName: a csv file 
    
    Return value: 4 lists containing high school GPA, SAT Math and Verbal score
    and college GPA. 
    """
    fileName = open('sat.csv','r')
    line = fileName.readline() # read the first line
    hsGPA = []         #list contains all values from hs_GPA column
    mathSAT = []       #list contains all values from mathSAT column
    crSAT = []       #list contains all values from verbSAT column
    collegeGPA = []    #list contains all values from collegeGPA column
    
    #Loop going through each row
    for line in fileName: 
        row = line.split(",")             #removing colons
        hsGPA.append(float(row[0]))
        mathSAT.append(int(row[1]))
        crSAT.append(int(row[2]))
        collegeGPA.append(float(row[3]))
    
    fileName.close()
    
    return hsGPA, mathSAT, crSAT, collegeGPA

def plotData(hsGPA, mathSAT, crSAT, collegeGPA): 
    """
    Plots collected data in one figure.
    
    Parameter:
        hsGPA:       list of high school GPAs
        mathSAT:     list of math SAT scores
        crSAT:       list of verbal SAT scores
        collegeGPA:  list of college GPAs
        
    Return value: None
    """
    pyplot.figure(1)         #use the subplot function to plot all 4 lists on the same figure
    pyplot.subplot(4, 1, 1)  #arguments are rows, columns, and subplot number

    pyplot.hist(hsGPA)
    pyplot.subplot(4, 1, 2)

    pyplot.hist(mathSAT)
    pyplot.subplot(4, 1, 3)
    pyplot.hist(crSAT)

    pyplot.subplot(4, 1, 4)
    pyplot.hist(collegeGPA)
    pyplot.show()

#Part 2:Linear Regression
def linearRegression(x, y):
    """
    Plots the linear regression line of x and y.
    
    Parameters:
        x: list of x values (independent variable)
        y: list of y values (dependent variable)
    
    Return value: slope and intercept of lineaer regression
    """
    sumx = 0          #sum of independent variables
    sumy = 0          #sum of dependent variables
    sumxy = 0         #sum of products of indepent and dependent variables
    sumxsquare = 0    #sum of squared independent variables
    
    #Loop going through the number of independent variables
    for i in range(len(x)):
        sumx = sumx + x[i] #calculate the sum of x
        sumy = sumy + y[i]
        sumxy = sumxy + x[i] * y[i]
        sumxsquare = sumxsquare + x[i]*x[i] # calculate the sum of x^2
    
    slope = (len(x)*sumxy - sumx * sumy) / (len(x) * sumxsquare - sumx * sumx) #calculate the slope
    intercept = (sumy - slope * sumx) / len(x) #calculate the intercept
    
    return slope, intercept

def plotRegression(x, y, xLabel, yLabel): 
    """
    Plots the linear regression line with x and y points.
    
    Parameter:
        x:       list of x values (independet variable)
        y:       list of y values (dependent variable)
        xLabel:  label of x axis
        yLabel:  label of y axis
            
    Return value: None
    """
    pyplot.scatter(x, y) #plot the points
    m, b = linearRegression(x, y)
    
    minX = min(x)
    maxX = max(x)
    
    pyplot.plot([minX, maxX], [m * minX + b, m * maxX + b], color = 'red')   #plot the regression line
    pyplot.xlabel(xLabel)
    pyplot.ylabel(yLabel)
    pyplot.show()

#Part 3: Measuring fit and part 4: Addtional analysis
def rSquared(x, y, m, b):
    """
    Computes coefficient of determination.
    
    Parameters:
        x: a list of x values (independent variable)
        y: a list of y values (dependent variable)
        m: slope of the linear regression
        b: y-intercept of linear regression
    Return value: coefficient of determination R^2
    """
    S = 0
    T = 0
    sumy = 0
    
    #Loop going through the number of independent variables
    for a in range(len(x)):
        sumy = sumy + y[a] #calculate the sum of all the values of y
    ymean = sumy / len(x) #calculate the mean of y
    
    #Loop going through the number of independent variables
    for c in range(len(x)):
        S = S + (y[c] - (m * x[c] + b)) ** 2 #calculate the value of S 
        T = T + (y[c] - ymean) ** 2 #calculate the value of T
    R = 1 - S / T # calculate R^2
    
    return R


    
def main():
    """
    Used to call all of the functions above and print the results of R^2 value.
    
    Parameters: None
    Return value: None
    """
    
    readData('sat.csv')
    score = readData('sat.csv') 
    plotData(score[0], score[1], score[2], score[3])
    test_results = []
    for i in range(len(score[1])): #loop iterating the length of the csv file
        test_results.append(score[1][i] + score[2][i]) #calculate the combined SAT score
    plotData(score[0], score[1], score[2], score[3])
    plotRegression(score[0], score[3] , 'High school GPA', 'College GPA')
    plotRegression(score[1], score[3], 'SAT (Math)', 'College GPA')
    plotRegression(score[2], score[3], 'SAT (Verbal)','College GPA')
    plotRegression(test_results, score[3], 'SAT score', 'College GPA')
    plotRegression(score[1],score[2],'SAT (Math)','SAT (Verbal)')
    
    HSGPA = linearRegression(score[0], score[3]) #calling the linearRegression function to get the slope and intercept
    MATH = linearRegression(score[1], score[3])
    VERBAL = linearRegression(score[2], score[3])
    COMBINED = linearRegression(test_results,score[3])
    MATH_VERBAL = linearRegression(score[1],score[2])
    
    print(rSquared(score[0], score[3], HSGPA[0], HSGPA[1])) #print the result of R^2 for each independent variable
    print(rSquared(score[1], score[3], MATH[0], MATH[1]))
    print(rSquared(score[2], score[3], VERBAL[0], VERBAL[1]))
    print(rSquared(test_results, score[3], COMBINED[0], COMBINED[1]))
    print(rSquared(score[1], score[2], MATH_VERBAL[0], MATH_VERBAL[1])) # print the R^2 of thư two independent variables.
    
main()

  
