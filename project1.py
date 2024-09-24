# Project Version 1 : Water Consumption from Showers
print (' ')
shower1 = input("How many showers do you take per week on average: ")
print (' ')
shower2 = input("On average, how long do you shower for this many minutes: ")

# Converting input into intergers for math
shower1 = int(shower1)
shower2 = int(shower2)

# Weekly shower length math and convert into string to print
weeklyshower = (shower1 * shower2)
weeklyshower = str(weeklyshower)

print (' ')
print ("That means, on average, you spend " + weeklyshower + " mintues a week." )

# Weekly water consumption
# According to EPA, 2.5 gallons of water are spent per minute in a shower (Round up to 3)

waterweek = (int(2) * int(weeklyshower)) 
waterweek = str(waterweek)

print (' ')
print ("That is roughly equivalent to " + waterweek + " gallons of water per week on showers alone.")

# Yearly water consumption math 

wateryear = (int(waterweek) * int(52)) 
wateryear = str(wateryear)

print (' ')
print ("That is equivalent to " + wateryear + " gallons per year just showering.")
print (' ')

# Project Version 1.2 : Meal... 
print (' ')
mealday = input('Now on average, how many meals you you eat per day: ')

mealday = int(mealday)
mealweek = (int(mealday) * int(7))
mealweek = str(mealweek)

print (' ')
print ('This means you eat ' + mealweek + ' on average.')
print (' ')

# Project Version 1.3 : Miles Driven (Advanced; Teach myself to work on now)