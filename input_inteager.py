def ramesh():
    a=input("Enter a name")
    product_stock=[70,12,16]   #1=milk,2=bread,3=cheez
    product_price=[45,15,75]    #milk=45rsltr  , bread= 15rs pack, cheez= 75rs pack
    while True:
        user_choise = int(input('Enter a choise'))-1
        if user_choise==0 or user_choise==1 or user_choise==2 or user_choise==3:
          break
        else:
            print('wrong  choise')
            continue
    while True:
         user_quantity=int(input("enter quantity"))
         if product_stock[user_choise] > user_quantity:
              break
         else:
             print('stock are not available')
    product_stock[user_choise]-=user_quantity
    print(a)
    print(product_stock)
    print("you have to pay: "+ str(product_price[user_choise]*user_quantity))
ramesh()
