#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

bill_per_person = bill / num_people
tip_as_percent = tip / 100

tip_per_person = bill_per_person * tip_as_percent

bill_per_person_plus_tip = bill_per_person + tip_per_person
# alternatives
# bill_with_tip = tip / 100 * bill + bill
# bill_with_tip = total_bill + (1 + tip_percentage / 100)

rounded_pay_per_person = round(bill_per_person_plus_tip, 2)
formatted_pay_per_person = "{:.2f}".format(bill_per_person_plus_tip)
print(f"Each person should pay: ${rounded_pay_per_person}") 
# prints 33.6, which is not showing 2 decimals cause it's an exact division
print(f"Each person should pay: ${formatted_pay_per_person}") 
