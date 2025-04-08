import datetime
today_date = datetime.datetime.now().strftime("%m-%d-%Y")

with open("today.txt", "w") as file:
    file.write(today_date)

print("Today's date has been written to today.txt")