num=0
count=0
xStr=input()
while xStr!='':
    x=eval(xStr)
    num+=x
    count+=1
    xStr=input()
a=num/count
print('平均数为：{:.2f}'.format(a))
