from dateutil import parser
date_time=input("Enetr a date and time: ")
date_time = parser.parse(date_time)
print(date_time)
