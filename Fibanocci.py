num = int(input("please enter the number upto you want series: "))

n1=0
n2=1
for i in range(num):
    print(n1)
    nth =n1+n2
    n2=n1
    n1 =nth