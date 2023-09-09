# This part of code takes the user's gender and uses input validation to make sure it's valid
gender = (input("Enter your gender (f or m):\n")).lower()
while gender != "f" and gender != "m":
  print("That's not valid.")
  gender = (input("Enter your gender (f or m):\n")).lower()


# This part checks to see which gender the person selected and updates two different lists with different body parts based on their gender
if gender == 'f':
  measurements1 = ['triceps', 'thigh', "suprailiac"]
  last = ["gluteal"]
else:
  measurements1 = ['chest', 'abdomen', "thigh"]
  last = ["waist", "forearm"]


# This initializes the main values list that has all the values used in the equation, gets the user's input for the items in measurements1, adds those values up, and appends the sum to the main values list
values_lst = []
sum = 0
for i in measurements1:
  while True:
    try:
      measure = float(input(f'Enter the measurements for your {i} skinfolds in mm: ')) 
    except ValueError:
      print("That's not valid.")
      continue 
    sum += measure
    break
values_lst.append(sum)


# This just asks for the user's age, checks to make sure the str entered is an integer, and then appends the age to the values list
age = input('Enter your age in years: ')
while not age.isdigit():
  print("That's not valid.")
  age = input('Enter your age in years: ')
age = int(age)
values_lst.append(age)


# This initializes a new list and iterates through the list last, which will be different depending on the gender of the person, then asks for the values of the items in last, and then appends those values to the values list.
for i in last:
  while True:
    try:
      if gender == 'm':
        new = float(input(f"Input your {i} circumference in m: "))
      else:
        new = float(input(f"Input your {i} circumference in cm: "))
    except ValueError:
      print("That's not valid")
      continue
    values_lst.append(new)
    break


# This finds the body density based on the person's gender using the Pollock equations and popping the values from the value list
if gender == "m": 
  body_density = 1.0990750 - (0.0008209*values_lst[0]) 
  body_density += (0.00000262*((values_lst.pop(0)**2))) 
  body_density -= (0.0002017*values_lst.pop(0)) 
  body_density -= (0.005675*values_lst.pop(0)) 
  body_density += (0.018586*values_lst.pop(0))
else:
  body_density = 1.1470292 - (0.0009376*values_lst[0])
  body_density += ((0.0000030*(values_lst.pop(0)**2))) 
  body_density -= (0.0001156*values_lst.pop(0)) 
  body_density -= (0.0005839*values_lst.pop(0))


#Print statements with both the body density and body fat percentage
print(f"Your body density is {body_density:.3f}.")

body_fat = (495/body_density) - 450
print(f"Your body fat percentage is {body_fat:.3f}%.")
