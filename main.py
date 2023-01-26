import datetime # import a datetime to showing date

name = input("Write the company name: ") # input a name of company
nameUp= name.upper() # changing variable to Upper Case
address1 = input("Write a first line of address: ") # input address1
address2 = input("Write a second line of address: ") # input address2
address3 = input("Write a third line of address: ") # input address3
phoneNumber = int(input("Write a number: ")) # input a phone number
phoneNumberStr= str(phoneNumber) # converting integer to string
todayDate = datetime.datetime.today().strftime('%d-%m-%y')  # format of date

ButchersPaleAle = int(input("Write number of barrels Butchers` Pale Ale: ")) # input num of barrels for first company
FarriersIPA = int(input("Write number of barrels Farriers` IPA: ")) # input num of barrels for second company
GatehouseBrownAle = int(input("Write number of barrels Gatehouse Brown Ale: ")) # input num of barrels for third company

totalOrder = (ButchersPaleAle+FarriersIPA+GatehouseBrownAle) # calculating a total amount of barrels


# calculating cost of delivery

# calculating how many free space left
if (totalOrder % 15) == 0:
    left = 0
else:
    left = 15-(totalOrder % 15)

# calculating a cost for ButchersPaleAle
discountBPA = int(ButchersPaleAle // 10)
discountBPACost = discountBPA*10
costBPA = (ButchersPaleAle * 125.5)
costBPADisc = costBPA - discountBPACost


# calculating a cost for FarriersIPA
discountFIPA = int(FarriersIPA // 12)
discountFIPACost = discountFIPA*8.4
costFIPA =(FarriersIPA * 105.9)
costFIPADisc = costFIPA - discountFIPACost


# calculating a cost for GatehouseBrownAle
discountGBA = int(GatehouseBrownAle // 9)
discountGBACost = discountGBA*11.65
costGBA = (GatehouseBrownAle * 132.35)
costGBADisc = costGBA - discountGBACost

totalCost = costGBA + costFIPA + costBPA # calculating total cost without discount
totalCostDisc = costGBADisc + costBPADisc + costFIPADisc # calculating total cost with discount
total= totalCostDisc+(left*2) # calculating a total cost of delivery


print('{:>50}'.format("Walled Town ALe")) # output main name
print('{:>75}'.format("Invoice No: WTA" + phoneNumberStr[0:2]+phoneNumberStr[-2:]+nameUp[-2])) # output and creating a WTA number
print('{:>60}'.format("Date:"), '{:>14}'.format(todayDate)) # output a Current Date
print("\nCompany Name:", name) # output a customer company name
print("Address:", "\t  ", address1, "\n\t\t\t  " , address2, "\n\t\t\t  ", address3) # output address

# output Sales Details
print("\nSales Details:\n\nButchers’ Pale Ale:", '{:>19}'.format(ButchersPaleAle), '{:>28}'.format(""), '€{:,.2f}'.format(costBPA))
print("Farriers’ IPA:",'{:>24}'.format(FarriersIPA), '{:>28}'.format(""), '€{:,.2f}'.format(costFIPA))
print("Gatehouse Brown Ale:", '{:>18}'.format(GatehouseBrownAle), '{:>28}'.format(""), '€{:,.2f}'.format(costGBA))
print("\n", '{:>45}'.format("Subtotal:"), '{:>21}'.format(""), '€{:,.2f}'.format(totalCost))

# output a surcharge
if left > 0:
    print("\nSurcharge:")
    print("Rack spaces unused:", '{:>19}'.format(left),'{:>28}'.format(""), '€{:,.2f}'.format(left*2))


# output a discounts
if discountBPA or discountFIPA or discountGBA > 0:
    print("\nDiscount:")


if discountBPA > 0:
    print("Butchers’ Pale Ale:", '{:>19}'.format(discountBPA), '{:>28}'.format(""), '€{:,.2f}'.format(discountBPACost))
if discountFIPA > 0:
    print("Farriers’ IPA:", '{:>24}'.format(discountFIPA), '{:>28}'.format(""), '€{:,.2f}'.format(discountFIPACost))
if discountGBA > 0:
    print("Gatehouse Brown Ale:", '{:>18}'.format(discountGBA), '{:>28}'.format(""), '€{:,.2f}'.format(discountGBACost))

# output total cost
print("\n", '{:>45}'.format("Total:"), '{:>21}'.format(""), '€{:,.2f}'.format(total))

