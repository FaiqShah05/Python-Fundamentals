items = ["Burger","Pizza","Pasta","Drinks","Salad"]
prices = [200,400,150,60,20]

print("======MENU=======")
total_price = 0
item_total = 0
for i in range(len(items)):
    print(i+1,items[i],"\tRs.",prices[i])


while True:
        user = int(input("Enter from 1 to 5 for order or enter 0 to exit : "))

        if user == 0:
            break
            print("Exiting.....")
        
        if user == 1:
            print("Burger")

            quantity = int(input("Enter the quantity of :" ))
            item_total = quantity * 200
            total_price += item_total

        elif user == 2:
            print("Pizza")
            quantity = int(input("Enter the quantity: "))
            item_total = quantity *400
            total_price += item_total

        elif user == 3:
            print("Pasta")
            quantity = int(input("Enter the quantity: "))
            item_total = quantity * 150
            total_price += item_total        


        elif user == 4:
            print("Drinks") 
            quantity = int(input("Enter the quantity: "))
            item_total = quantity * 60
            total_price += item_total 

        elif user == 5:
            print("Salad")    
            quantity = int(input("Enter the quantity: "))
            item_total = quantity * 20
            total_price += item_total 

        else:
            print("Invalid...")  
if total_price < 200:
    discount = 0
elif 200 <= total_price < 500:
    discount = total_price * 0.05
elif 500 <= total_price < 1000:
    discount = total_price * 0.10
else:
    discount = total_price * 0.15

discounted_price = total_price - discount

print("Discount applied:", discount)
print("Price after discount:", discounted_price)

        
     
     





print("Total price is: ",total_price)

