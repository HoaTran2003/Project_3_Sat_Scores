# Project_3_Sat_Scores

HOA TRAN AND BACH PHAM 
CS-112
PROJECT 7.4: ADMISSIONS

PROJECT REPORT 

I.	Introduction 
- This project aims to investigate whether SAT scores (MATH & VERBAL individually and cumulatively) as well as high school GPA are good predictors of college’s GPA. With that in mind, the resulting analysis will certainly help us to have a better understanding of how admission officers  weigh their options based on academic achievements. 
II.	Algorithm explanation: 
There are four parts for in the project and the algorithm for it can be divided into four parts:
For part 1: 
+) In order to create  lists containing high school GPA, college GPA and SAT scores (each for MATH and VERBAL), we must get Python to read the data from “sat.csv”. After reading the data, we must filter the necessary information and put them into their respective lists. After that, we can plot all of the four lists in one figure using the matplotlib subplot  function.
 For part 2: 
+) To do linear regression analysis, we must compare the independent variables (being high school GPA and the two SAT scores) with the dependent variable (college GPA). 
First we must calculate the slope and intercept of the regression for each pair of independent variables with the dependent variable based on the formula given. Then, after having the required calculations, we plot the regressions required (each graph is a pair of independent variables with college GPA).  
For part 3: 
+) To see how fit the regression line is for each of the four graph, we calculate the R^2 values (there will be 4 values in accordance with four graphs). To do this, we must use the slope and intercept calculated above along with the values of the x and y variables. With all of them, we rely on the formula to calculate R^2 to return the resulting value of how well the regression line fits the data. 
For part 4: 
+) We just choose two of the four independent variables and perform a regression analysis (by creating a scatter plot with a regression line and calculating the R^2 value)

III.	Algorithm implementation: 
-	Our program has six functions: readData, plotData, linearRegression, plotRegression, rSquared and main.
-	The readData function takes fileName, a string as its parameter. The goal of this function is to create 4 subplots in one figure for high school GPA, SAT Math scores, Verbal scores and college GPA. To do this, we must first open the csv file (sat.csv) in Python and read the header lines. After that, I create four lists in accordance with four of the required values above. Then, I use a for loop to decode each split column in the csv files and remove the “,” in each iteration. Moreover, the loop also appends the appropriate values to their respective lists until the loop ends. At the end, the function should return four lists containing the independent variables. 
-	The plotData function takes the four lists in the function above as parameters. In this function, I use the subplot method in matplotlib to draw four histograms, each one for each of the independent variables. The result should be a complete figure with four separate plots. 
-	The linearRegression function takes x, being a list for each of the independent variables and y, being the list of the dependent variable. The goal of this function is to calculate the slope and intercept of the graph of  each pair of the independent variables when comparing with college GPA.  To do so, we must first initialize the required sum variables as 0  so that we could get the appropriate calculations . Then we use a for loop in the range of the length of list x (or y). For each iteration, we increment the sum variables by adding in the value in the list x and y (based on the formula to calculate each sum). After that, we create two variables called slope and intercept and calculate them based on the formula of calculation. At the end, the function should return two said variables. 
-	The plotRegression takes x, y (which is lists of the value of independent and dependent variables) as well as xLabel and yLabel (label of x and y-axis) as parameters. This function is used to plot the scatter plot for each of the independent variables with college GPA and add a regression line to each of them. 
-	The rSquared function takes x, y (which is lists of the value of independent and dependent variables) and m and b (which is the slope and intercept) as parameters. The function uses a for loop in range of the length of x (list x). In each iteration it calculates the sum of all values of y to then use that to calculate the mean of y. In another loop in range of x (list x), the values of S and T are calculated to then compute the R^2 value. 
-	The main function is where the program begins. It is used to call the 5 above functions with the appropriate parameters. In addition, the function also uses a for loop in range of the length of the list containing the length of the csv file. In each iteration, it adds the value of SAT Math and Verbal score of each student to get the full SAT scores and append that value to a list. This is used to do a linear regression of the SAT score with college GPA. 

IV. Results and findings
 
![alt text](https://github.com/HoaTran2003/Project_3_Sat_Scores/blob/main/GPA.jpg)

![](https://github.com/HoaTran2003/Project_3_Sat_Scores/blob/main/MATH.jpg)

![](https://github.com/HoaTran2003/Project_3_Sat_Scores/blob/main/VERBAL.jpg)

![](https://github.com/HoaTran2003/Project_3_Sat_Scores/blob/main/VERBAL.jpg)

From the four graphs, high school GPA, SAT scores (math and verbal individually as well as combined) are all good predictors of college GPA, especially high school GPA. The reason for this is that in all of the graphs, there seems to be  a positive correlation among the pair of independent variables and dependent variables as indicated by the upward regression line. 
Based on the graphs, high school GPA is the best predictor of college GPA because many of the data points seem to lie on the line of best fit compared to the other predictors. 

![](https://github.com/HoaTran2003/Project_3_Sat_Scores/blob/main/RES1.jpg)
 
Based on the results of the R^2 value, high school GPA is the best predictor as its value is the highest among the independent variables and is the closest to 1 (being 0.6). Moreover, combined math and verbal scores are also a solid predictor due to the R^2 being around 0.47. Followed that are SAT math and verbal score separately. 

 ![](https://github.com/HoaTran2003/Project_3_Sat_Scores/blob/main/RES2.jpg)
 ![](https://github.com/HoaTran2003/Project_3_Sat_Scores/blob/main/MATH_N.jpg)

I choose SAT math and verbal as the two independent variables to do a regression analysis. According to the graph there is a strong positive correlation between them as SAT math score increases, so does SAT verbal score. The R^2 value of this analysis also proves this as it has a very good value of around 0.7, which is very close to 1. Therefore, the regression analysis shows that the relationship between these two independent variables is strong and they are highly correlated. 

IV. Conclusion: 

In conclusion, the main goal of the project is to see the correlations between test scores, high school GPA with how well a student will be in college. With that purpose, I have a more thorough understanding of how important test scores and GPA are to the admission process of high school students. Such knowledge is immensely valuable to virtually anyone from admission officers in colleges to the general public. Therefore, by completing this project, I, as a college student, have a glimpse of how admission officers would consider the importance of academic achievements during the application process. 
