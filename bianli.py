s=input()
t=''
if s!='':
    for i in s:
        if ord(i)>=ord('z'):
            t=t+''
            break
        else:
           i=chr(ord(i)+1)
           t=t+i
if len(t)==len(s):
    print('{}哈哈，成功遍历！'.format(t))
elif len(t)!=0 and len(s)>len(t):
    print(t)
else:
    print('')
