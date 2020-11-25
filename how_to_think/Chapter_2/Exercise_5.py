principal = int(input("What is your initial investment in Euros?"))

interest_rate_percent = 5
interest_rate_decimal = interest_rate_percent / 100

compound_number = 4

time = int(input("How long (in years) would you like to invest?"))

final_amount = principal*(1+(interest_rate_decimal/compound_number))**(compound_number*time)

final_amount_1 = round(final_amount, 2)

print("With a", interest_rate_percent, "% interest rate, you will earn: €", final_amount_1)
