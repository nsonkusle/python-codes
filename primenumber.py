def primenum(a):
    for num in range(0,a + 1):
      if num > 1:
        for i in range (2, num):
         if (num % i) == 0:
                break
        else:
            print(num,"is a prime number")
primenum(10)  
