print("Title of program: What your food should you try")
print()
print("Hello! Please answer the following questions truthfully and we'll suggest a type of food that you should try !")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

savoury1 = input("I enjoy savoury/ salty food like french fries.")

sweet1 = input("I'll go crazy withou having sugary stuff like sweets.")

healthy1 = input("I am a health enthusiast and prefer not to eat junk food.")

sour2 = input("I like chewy food as it keeps me awake throughout the day.")

sour1 = input("I like sour food as it gives me abit of zest.")

drinks1 = input("I like drinks more than snacks.")

drinks2 = input("I like sugary drinks that is not quite healthy ")

healthy2 = input(" I want to healthy but I do not have motivation to do so")

sweet2 = input(" I am very high-classed")

savoury2 = input("I go to western stalls often")




savoury_final = int(savoury1) + int(savoury2)
sweet_final = int(sweet1) + int(sweet2)
healthy_final = int(healthy1)+ int(healthy2)
sour_final = int(sour1)+ int(sour2)
drinks_final = int(drinks1)+ int(drinks2)

print()

if sweet_final > savoury_final and drinks_final > healthy_final:
  print("You might like Cheesecake!")
elif savoury_final > healthy_final:
  print("You might like Mcdonald's fries set!")
elif sour_final > healthy_final:
  print("You might like Sour Patch Kids sweet!")
elif drinks_final > sour_final and savoury_final:
  print("You might like Bubble tea!")
else:
  print("You might be suitable for yogurt,  fruits and gronola or kale chips!")
