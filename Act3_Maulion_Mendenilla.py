price=0
print( "Online Computer Parts Store \n")
print ("****************** \n")
#Products
print ("1.Keyboard   Price : 900 Pesos")
print ("2.Mouse      Price : 400 Pesos")
print ("3.Monitor    Price : 12000 Pesos")
print ("4.Camera     Price : 500 Pesos")
print ("5.Headset    Price : 1000 Pesos")

#maulion_mendenilla
print ("------------------------------- ")
print ("Type 0 "+"("+"Zero"+")"+" if you're done.")
print ("------------------------------- \n")



while True:
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
        elif choice == 0:
            print("")
            print("The price would be ",price)
            print("")

            if price <= 18000:
                print("You don't have disocunt!")
                print("")
                break
            elif price >= 18000 & price < 25000:
                disc = price * 0.3
                tot = price - disc
                print("Congrats! You got 30% Discount!")
                print("Your total price is {}, and your discount is {}. ".format(tot, disc))
                print("")
                break