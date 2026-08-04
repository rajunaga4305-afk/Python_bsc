#positive slicing
#syntax str1[start :stop-1:step]
str1="welcome to Nandyal"
print(str1)
#case 1
print(str1[0:7])

#case 2
print(str1[0:7:2])

#case 3
#print(str1[0:7:0])

#case 4
print(str1[0:7:-1])

#case 5
print(str1[::])

l1=[1,2,3,['a','b',[45,'tcs',20]]]
print(l1)
print(l1[3][2][1]) #positive indexing
print(11[-1][-1][-2]) #negative indexing

12=[24,35,67,['abc',[12,56,78,[AP]]]]