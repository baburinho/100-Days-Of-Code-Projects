# tip calculator
# calculates the amount of tip for a bill and then divides that total cost among members of the group

print('Welcome to the tip calculator')
total = float(input("What was the total bill? $"))
people_num = float(input("How many people to split the bill? "))
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

if percentage == '10':
    tip = total*0.1
    tot_tip = tip+total
    amount_paid = round(tot_tip/people_num, 2)
    print(f"Each person should pay: {amount_paid}")
elif percentage == '12':
    tip = total*0.12
    tot_tip = tip+total
    amount_paid = round(tot_tip/people_num, 2)
    print(f"Each person should pay: {amount_paid}")
elif percentage == '15':
    tip = total*0.15
    tot_tip = tip+total
    amount_paid = round(tot_tip/people_num, 2)
    print(f"Each person should pay: {amount_paid}")