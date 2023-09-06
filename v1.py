# Take gender
# Take 5 girth measurements
# Use equation based on gender

# siri_equation = (495/body_density) - 450



gender = (input("Enter your gender (f or m):\n")).lower()
while gender != "f" and gender != "m":
  print('Enter a valid gender')
  gender = (input("Enter your gender (f or m):\n")).lower()
  
if gender == 'f':
  measurements = ['triceps', 'thigh', "suprailiac"]
  sum = 0
  for i in measurements:
    x = input(f'Enter the measurements for your {i} in mm: ')
    while not x.isdigit() and "." not in x:
      print("That's not valid.")
      x = input(f'Enter the measurements for your {i} in mm: ')
    x = int(x)
    sum += x

  age = input('Enter your age in years: ')
  while not age.isdigit():
    print("That's not valid.")
    age = input('Enter your age in years: ')
  age = int(age)
  

  

elif gender == "m":
  pass