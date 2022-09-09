if __name__ == '__main__':
    a=input()
    a=int(a)
    b=input()
    b=int(b)
    c=int((2*a+b*3)/2)
    d=4
    for i in range(0,4,1):
        print(c)
    if c%5==0 or c%5==1 or c%5==2:
        for j in range(0,a/2,1):
            print("*",end="")
        print()
    else:
        for j in range(0,a,1):
            print("*",end="")
        print()
    if b>=6:
        for i in range(b/2):
            print("*",end="")
        print()
    else:
        for i in range(0,b,1):
            print("*",end="")
        print()

print("Dnes se citim na znamku:",d)



