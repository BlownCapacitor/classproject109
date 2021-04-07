import csv
from collections import Counter
import math 
import statistics

with open('StudentsPerformance.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
data.pop(1)
data.pop(2)
data.pop(3)
data.pop(4)

Performance = []

for i in range(len(data)):
    num = data[i][5]
    Performance.append(float(num))
n = len(Performance)


mean = sum(Performance)/len(Performance) 
median = statistics.median(Performance)
mode = statistics.mode(Performance)

print("mean:" ,mean)
print("median:" ,median)
print("mode:" ,mode)

standardDevaition = statistics.stdev(Performance)

print("STD:" ,standardDevaition)

firstStdStart, firstStdEnd = mean - standardDevaition, mean + standardDevaition
secondStdStart, secondStdEnd = mean - (2*standardDevaition), mean + (2*standardDevaition)
thirdStdStart, thirdStdEnd = mean - (3*standardDevaition), mean + (3*standardDevaition)

FSD = [result for result in Performance if result > firstStdStart and result < firstStdEnd]
print("{}%" .format(len(FSD)*100/len(Performance)))

SSD = [result for result in Performance if result > secondStdStart and result < secondStdEnd]
print("{}%" .format(len(SSD)*100/len(Performance)))

TSD = [result for result in Performance if result > thirdStdStart and result < thirdStdEnd]
print("{}%" .format(len(TSD)*100/len(Performance)))