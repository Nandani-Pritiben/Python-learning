# movie tickets: $12 on adult (18 or above) , $8 for child and on wednesday 2$ discount

age=int(input("Enter your age:"))
print("MonDay","TuesDay","WednesDay","ThurseDay","FriDay","SaturDay","SunDay")
day=str(input("Enter your weekday:"))
if day=='WednesDay':
  if(age<18):
    print(f'Hurray! Today is {day} you get 2$ discount so your ticket price:$6')
  else:
    print(f'Hurray! Today is {day} you get 2$ discount so your ticket price:$10')
else:
  if(age<18):
    print("$8")
  else:
    print("$12")