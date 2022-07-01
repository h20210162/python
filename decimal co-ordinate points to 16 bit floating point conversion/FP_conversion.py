def fp_16(num):
    if(num>=0):
        sign=0
        #print(sign)
    else:
        sign=1
        #print(sign)
    num=abs(num)
    i=20
    binary=str()
    for i in range(20):
        num*=2
        if(num>=1):
            bit=1
            num-=1
            i+=1
            binary+=str(bit)
        else:
            bit=0
            i+=1
            binary+=str(bit)

    #print(binary)
    ind=binary.index('1')
    #print(ind)
    exp=bin(-ind+14)[2:]
    exp='0'*(5-len(exp))+exp
    #print(exp)
    mant=binary[(ind+1):(ind+11)]
    #print(mant)
    floating_point=str(sign) + exp + mant
    #print(floating_point)
    return binary,mant,exp,sign,floating_point
with open('co-ordinates.txt','r', encoding="utf-8")as g:
    value=g.readlines()
    value=[x[:-1] for x in value]
    n=int(input("enter the number of co-ordinate points:"))
    a=[]
for j in range(n):
    value_x,value_y=value[j].split(",")
    a.append(float(value_x))
    a.append(float(value_y))
print(a)
fp_v=[]    
for i in range(len(a)):
    binary,mant,exp,sign,floating_point = fp_16(a[i])
    fp = str(sign) + exp + mant
    fp_v.append(fp)
    #print("Floating point half precision is :",fp)
print(fp_v)
with open('FP_result.txt','w') as h:
    for k in range(n):
        h.write(fp_v[2*k])
        h.write(fp_v[(2*k)+1])
        h.write(' ')








