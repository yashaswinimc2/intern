def palprime(a,b):

    a += 1
    count = 0
    for i in range(a,b):
        y = True
        if(str(i) == str(i)[::-1]):
            if(i>2):
                for a in range(2,i):
                    if(i%a==0):
                        y = False
                        break
                if y:
                    count = count + 1
                    print(i)
    
    return count

a=int(input())
b=int(input())
print(palprime(a,b))
#print("COUNT = ")
#print(count)
