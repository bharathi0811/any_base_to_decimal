a = int(input())
b = int(input())
l=[]
for i in str(a):
    l.append(i)
sum_=0
l =l[::-1]
for j in range(len(l)):
    sum_+= int(l[j]) * (b**j)
    #print(sum_)
print(sum_)