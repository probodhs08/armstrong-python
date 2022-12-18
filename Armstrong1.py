for x in range(1,1000):
    y=x
    CubeSum=0
    while x!=0:
        a=x%10
        CubeSum+=a*a*a
        x=int(x/10)
    if y==CubeSum:
        print("Armstrong")
    else:
        print("Not Armstrong")


