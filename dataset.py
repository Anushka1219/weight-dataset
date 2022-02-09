from collections import Counter
import csv

with open ("HeightWeight.csv",newline="")as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
weightdata=[]

for i in range(len(filedata)):
    num=filedata[i][2]
    weightdata.append(float(num))

n=len(weightdata)
total=0

for i in weightdata:
    total=total+i

mean=total/n
print(mean)

weightdata.sort()

if(n%2!=0):
    median=weightdata[n//2]
else:
    median1=weightdata[n//2]
    median2=weightdata[n//2+1]
    median=(median1+median2)/2

print(median)

