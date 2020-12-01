departure = int(input("What day are you leaving (0-6)?"))

stay_period = float(input("How many days will you be away?"))

ledger = int((departure+stay_period) % 6)

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

answer = days_of_the_week[ledger]

print("You will return on:", answer)

