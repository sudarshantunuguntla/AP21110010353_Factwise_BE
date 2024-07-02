n=int(input())
l=[]
while n>0:
    l.append(n%10)
    n=n//10
l=l[::-1]
# print(l)
dict1={1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,0:4} # 0-9
dict2={1:3,2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6} #tys
dict3={1:6,2:6,3:8,4:8,5:7,6:7,7:9,8:8,9:9}
if len(l)==1:
    print("Number of letters : ",dict1[l[0]])
elif len(l)==2:
    
    if l[1]==0 and l[0]!=1:
        print("Number of letters : ",dict2[l[0]])
    elif l[0]!=1:
        print("Number of letters : ",dict2[l[0]]+dict1[l[1]])
    else:
        if l[0]==1 and l[1]==0:
            print("Number of letters : ",3)
        elif l[0]==1:
            print("Number of letters : ",dict3[l[1]])
elif len(l)==3:
    if l[1]==0 and l[2]==0:
        print("Number of letters : ",dict1[l[0]]+7)  # 100 - one hundred
    elif l[1]==1 and l[2]==0:
        print("Number of letters : ",dict1[l[0]]+7+3+3) ## 210,110,310
    elif l[1]==1 and l[2]!=0:
        print("Number of letters : ",dict1[l[0]]+7+3+dict3[l[2]]) ## 213 315 112 teens
    elif l[2]==0 and l[1]!=1 and l[1]!=0:
        print("Number of letters : ",dict1[l[0]]+7+3+dict2[l[1]])
    else:
        print("Number of letters : ",dict1[l[0]]+7+3+dict2[l[1]]+dict1[l[2]])
elif len(l)==4:
    print("Number of letters : ",11) # one thousand
