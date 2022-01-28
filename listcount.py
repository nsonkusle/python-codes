a = [1,2,3,4,5,1,3,4,1,2,1,2,8,0,5,6,2,3,4,5,6,7,8,9,7,6,4,5,2,2,4,6,1,4]
def n(a):
    n=sorted(set(a))
    iter_count(n)
def iter_count(b):
    for i in b:
        print(a.count(i),"=" +str(i))
n(a)
   
