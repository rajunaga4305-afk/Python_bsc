i=1
while i<=5:
   print("Hello")
   i=i+1

n=input("enter the string")
str2=" "
i=0
while i<len(n):
	str2=n[i]+str2
	i=i+1
print(str2)

for i in range(len(n)):
   print(n[i]) 