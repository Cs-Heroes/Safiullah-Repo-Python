from collections import defaultdict
lis=[1,2,3,4]
dic=defaultdict(int)
for i in lis:
    dic[i]+=i

print(dic)

