import datetime

today_string = "04-07-2025"

parsed_date = datetime.datetime.strptime(today_string, "%m-%d-%Y")

print("Parsed date:", parsed_date)
