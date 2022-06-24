string="I am AkiraChix"
x=string.split()
start=0
last=len(x)-1
while start<last:
    x[start],x[last]=x[last],x[start]
    start+=1
    last-=1
    strings=" "
    print(strings.join(x))





