current_time = int(input("What is the time now (in hours 0-23)?"))
wait_time = int(input("In how many hours do you want to be alerted?"))

final_time_int = current_time + wait_time

final_answer = final_time_int % 24

print("Your alarm will go off at:", final_answer)
