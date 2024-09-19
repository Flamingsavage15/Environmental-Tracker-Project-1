shower1 = input("How many showers do you take per week on average: ")
shower2 = input("On average, how long do you shower for this many minutes: ")

#converting input into intergers for math
shower1 = int(shower1)
shower2 = int(shower2)

# Weekly shower length math and convert into string to print
weeklyshower = (shower1 * shower2)
weeklyshower = str(weeklyshower)

print ("On average, you spend " + weeklyshower + " mintues a week." )