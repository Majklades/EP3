if __name__=="__main__":
    a=input()
    b=input()
    a=int(a)
    b=int(b)
    c=(a*b)
    for i in range(0,4,1):
        print(a*b)
    if a>=5:
        p=int(a/2)
    else:
        p=a
    if b<5:
        o=int(b/4)
    else:
        o=int(b)
    for i in range(0,p,1):
        for j in range(0,o,1):
            if c%2==0:
                print("*",end="")
            else:
                print("/",end="")
        print()


