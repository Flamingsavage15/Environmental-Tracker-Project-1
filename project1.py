shower1 = input("How many showers do you take per week on average: ")
shower2 = input("On average, how long do you shower for this many minutes: ")

# Converting input into intergers for math
shower1 = int(shower1)
shower2 = int(shower2)

# Weekly shower length math and convert into string to print
weeklyshower = (shower1 * shower2)
weeklyshower = str(weeklyshower)

print ("On average, you spend " + weeklyshower + " mintues a week." )

# Weekly water consumption
# According to EPA, 2.5 gallons of water are spent per minute in a shower
watergallons = int(2.5) 
waterweek = (watergallons * weeklyshower)
waterweek = str(waterweek)

print ("That means you spend roughly " + waterweek + " gallons of water per week on showers alone.")

# Yearly water consumption math
yearweeks = int(52.143) # weeks per year
wateryear = (waterweek * yearweeks)
wateryear = str(wateryear)

print ("That is equivalent to " + wateryear + "gallons per year")