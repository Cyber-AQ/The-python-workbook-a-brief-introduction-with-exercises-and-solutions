import math
# the_python_workbook_a_brief_introduction_with_exercises_and_solutions.
# Exercise 1: Mailing Address
# (Solved, 9 Lines)
# Create a program that displays your name and complete mailing address. The address
# should be printed in the format that is normally used in the area where you live. Your
# program does not need to read any input from the user.

# name = "Brice Robert Aquiline"
# # input("Enter your name here...")
#
# mail = "Mingoi"
# # input("Enter your mail address too here...")
#
# print(name)
# print(mail)


# Exercise 2: Hello
# (9 Lines)
# Write a program that asks the user to enter his or her name. The program should
# respond with a message that says hello to the user, using his or her name.

# name = input("Enter your name here...")
# print("hello, ", name)


# Exercise 3: Area of a Room
# (Solved, 13 Lines)
# Write a program that asks the user to enter the width and length of a room. Once
# these values have been read, your program should compute and display the area of
# the room. The length and the width will be entered as floating-point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.

# width = float(input("Enter width..."))
# length = float(input("Enter length..."))
# area = width * length
# print("your area is: {} m".format(area))


# Exercise 4: Area of a Field
# (Solved, 15 Lines)
# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre.

# width = float(input("Enter width..."))
# length = float(input("Enter length..."))
# area = (width * length) / 43560
# print("Area = {}".format(area))


# Exercise 5: Bottle Deposits
# (Solved, 15 Lines)
# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and two digits to the right of the decimal point.

# summation = 0
# sh1_litre = 0.10
# sh1_litreMore = 0.25
# drink_1Litre = sh1_litre
# drink_1LitreMore = sh1_litreMore
# containers_1LitreMore = int(input("how many number of containers of more than 1 litre do you have?"))
# containers_1Litre = int(input("how many number of containers of 1 litre or less do you have?"))
# total_1LitreMore = containers_1LitreMore * drink_1LitreMore
# total_1Litre = containers_1Litre * drink_1Litre
# summation = total_1LitreMore + total_1Litre
# print("Total refund is: {:.2f}".format(summation))


# Exercise 6: Tax and Tip
# (Solved, 17 Lines)
# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.

# print("Welcome to: PROGRAMMING RESTAURANT!")
# print("Here is the menu and the price below:")
# print("1. chai ya rangi     200/=")
# print("2. chai ya maziwa     300/=")
# print("3. maandazi     200/=")
# print("4. chapati     500/=")
# print("5. skonzi     500/=")
# print("6. chips kavu     1,500/=")
# print("7. chips mayai     2,000/=")
# print("8. mshikaki     500/=")
# print("9. wali nazi     4,500/=")
# print("10. wali mchuzi wa samaki     2,000/=")
# print("11. ugali maharage     1,500/=")
#
# tax = 0.18
# tip = 0.18
# food_eaten = int(input("Enter total amount eaten here..."))
# total_tax = tax * food_eaten
# total_tip = tip * food_eaten
# total = total_tax + total_tip + food_eaten
# print("you ate total of: ${:.2f}".format(food_eaten))
# print("Total tax amount is: ${:.2f}".format(total_tax))
# print("Total tip amount is: ${:.2f}".format(total_tip))
# print("Total amount paid on Bank card is: ${:.2f}".format(total))


# Exercise 7: Sum of the First n Positive Integers
# (Solved, 11 Lines)
# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
# sum = (n)(n + 1)
#       ----------
#           2

# n = int(input("Enter a positive integer!"))
# summation = (n * (n + 1)) / 2
# print("Sum is: {}".format(summation))


# Exercise 8: Widgets and Gizmos
# (15 Lines)
# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos from the user. Then your program should compute
# and display the total weight of the parts.

# widget = 75  # per each for grams
# gizmo = 112  # per each for grams
# no_widget = int(input("Enter number of Widgets..."))
# no_gizmo = int(input("Enter number of gizmo..."))
#
# total_widgets = no_widget * widget
# total_gizmo = no_gizmo * gizmo
#
# print("Number of Widget = {}".format(total_widgets))
# print("Number of Gizmos = {}".format(total_gizmo))


# Exercise 9: Compound Interest
# (19 Lines)
# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added to the
# balance of the savings account. Write a program that begins by reading the amount of
# money deposited into the account from the user. Then your program should compute
# and display the amount in the savings account after 1, 2, and 3 years. Display each
# amount so that it is rounded to 2 decimal places.

# interest = 4 / 100
# Amount = int(input("Enter Amount to deposit here..."))
# real_interest = interest * Amount
# print("Your Amount Deposited is: ${:.2f}".format(Amount))
# print("Your Amount of interest is: ${:.2f}".format(real_interest))
# year = int(input("Enter number of years from 1-3 years..."))
# yearly_Amount = (real_interest + Amount) * year
# print("Amount for year {0} is: ${1:.2f}".format(year, yearly_Amount))


# Exercise 10: Arithmetic
# (Solved, 22 Lines)
# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of a**b
# Hint: You will probably find the log10 function in the math module helpful
# for computing the second last item in the list.

# a = int(input("value 1?"))
# print("value 1 is: {}".format(a))
# b = int(input("value 2?"))
# print("value 2 is: {}".format(b))
# print("Sum result is: {}".format(a+b))
# print("Difference result is: {}".format(b-a))
# print("Product result is: {}".format(a*b))
# print("Quotient result is: {}".format(a/b))
# print("Remainder result is: {}".format(a+b))
# print("Log result is: {}".format(math.log10(a)))
# print("Square root result is: {}".format(a**b))
# print("power of result is: {}".format(math.pow(a, b)))


# Exercise 11: Fuel Efficiency
# (13 Lines)
# In the United States, fuel efficiency for vehicles is normally expressed in miles-pergallon (MPG).
# In Canada, fuel efficiency is normally expressed in liters-per-hundred kilometers (L/100 km).
# Use your research skills to determine how to convert from MPG to L/100 km.
# Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units.




# Exercise 12: Distance Between Two Points on Earth
# (27 Lines)
# The surface of the Earth is curved, and the distance between degrees of longitude
# varies with latitude. As a result, finding the distance between two points on the surface
# of the Earth is more complicated than simply using the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
# surface. The distance between these points, following the surface of the Earth, in
# kilometers is:
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
# The value 6371.01 in the previous equation wasn't selected at random. It is the
# average radius of the Earth in kilometers.
# Create a program that allows the user to enter the latitude and longitude of two
# points on the Earth in degrees. Your program should display the distance between
# the points, following the surface of the earth, in kilometers.
# Hint: Python’s trigonometric functions operate in radians. As a result, you will
# need to convert the user’s input from degrees to radians before computing the
# distance with the formula discussed previously. The math module contains a
# function named radians which converts from degrees to radians

# t1 = int(input("Enter latitude 1"))
# t2 = int(input("Enter latitude 2"))
# g1 = int(input("Enter longitude 1"))
# g2 = int(input("Enter longitude 2"))
# # 10600.622383278864 - answer in degrees
# # 10003.68219476696  - answer in radians
# T1 = math.radians(t1)
# T2 = math.radians(t2)
# G1 = math.radians(g1)
# G2 = math.radians(g2)
# distance = 6371.01 * math.acos(math.sin(T1) * math.sin(T2) * math.cos(T1) * math.cos(T2) * math.cos(G1 - G2))
#
# print("The distance is: {}".format(distance))


# Exercise 13: Making Change
# (Solved, 35 Lines)
# Consider the software that runs on a self-checkout machine. One task that it must be
# able to perform is to determine how much change to provide when the shopper pays
# for a purchase with cash.
# Write a program that begins by reading a number of cents from the user as an
# integer. Then your program should compute and display the denominations of the
# coins that should be used to give that amount of change to the shopper. The change
# should be given using as few coins as possible. Assume that the machine is loaded
# with pennies, nickels, dimes, quarters, loonies and toonies.
# A one dollar coin was introduced in Canada in 1987. It is referred to as a loonie
# because one side of the coin has a loon (a type of bird) on it. The two dollar
# coin, referred to as a toonie, was introduced 9 years later. It’s name is derived
# from the combination of the number two and the name of the loonie.




# Exercise 14: Height Units
# (Solved, 16 Lines)
# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.
# Hint: One foot is 12 inches. One inch is 2.54 centimeters.

# h1 = int(input("Enter height for feet..."))
# h2 = int(input("Enter height for inches..."))
#
# h2_Into_Cm = h2 * 2.54
#
# h1_into_inches = h1 * 12
#
# h1_into_Cm = h1_into_inches * 2.54
#
# print()
# print("height 1 of {0}feet into {1}Cm".format(h1, h1_into_Cm))
# print("height 2 of {0}feet into {1}Cm {}Cm".format(h2, h2_Into_Cm))


# Exercise 15: Distance Units
# (20 Lines)
# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don’t have them memorized.

# reading = int(input("Enter your readings here..."))
# print("Now converting the reading from you, into inches!")
# inches = reading * 12
# yards = reading * 0.3333
# miles = reading * 0.00019
#
# print("Reading of {0}feet into {1}inches".format(reading, inches))
# print("Reading of {0}feet into {1}yards".format(reading, yards))
# print("Reading of {0}feet into {1}miles".format(reading, miles))


# Exercise 16: Area and Volume
# (15 Lines)
# Write a program that begins by reading a radius, r, from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r. Use the pi constant in the math module in your calculations.
# Hint: The area of a circle is computed using the formula area = πr**2.
# The volume of a sphere is computed using the formula volume = 4/3 πr**3.

# r = int(input("Radius required..."))
# area = math.pi * (r ** 2)
# volume = (4 / 3) * math.pi * (r ** 3)
# print("The Area is: {}".format(area))
# print("The Volume is: {}".format(volume))


# Exercise 17: Heat Capacity
# (Solved, 23 Lines)
# The amount of energy required to increase the temperature of one gram of a material
# by one degree Celsius is the material’s specific heat capacity, C. The total amount
# of energy, q, required to raise m grams of a material by ΔT degrees Celsius can be
# computed using the formula:
# q = mCΔT
# Write a program that reads the mass of some water and the temperature change from
# the user. Your program should display the total amount of energy that must be added
# or removed to achieve the desired temperature change.
# Hint: The specific heat capacity of water is 4.186 J
# g◦C. Because water has a
# density of 1.0 grams per milliliter, you can use grams and milliliters interchangeably in this exercise.
# Extend your program so that it also computes the cost of heating the water.
# Electricity is normally billed using units of kilowatt hours rather than Joules. In this
# exercise, you should assume that electricity costs 8.9 cents per kilowatt hour. Use
# your program to compute the cost of boiling the water needed for a cup of coffee.
# Hint: You will need to look up the factor for converting between Joules and
# kilowatt hours to complete the last part of this exercise.

# m = int(input("Enter some water mass!"))
# t = int(input("Enter some change of temperature observed!"))
# c = 4.186  # joule / gram * degree celcius
# q = m * c * t
# print("Total amount of energy is: {} joules".format(q))


# Exercise 18: Volume of a Cylinder
# (15 Lines)
# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place.

# radius = int(input("Enter the radius of the cylinder..."))
# height = int(input("Enter the height of the cylinder..."))
# area = 2 * math.pi * radius**2
# volume = area * height
# print("The volume is {:.1f}cm cubic".format(volume))


# Exercise 19: Free Fall
# (Solved, 15 Lines)
# Create a program that determines how quickly an object is travelling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
# due to gravity is 9.8 m/s2. You can use the formula vf = square root(square(V)+ 2ad) to compute the
# final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.




# Exercise 20: Ideal Gas Law
# (19 Lines)
# The ideal gas law is a mathematical approximation of the behavior of gasses as
# pressure, volume and temperature change. It is usually stated as:
# PV = nRT
# where P is the pressure in Pascals, V is the volume in liters, n is the amount of
# substance in moles, R is the ideal gas constant, equal to 8.314 J
# mol K , and T is the
# temperature in degrees Kelvin.
# Write a program that computes the amount of gas in moles when the user supplies
# the pressure, volume and temperature. Test your program by determining the number
# of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
# a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
# approximately 20 degrees Celsius or 68 degrees Fahrenheit.
# Hint: A temperature is converted from Celsius to Kelvin by adding 273.15
# to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it,
# multiply it by 5
# 9 and then add 273.15 to it.




# Exercise 21: Area of a Triangle
# (13 Lines)
# The area of a triangle can be computed using the following formula, where b is the
# length of the base of the triangle, and h is its height:
# area = b × h
#        -----
#          2
# Write a program that allows the user to enter values for b and h. The program should
# then compute and display the area of a triangle with base length b and height h.




# Exercise 22: Area of a Triangle (Again)
# (16 Lines)
# In the previous exercise you created a program that computed the area of a triangle
# when the length of its base and its height were known. It is also possible to compute
# the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
# be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
# can be calculated using the following formula:
# area =square root(s × (s − s1) × (s − s2) × (s − s3))
# Develop a program that reads the lengths of the sides of a triangle from the user and
# displays its area.




# Exercise 23: Area of a Regular Polygon
# (Solved, 14 Lines)
# A polygon is regular if its sides are all the same length and the angles between all of
# the adjacent sides are equal. The area of a regular polygon can be computed using
# the following formula, where s is the length of a side and n is the number of sides:
# area = n × s2
# 4 × tan π
# n
# 
# Write a program that reads s and n from the user and then displays the area of a
# regular polygon constructed from these values.




# Exercise 24: Units of Time
# (22 Lines)
# Create a program that reads a duration from the user as a number of days, hours,
# minutes, and seconds. Compute and display the total number of seconds represented
# by this duration.




# Exercise 25: Units of Time (Again)
# (Solved, 24 Lines)
# In this exercise you will reverse the process described in Exercise 24. Develop a
# program that begins by reading a number of seconds from the user. Then your program
# should display the equivalent amount of time in the form D:HH:MM:SS, where D,
# HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours,
# minutes and seconds should all be formatted so that they occupy exactly two digits.
# Use your research skills determine what additional character needs to be included in
# the format specifier so that leading zeros are used instead of leading spaces when a
# number is formatted to a particular width.




# Exercise 26: Current Time
# (10 Lines)
# Python’s time module includes several time-related functions. One of these is the
# asctime function which reads the current time from the computer’s internal clock
# and returns it in a human-readable format. Use this function to write a program that
# displays the current time and date. Your program will not require any input from the
# user.




# Exercise 27: When is Easter?
# (33 Lines)
# Easter is celebrated on the Sunday immediately after the first full moon following the
# spring equinox. Because its date includes a lunar component, Easter does not have
# a fixed date in the Gregorian calendar. Instead, it can occur on any date between
# March 22 and April 25. The month and day for Easter can be computed for a given
# year using the Anonymous Gregorian Computus algorithm, which is shown below.
# Set a equal to the remainder when year is divided by 19
# Set b equal to the floor of year divided by 100
# Set c equal to the remainder when year is divided by 100
# Set d equal to the floor of b divided by 4
# Set e equal to the remainder when b is divided by 4
# Set f equal to the floor of
# b + 8
# 25
# Set g equal to the floor of
# b − f + 1
# 3
# Set h equal to the remainder when 19a + b − d − g + 15 is divided by 30
# Set i equal to the floor of c divided by 4
# Set k equal to the remainder when c is divided by 4
# Set l equal to the remainder when 32 + 2e + 2i − h − k is divided by 7
# Set m equal to the floor of a + 11h + 22l
# 451
# Set month equal to the floor of
# h + l − 7m + 114
# 31
# Set day equal to one plus the remainder when h + l − 7m + 114 is divided
# by 31
# Write a program that implements the Anonymous Gregorian Computus algorithm
# to compute the date of Easter. Your program should read the year from the user and
# then display a appropriate message that includes the date of Easter in that year.




# Exercise 28: Body Mass Index
# (14 Lines)
# Write a program that computes the body mass index (BMI) of an individual. Your
# program should begin by reading a height and weight from the user. Then it should
# use one of the following two formulas to compute the BMI before displaying it. If
# you read the height in inches and the weight in pounds then body mass index is
# computed using the following formula:
# BMI = weight
# height × height × 703
# If you read the height in meters and the weight in kilograms then body mass index
# is computed using this slightly simpler formula:
# BMI = weight
# height × height




# Exercise 29: Wind Chill
# (Solved, 22 Lines)
# When the wind blows in cold weather, the air feels even colder than it actually is
# because the movement of the air increases the rate of cooling for warm objects, like
# people. This effect is known as wind chill.
# In 2001, Canada, the United Kingdom and the United States adopted the following formula for computing the wind chill index. Within the formula Ta is the
# air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
# A similar formula with different constant values can be used for temperatures in
# degrees Fahrenheit and wind speeds in miles per hour.
# WCI = 13.12 + 0.6215Ta − 11.37V0.16 + 0.3965TaV0.16
# Write a program that begins by reading the air temperature and wind speed from the
# user. Once these values have been read your program should display the wind chill
# index rounded to the closest integer.
# The wind chill index is only considered valid for temperatures less than or
# equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per
# hour.




# Exercise 30: Celsius to Fahrenheit and Kelvin
# (17 Lines)
# Write a program that begins by reading a temperature from the user in degrees
# Celsius. Then your program should display the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin. The calculations needed to convert between different
# units of temperature can be found on the Internet.




# Exercise 31: Units of Pressure
# (20 Lines)
# In this exercise you will create a program that reads a pressure from the user in kilopascals.
# Once the pressure has been read your program should report the equivalent
# pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
# your research skills to determine the conversion factors between these units.




# Exercise 32: Sum of the Digits in an Integer
# (18 Lines)
# Develop a program that reads a four-digit integer from the user and displays the sum
# of its digits. For example, if the user enters 3141 then your program should display
# 3+1+4+1=9.




# Exercise 33: Sort 3 Integers
# (Solved, 19 Lines)
# Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest
# and largest values. The middle value can be found by computing the sum of all three
# values, and then subtracting the minimum value and the maximum value.




# Exercise 34: Day Old Bread
# (Solved, 19 Lines)
# A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
# percent. Write a program that begins by reading the number of loaves of day old
# bread being purchased from the user. Then your program should display the regular
# price for the bread, the discount because it is a day old, and the total price. Each of
# these amounts should be displayed on its own line with an appropriate label. All of
# the values should be displayed using two decimal places, and the decimal points in
# all of the numbers should be aligned when reasonable values are entered by the user.
