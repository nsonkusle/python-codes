def ns (n):
    sam=0
    i=1
    while i<n:
        if n%i==0:
            sam=sam+i
        i=i+1
    if n==sam:
        print(n,"is a pefect number")
    else:
        print(n,"is not perfet number")
ns(5)
