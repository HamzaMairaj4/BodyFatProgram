# Take gender
# Take 5 girth measurements
# Use equation based on gender

# siri_equation = (495/body_density) - 450



gender = (input("Enter your gender (f or m):\n")).lower()
while gender != "f" and gender != "m":
  print('Enter a valid gender')
  gender = (input("Enter your gender (f or m):\n")).lower()

measurements1 = []
values_lst = []
  
if gender == 'f':
  measurements1 = ['triceps', 'thigh', "suprailiac"]
  last = ""
elif gender == "m":
  measurements1 = ['chest', 'abdomen', "thigh"]

sum = 0
for i in measurements1:
  x = input(f'Enter the measurements for your {i} in mm: ')
  while x.isdigit() and "." not in x:
    print("That's not valid.")
    x = input(f'Enter the measurements for your {i} in mm: ')
  x = float(x)
  sum += x
values_lst.append(sum)

age = input('Enter your age in years: ')
while not age.isdigit():
  print("That's not valid.")
  age = input('Enter your age in years: ')
age = int(age)
values_lst.append(age)

