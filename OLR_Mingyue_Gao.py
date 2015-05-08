# -*- coding: utf-8 -*-
"""
Created on Thu May 07 16:37:41 2015

@author: gaom212
"""

from bokeh.plotting import *
import numpy as np
import statsmodels.api as sm
# draw a re fdafds 
# input: a string of input file name and writelog handler
# output: two lists - x,y 
def ProcessInputData(InputDataFile,WriteLog):
    WriteLog.write('ProcessInputData() is called \n')
    x = list()
    y = list()  
    WriteLog.write('Start to process input data file: ' + InputDataFile + '\n') 
    InputData = open(InputDataFile, 'rb')
    num_line = 0 
    for EachDataRow in InputData:
        num_line += 1
        RowSplit = EachDataRow.split(',')
        try:
            x.append(float(RowSplit[1]))
            y.append(float(RowSplit[2]))
        except ValueError as e:
            WriteLog.write('erros: '+ str(e) + '\n')
    WriteLog.write('number of rows input: ' + str(num_line) + '\n')        
    InputData.close() 
    return x, y 

# draw an ordinary linear regression for two input vertors, write regression summary  
# input: two lists - x, y and writelog handler
# output: none 
def PlotRegressionGraph(x,y,WriteLog):
    WriteLog.write('\nPlotRegressionGraph() is called \n')
    X = sm.add_constant(x)
    est = sm.OLS(y,X)
    est = est.fit()
    WriteLog.write('Regresion finished! \n')
    # We need to generate actual values for the regression line.
    r_x, r_y = zip(*((i, i*est.params[1] + est.params[0]) for i in range(1948,1961)))
    WriteLog.write('Slope: ' + str(est.params[1])+ '\n')
    WriteLog.write('Intercept: ' + str(est.params[0])+ '\n')
    WriteLog.write('Regression model: y = '+str(est.params[1])+'*x ' + str(est.params[0]) + '\n')
    output_file("OrdinaryLinearRegression.html")
    plot = figure(title="Ordinary Linear Regression", x_axis_label='Time', y_axis_label='AirPassengers')
    WriteLog.write('Figure set up \n')
    plot.line(r_x, r_y, color="red",line_width=5)
    WriteLog.write('Line set up \n')
    plot.scatter(x, y, marker="square", color="blue")
    WriteLog.write('Scatter set up \n')
    show(plot) 
    WriteLog.write('Job done! Log closed! \n')
    RegressionSummary = open('Regression_Summary.txt','w')
    RegressionSummary.write(str(est.summary()))

if __name__ == "__main__":
    InputDataFile = 'AirPassengers.csv'
    ProgramLogFile = 'log.txt'
    WriteLog = open(ProgramLogFile,'w')
    
    x,y = ProcessInputData(InputDataFile,WriteLog)
    PlotRegressionGraph(x,y,WriteLog)
    
    WriteLog.close()
    
    

















