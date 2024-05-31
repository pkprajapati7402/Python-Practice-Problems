#letter with maximum count using hashing TC:O(n)
str=input("enter")
dic={}
for i in str:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic.items())
maxi=0
for i,j in dic.items():
    if maxi<j:
        maxi=j
        ans=i
print(ans)