import time
List_one=eval(input('enter the list data'))
R=0
X=0
while(X<len(List_one)):
	R=R+List_one[X]
	X+=1
print("the result is:",R)
print()
time.sleep(2)
print("end of an application")