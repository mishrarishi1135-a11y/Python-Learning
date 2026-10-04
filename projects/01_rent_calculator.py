## Inputs we need from the user
# Total rent
# Total food order for snacking
# total electricity units speed
# charge per unit
# total no of persons living in room/flat

# output - total amount you have to pay is.

rent = int(input("Enter your flat/hostel rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity = int(input('Enter total amount of electricity spend = '))
Charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity * Charge_per_unit

output = (food + rent + total_bill) // persons
print("each person will pay = ", output)
