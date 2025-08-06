import calendar
def generate_calendar(year, month):
    return calendar.month(year, month)
y=int(input("Enter year:"))
m=int(input("Enter month:"))
n=generate_calendar(y,m)
print(n)
