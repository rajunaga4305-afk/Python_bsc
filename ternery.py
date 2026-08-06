a,b=10,20 
x=30 if a<b else 40 
print(x) 

a=int(input("Enter First Number:")) 
b=int(input("Enter Second Number:")) 
min=a if a<b else b 
print("Minimum Value:",min)

#minimum of 3 Numbers
a=int(input("Enter First Number:")) 
b=int(input("Enter Second Number:")) 
c=int(input("Enter Third Number:")) 
min=a if a<b and a<c else b if b<c else c 
print("Minimum Value:",min)

#maximum of 3 Numbers
a=int(input("Enter First Number:")) 
b=int(input("Enter Second Number:")) 
c=int(input("Enter Third Number:")) 
max=a if a>b and a>c else b if b>c else c 
print("Maximum Value:",max)
