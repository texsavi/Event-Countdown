
import datetime,time,os
s=""

today=datetime.date.today()
event=input("Enter name of event>>@ ").title()
time.sleep(1.5)
os.system("clear")

print()

print(f"{s:^18} ✅⭐The {event} Event Countdown⚡✅")
print()

try:
  year=int(input("Year of event> "))
  month=int(input("Month> "))
  day=int(input("Day> "))
except:
  print("Input dates in numbers only...")
  
eveDate=datetime.date(year,month,day)

days=eveDate-today
days=days.days

print()

if eveDate>today:
  print(f"⭐⚡{days} days left to the {event} event⚡⭐")
elif eveDate==today:
  print("Woohooo!!✨✨⭐🥳The day is finally here🎉🥳⚡🥳")
else:
  print("Uh!Oh!😢The event already happened😪☹️☹️🥱😔😔")
  