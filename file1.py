#Reading Scores data

import plotly.figure_factory as pf
import csv
import pandas as pd
import statistics

file = pd.read_csv('StudentsPerformance.csv')
fileList = file['reading score'].tolist()

mean = statistics.mean(fileList)
print('Mean of this data is : ', mean)

median = statistics.median(fileList)
print('Median of this data is : ', median)

mode = statistics.mode(fileList)
print('Mode of this data is : ', mode)


sd = statistics.stdev(fileList)
print('Standard Deviation of this data is : ', sd)

firstSdStart, firstSdEnd = mean - sd, mean + sd
secondSdStart, secondSdEnd = mean - (2*sd), mean + (2*sd)
thirdSdStart, thirdSdEnd = mean - (3*sd), mean + (3*sd)

listOfFirstData = [result for result in fileList if result > firstSdStart and result < firstSdEnd]
print(format(len(listOfFirstData)*100/len(fileList)), "{}% of data lies within 1 standard deviations")

listOfSecondData = [result for result in fileList if result > secondSdStart and result < secondSdEnd]
print(format(len(listOfSecondData)*100/len(fileList)), "% of data lies within 2 standard deviations")

listOfThirdData = [result for result in fileList if result > thirdSdStart and result < thirdSdEnd]
print(format(len(listOfThirdData)*100/len(fileList)), "{}% of data lies within 3 standard deviations")