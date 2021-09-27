price=0
print( "Online Computer Parts Store \n")
print ("****************** \n")
#Products
print ("1.Keyboard   Price : 900 Pesos")
print ("2.Mouse      Price : 400 Pesos")
print ("3.Monitor    Price : 12000 Pesos")
print ("4.Camera     Price : 500 Pesos")
print ("5.Headset    Price : 1000 Pesos")
choice=int(input("Enter the designated number or name of the device :"))
if choice ==1:
    price= price + 900
elif choice ==2:
    price= price + 400
elif choice ==3:
    price= price + 12000
elif choice ==4:
    price=price + 500
elif choice ==5:
    price=(price + 1000)
print("The price would be ",price)