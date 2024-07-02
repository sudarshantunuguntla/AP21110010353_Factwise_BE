print("Enter the list of numbers : ")
n=list(map(int,input().split()))
print("enter the number of cards to be taken : ")
k=int(input())
sum1=0
while k>0:
    if n[0]>n[-1]:
        sum1=sum1+n[0]
        n=n[1::]
    elif n[-1]>n[0]:
        sum1=sum1+n[-1]
        n.pop()
    elif n[0]==n[-1] and len(n)>=3:
        if n[1]>n[-2]:
            sum1=sum1+n[0]
            n=n[1::]
        else:
            sum1=sum1+n[-1]
            n.pop()
    elif n[0]==n[-1] and len(n)<3:
        sum1=sum1+n[0]
        n=n[1::]
    k=k-1
print("answer : ",sum1)