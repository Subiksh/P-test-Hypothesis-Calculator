import math
import sys


#SD with p paired test consisting of p value

x=[6.6, 6.5, 9, 10.3, 11.3, 8.1, 6.3, 11.6]
y=[6.8, 2.4, 7.4, 8.5, 8.1, 6.1, 3.4, 2]

#Amend the values of X and Y and run the program

d=[]
d_round=[]
  # using zip to get iterables of list1 and list2
zip_object=zip(x,y)
for i , ii in zip_object:
    d.append(i-ii)
for i in d:
    d_round.append(round(i, 2))
print("The value of d(x-y)is:\n", d)
print("rounded value of d is :\n", d_round)
sumof_d=sum(d)
print("The value of Σd is:\n ", sumof_d)
d_bar=sumof_d/len(x)
print("The value of d̅ :\n",d_bar)
dbar_sqr=round(d_bar**2,2)
print("The value of d̅² is :\n", dbar_sqr)

    #now for standard deviation
d_sqr,d_sqr_round=[],[]
for i in d_round:
    d_sqr.append(i**2)
for i in d_sqr:
    d_sqr_round.append(round(i,2))
sum_dsqr=sum(d_sqr_round)
round_dsqr=round(sum_dsqr,2)
print("The value of Σd² is\n", round_dsqr, "\nand d² individual list is\n", d_sqr_round)


sd=math.sqrt((round_dsqr - (float(len(x)) * dbar_sqr))/float(len(x)-1))
print("\n\n The standard deviation is : \n", sd)