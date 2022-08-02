print("Welcome to the tip calculator")

total_bill = input("What was the total bill? $")
new_total_bill = float(total_bill)

percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")

new_percentage = int(percentage)

percentage_cal = (new_percentage/100)

split_bill = input("How many people to split the bill? ")

split_bill_new = int(split_bill)

total_each_person = round((new_total_bill/split_bill_new)*(1+percentage_cal),2)

print(f"Each person should pay: ${total_each_person}")