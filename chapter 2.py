import math
# Exercise 35: Even or Odd?
# (Solved, 13 Lines)
# Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd.

# i = int(input("Enter a value"))
# if i % 2 == 0:
#     print("This number {} is an even number!".format(i))
# else:
#     print("This number {} is an odd number!".format(i))


# Exercise 36: Dog Years
# (22 Lines)
# It is commonly said that one human year is equivalent to 7 dog years. However this
# simple conversion fails to recognize that dogs reach adulthood in approximately two
# years. As a result, some people believe that it is better to count each of the first two
# human years as 10.5 dog years, and then count each additional human year as 4 dog
# years.
# Write a program that implements the conversion from human years to dog years
# described in the previous paragraph. Ensure that your program works correctly for
# conversions of less than two human years and for conversions of two or more human
# years. Your program should display an appropriate error message if the user enters
# a negative number.

# human1 = 1  # equivalent to 7 dogs... dog1.
# human2 = 2  # in two years dog reach adult hood.
# dog1 = 7
# dog2 = 10.5  # # equivalent to 10.5 dogs... dog2
# # for each additional human year count as 4 dog years.
# print("enter human age...")
# user = float(input())
# summation = (user * (user+1)) / 2


# Exercise 37:Vowel or Consonant
# (Solved, 16 Lines)
# In this exercise you will create a program that reads a letter of the alphabet from the
# user. If the user enters a, e, i, o or u then your program should display a message
# indicating that the entered letter is a vowel. If the user enters y then your program
# should display a message indicating that sometimes y is a vowel, and sometimes y is
# a consonant. Otherwise your program should display a message indicating that the
# letter is a consonant.

# user = input("Enter an alphabet...")
# if user == "a" or user == "e" or user == "i" or user == "o" or user == "u":
#     print("This {} is a vowel".format(user))
# elif user == "y":
#     print("This {} is sometimes a vowel or a consonant".format(user))
# else:
#     print("This {} is consonant".format(user))


# Exercise 38: Name That Shape
# (Solved, 31 Lines)
# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides.
# If a number of sides outside of this range is entered then your program should display an appropriate error message.

# user = int(input("Enter number of figures sides here..."))
# if user == 1:
#     print("This is a circle")
# elif user == 3:
#     print("This is a triangle")
# elif user == 4:
#     print("This is can be a cube, a square or a triangle")
# elif user == 5:
#     print("This is a pentagon")
# elif user == 6:
#     print("This is a hexagon")
# elif user == 7:
#     print("This is a heptagon")
# elif user == 8:
#     print("This is a octagon")
# elif user == 9:
#     print("This is a nonagon")
# elif user == 10:
#     print("This is a decagon")
# else:
#     print("The database does not recognise such figure with {} shapes.".format(user))


# Exercise 39: Month Name to Number of Days
# (Solved, 18 Lines)
# The length of a month varies from 28 to 31 days. In this exercise you will create
# a program that reads the name of a month from the user as a string. Then your
# program should display the number of days in that month. Display “28 or 29 days”
# for February so that leap years are addressed.

# received = input("Enter name of the month here...")
# user = received.lower()
# if user == "january":
#     print("{} has 31 days".format(user))
# elif user == "february":
#     print("{} has 28 days".format(user))
# elif user == "march":
#     print("{} has 31 days".format(user))
# elif user == "april":
#     print("{} has 30 days".format(user))
# elif user == "may":
#     print("{} has 31 days".format(user))
# elif user == "june":
#     print("{} has 30 days".format(user))
# elif user == "july":
#     print("{} has 31 days".format(user))
# elif user == "august":
#     print("{} has 31 days".format(user))
# elif user == "september":
#     print("{} has 30 days".format(user))
# elif user == "october":
#     print("{} has 31 days".format(user))
# elif user == "november":
#     print("{} has 30 days".format(user))
# elif user == "december":
#     print("{} has 31 days".format(user))
# else:
#     print("There is no such a month as {}".format(user))


# Exercise 40: Sound Levels
# (30 Lines)
# The following table lists the sound level in decibels for several common noises.
# Noise Decibel Level
# Jackhammer 130 dB
# Gas Lawnmower 106 dB
# Alarm Clock 70 dB
# Quiet Room 40 dB
# Write a program that reads a sound level in decibels from the user. If the user
# enters a decibel level that matches one of the noises in the table then your program
# should display a message containing only that noise. If the user enters a number
# of decibels between the noises listed then your program should display a message
# indicating which noises the value is between. Ensure that your program also generates
# reasonable output for a value smaller than the quietest noise in the table, and for a
# value larger than the loudest noise in the table.

# user = int(input("Enter value of sound level"))
# if user == 130:
#     print("{}db, it's a Jackhammer's noise".format(user))
# elif user == 106:
#     print("{}db, it's a Gas Lawnmower noise".format(user))
# elif user == 70:
#     print("{}db, it's an Alarm Clock noise".format(user))
# elif user == 40:
#     print("{}db, it's a Quiet room noise".format(user))
# elif user > 130:
#     print("{}db it's a Louder noise that can't be handled".format(user))
# elif user < 40:
#     print("{}db, it's so lower noise that can't be heard".format(user))
# else:
#     print("{}db, it's not an exactly known noise.".format(user))


# Exercise 41: Classifying Triangles
# (Solved, 21 Lines)
# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
# scalene. All three sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of the three sides of a triangle from the
# user. Then display a message that states the triangle’s type.

# s1 = float(input("Enter side 1"))
# s2 = float(input("Enter side 2"))
# s3 = float(input("Enter side 3"))
# if s1 == s2 or s1 == s3 or s2 == s3:
#     print("This is a Isosceles triangle")
# elif s1 == s2 == s3:
#     print("This is a Equivalent triangle")
# else:
#     print("This is a Scalene triangle")

# Exercise 41: Classifying Triangles
# (Solved, 21 Lines)
# A triangle can be classified based on the lengths of its sides as equilateral, isosceles or
# scalene. All three sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of the three sides of a triangle from the
# user. Then display a message that states the triangle’s type.
# Exercise 42: Note to Frequency
# (Solved, 39 Lines)
# The following table lists an octave of music notes, beginning with middle C, along
# with their frequencies.
# Note Frequency (Hz)
# C4 261.63
# D4 293.66
# E4 329.63
# F4 349.23
# G4 392.00
# A4 440.00
# B4 493.88
# --------------------
# Begin by writing a program that reads the name of a note from the user and
# displays the note’s frequency. Your program should support all of the notes listed
# previously.
# Once you have your program working correctly for the notes listed previously
# you should add support for all of the notes from C0 to C8. While this could be
# done by adding many additional cases to your if statement, such a solution is
# cumbersome, inelegant and unacceptable for the purposes of this exercise. Instead,
# you should exploit the relationship between notes in adjacent octaves.
# In particular, the frequency of any note in octave n is half the frequency of the corresponding note in octave n + 1.
# By using this relationship, you should be able to
# add support for the additional notes without adding additional cases to your if
# statement.
# Hint: You will want to access the characters in the note entered by the user
# individually when completing this exercise. Begin by separating the letter from
# the octave. Then compute the frequency for that letter in the fourth octave using
# the data in the table above. Once you have this frequency you should divide it
# by 24−x , where x is the octave number entered by the user. This will halve or
# double the frequency the correct number of times.

# print("Here are some of the name of music tones and there frequencies")
# print("Music note    frequency(Hz)")
# print("A4            440.00")
# print("B4            493.88")
# print("C4            261.63")
# print("D4            293.66")
# print("E4            329.63")
# print("F4            349.23")
# print("G4            392.00")
#
# user = input("Enter name of a tone:")
# if user == "A4":
#     print("{} is {}Hz".format(user, 440.00))
# elif user == "B4":
#     print("{} is {}Hz".format(user, 493.88))
# elif user == "C4":
#     print("{} is {}Hz".format(user, 261.63))
# elif user == "D4":
#     print("{} is {}Hz".format(user, 293.66))
# elif user == "E4":
#     print("{} is {}Hz".format(user, 329.63))
# elif user == "F4":
#     print("{} is {}Hz".format(user, 349.23))
# elif user == "G4":
#     print("{} is {}Hz".format(user, 392.00))
# else:
#     print("{} does not have a tone name nor frequency".format(user))
#


# Exercise 43: Frequency to Note
# (Solved, 42 Lines)
# In the previous question you converted from a note’s name to its frequency. In this
# question you will write a program that reverses that process. Begin by reading a
# frequency from the user. If the frequency is within one Hertz of a value listed in
# the table in the previous question then report the name of the corresponding note.
# Otherwise report that the frequency does not correspond to a known note. In this
# exercise you only need to consider the notes listed in the table. There is no need to
# consider notes from other octaves.

# print("Here are some of the name of music tones and there frequencies")
# print("Music note    frequency(Hz)")
# print("A4            440.00")
# print("B4            493.88")
# print("C4            261.63")
# print("D4            293.66")
# print("E4            329.63")
# print("F4            349.23")
# print("G4            392.00")
#
# user = float(input("Enter a frequency of a note:"))
# if user == 440.00:
#     print("{} is {}Hz".format(user, "A4"))
# elif user == 493.88:
#     print("{} is {}Hz".format(user, "B4"))
# elif user == 261.63:
#     print("{} is {}Hz".format(user, "C4"))
# elif user == 293.66:
#     print("{} is {}Hz".format(user, "D4"))
# elif user == 329.63:
#     print("{} is {}Hz".format(user, "E4"))
# elif user == 349.23:
#     print("{} is {}Hz".format(user, "F4"))
# elif user == 392.00:
#     print("{} is {}Hz".format(user, "G4"))
# else:
#     print("{} does not have a tone name nor frequency".format(user))


# Exercise 44: Faces on Money
# (31 Lines)
# It is common for images of a country’s previous leaders, or other individuals of historical significance,
# to appear on its money. The individuals that appear on banknotes
# in the United States are listed in below.
# Individual  Amount
# -----------------------
# George Washington $1
# Thomas Jefferson $2
# Abraham Lincoln $5
# Alexander Hamilton $10
# Andrew Jackson $20
# Ulysses S. Grant $50
# Benjamin Franklin $100
# -------------------------
# Write a program that begins by reading the denomination of a banknote from the
# user. Then your program should display the name of the individual that appears on the
# banknote of the entered amount. An appropriate error message should be displayed
# if no such note exists.
# While two dollar banknotes are rarely seen in circulation in the United States,
# they are legal tender that can be spent just like any other denomination. The
# United States has also issued banknotes in denominations of $500, $1,000,
# $5,000, and $10,000 for public use. However, high denomination banknotes
# have not been printed since 1945 and were officially discontinued in 1969. As
# a result, we will not consider them in this exercise.

# money = int(input("Enter a denomination of an American banknote:"))
# if money == 1:
#     name = "George Washington"
# elif money == 2:
#     name = "Thomas Jefferson"
# elif money == 5:
#     name = "Abraham Lincoln"
# elif money == 10:
#     name = "Alexander Hamilton"
# elif money == 20:
#     name = "Andrew Jackson"
# elif money == 50:
#     name = "Ulysses S. Grant"
# elif money == 50:
#     name = "Benjamin Franklin"
# else:
#     name = "Currency not recognised"
#
# print("${} has president {}".format(money, name))


# Exercise 45: Date to Holiday Name
# (18 Lines)
# Canada has three national holidays which fall on the same dates each year.
# Holiday Date
# --------------------------
# New Year’s Day January 1
# Canada Day July 1
# Christmas Day December 25
# --------------------------
# Write a program that reads a month and day from the user. If the month and day
# match one of the holidays listed previously then your program should display the
# holiday’s name. Otherwise your program should indicate that the entered month and
# day do not correspond to a fixed-date holiday.
# Canada has two additional national holidays, Good Friday and Labour Day,
# whose dates vary from year to year. There are also numerous provincial and
# territorial holidays, some of which have fixed dates, and some of which have
# variable dates. We will not consider any of these additional holidays in this
# exercise.

# day = int(input("Enter number of a holiday date"))
# Month = input("Enter month of a holiday date")
# month = Month.lower()
# if month == "january" and day == 1:
#     print("On {} {} is a {} holiday".format(day, month, "New Year’s Day"))
# elif month == "july" and day == 1:
#     print("On {} {} is a {} holiday".format(day, month, "Canada Day"))
# elif month == "december" and day == 25:
#     print("On {} {} is a {} holiday".format(day, month, "Christmas Day"))
# else:
#     print("entered month and day do not correspond to a fixed-date holiday")


# Exercise 46:What Color Is That Square?
# (22 Lines)
# Positions on a chess board are identified by a letter and a number. The letter identifies
# the column, while the number identifies the row, as shown below:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# a  b  c  d  e  f  g  h
# Write a program that reads a position from the user. Use an if statement to
# determine if the column begins with a black square or a white square. Then use
# modular arithmetic to report the color of the square in that row. For example, if the
# user enters a1 then your program should report that the square is black. If the user
# enters d5 then your program should report that the square is white. Your program
# may assume that a valid position will always be entered. It does not need to perform
# any error checking.

# row = int(input("Enter number 1 - 8"))
# Column = input("Enter letters from a - h")
# column = Column.lower()
#
# if (row % 2 != 0) and (column == "a"):
#     color = "Black"
# elif (row % 2 == 0) and (column == "b"):
#     color = "Black"
# elif (row % 2 != 0) and (column == "c"):
#     color = "Black"
# elif (row % 2 == 0) and (column == "d"):
#     color = "Black"
# elif (row % 2 != 0) and (column == "e"):
#     color = "Black"
# elif (row % 2 == 0) and (column == "f"):
#     color = "Black"
# elif (row % 2 != 0) and (column == "g"):
#     color = "Black"
# elif (row % 2 == 0) and (column == "h"):
#     color = "Black"
# else:
#     color = "White"
#
# print("{}{} has a {} square".format(column, row, color))


# Exercise 47: Season from Month and Day
# (Solved, 43 Lines)
# The year is divided into four seasons: spring, summer, fall (or autumn) and winter.
# While the exact dates that the seasons change vary a little bit from year to year
# because of the way that the calendar is constructed, we will use the following dates
# for this exercise:
# Season First Day
# Spring March 20
# Summer June 21
# Fall September 22
# Winter December 21
# Create a program that reads a month and day from the user. The user will
# enter the name of the month as a string, followed by the day within the month as an
# integer. Then your program should display the season associated with the date that
# was entered.

# day = int(input("Enter number of a holiday date"))
# Month = input("Enter month of a holiday date")
# month = Month.lower()
# if month == "march" and day == 20:
#     print("On {} {} is a {}".format(day, month, "Spring"))
# elif month == "june" and day == 21:
#     print("On {} {} is a {}".format(day, month, "Summer"))
# elif month == "september" and day == 22:
#     print("On {} {} is a {}".format(day, month, "Fall"))
# elif month == "december" and day == 21:
#     print("On {} {} is a {}".format(day, month, "Winter"))
# else:
#     print("entered month and day do not correspond to a season of the year.")


# Exercise 48: Birth Date to Astrological Sign
# (47 Lines)
# The horoscopes commonly reported in newspapers use the position of the sun at the
# time of one’s birth to try and predict the future. This system of astrology divides the
# year into twelve zodiac signs, as outline in the table below:
# Zodiac Sign Date Range
# Capricorn December 22 to January 19
# Aquarius January 20 to February 18
# Pisces February 19 to March 20
# Aries March 21 to April 19
# Taurus April 20 to May 20
# Gemini May 21 to June 20
# Cancer June 21 to July 22
# Leo July 23 to August 22
# Virgo August 23 to September 22
# Libra September 23 to October 22
# Scorpio October 23 to November 21
# Sagittarius November 22 to December 21
# Write a program that asks the user to enter his or her month and day of birth. Then
# your program should report the user’s zodiac sign as part of an appropriate output
# message.


# Exercise 49: Chinese Zodiac
# (Solved, 40 Lines)
# The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
# shown in the table below. The pattern repeats from there, with 2012 being another
# year of the dragon, and 1999 being another year of the hare.
# Year Animal
# 2000 Dragon
# 2001 Snake
# 2002 Horse
# 2003 Sheep
# 2004 Monkey
# 2005 Rooster
# 2006 Dog
# 2007 Pig
# 2008 Rat
# 2009 Ox
# 2010 Tiger
# 2011 Hare
# Write a program that reads a year from the user and displays the animal associated
# with that year. Your program should work correctly for any year greater than or equal
# to zero, not just the ones listed in the table.
# Exercise 50: Richter Scale
# (30 Lines)
# The following table contains earthquake magnitude ranges on the Richter scale and
# their descriptors:
# Magnitude Descriptor
# Less than 2.0 Micro
# 2.0 to less than 3.0 Very Minor
# 3.0 to less than 4.0 Minor
# 4.0 to less than 5.0 Light
# 5.0 to less than 6.0 Moderate
# 6.0 to less than 7.0 Strong
# 7.0 to less than 8.0 Major
# 8.0 to less than 10.0 Great
# 10.0 or more Meteoric
# Write a program that reads a magnitude from the user and displays the appropriate
# descriptor as part of a meaningful message. For example, if the user enters 5.5 then
# your program should indicate that a magnitude 5.5 earthquake is considered to be a
# moderate earthquake.


# Exercise 51: Roots of a Quadratic Function
# (24 Lines)
# A uni-variate quadratic function has the form f (x) = ax2 +bx +c, where a, b and c
# are constants, and a is non-zero. Its roots can be identified by finding the values of x
# that satisfy the quadratic equation ax2 + bx + c = 0. These values can be computed
# using the quadratic formula, shown below. A quadratic function may have 0, 1 or 2
# real roots.
# root = −b ± √b2−4ac
#       --------------
#             2a
# The portion of the expression under the square root sign is called the discriminant.
# If the discriminant is negative then the quadratic equation does not have any real
# roots. If the discriminant is 0, then the equation has one real root. Otherwise the
# equation has two real roots, and the expression must be evaluated twice, once using
# a plus sign, and once using a minus sign, when computing the numerator.
# Write a program that computes the real roots of a quadratic function.
# Your program should begin by prompting the user for the values of a, b and c. Then it should
# display a message indicating the number of real roots, along with the values of the
# real roots (if any).

# print("Nature of the quadratic equation is: ax2 + bx + c = 0")
# print("For equal roots try: 4x2 – 4x +  1")
# print("For different roots try: x2 – 6x +  5")
# print("You can try your own equations as well.")
# a = int(input("Enter value of a:"))
# b = int(input("Enter value of b:"))
# c = int(input("Enter value of c:"))
#
# root1 = (-b + math.sqrt((b**2) - (4 * a * c))) / 2
# root2 = (-b - math.sqrt((b**2) - (4 * a * c))) / 2
#
# if root1 == root2:
#     name = "roots are equal, hence equal to one root"
#     print(name)
#     print("root 1 = {}, and root 2 = {}".format(root1, root2))
# else:
#     name = "has two different roots"
#     print(name)
#     print("root 1 = {}, and root 2 = {}".format(root1, root2))


# Exercise 52: Letter Grade to Grade Points
# (Solved, 52 Lines)
# At a particular university, letter grades are mapped to grade points in the following
# manner:
# Letter Grade Points
# A+ 4.0
# A 4.0
# A- 3.7
# B+ 3.3
# B 3.0
# B- 2.7
# C+ 2.3
# C 2.0
# C- 1.7
# D+ 1.3
# D 1.0
# F 0
# Write a program that begins by reading a letter grade from the user. Then your
# program should compute and display the equivalent number of grade points. Ensure
# that your program generates an appropriate error message if the user enters an invalid
# letter grade.

# Letter = input("Enter a letter grade you have here:")
# letter = Letter.upper()
# words = ""
# marks = 0
#
# if letter == "A+":
#     marks = 4.0
# elif letter == "A":
#     marks = 4.0
# elif letter == "A-":
#     marks = 3.7
# elif letter == "B+":
#     marks = 3.3
# elif letter == "B":
#     marks = 3.0
# elif letter == "B-":
#     marks = 2.7
# elif letter == "C+":
#     marks = 2.3
# elif letter == "C":
#     marks = 2.0
# elif letter == "C-":
#     marks = 1.7
# elif letter == "D+":
#     marks = 1.3
# elif letter == "D":
#     marks = 1.0
# elif letter == "F":
#     marks = 0
# else:
#     words = "no such grades"
#
# print("You have {} points".format(marks))
# print(words)


# Exercise 53: Grade Points to Letter Grade
# (47 Lines)
# In the previous exercise you created a program that converted a letter grade into the
# equivalent number of grade points. In this exercise you will create a program that
# reverses the process and converts from a grade point value entered by the user to a
# letter grade. Ensure that your program handles grade point values that fall between
# letter grades. These should be rounded to the closest letter grade. Your program
# should report A+ if the value entered by the user is 4.0 or more.


# Exercise 54: Assessing Employees
# (Solved, 30 Lines)
# At a particular company, employees are rated at the end of each year. The rating scale
# begins at 0.0, with higher values indicating better performance and resulting in larger
# raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values
# between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated
# with each rating is shown in the following table. The amount of an employee’s raise
# is $2,400.00 multiplied by their rating.
# Rating Meaning
# 0.0 Unacceptable Performance
# 0.4 Acceptable Performance
# 0.6 or more Meritorious Performance
# Write a program that reads a rating from the user and indicates whether the performance
# for that rating is unacceptable, acceptable or meritorious. The amount
# of the employee’s raise should also be reported. Your program should display an
# appropriate error message if an invalid rating is entered.

# print("The known rates are:")
# print("0.0 Unacceptable Performance")
# print("0.4 Acceptable Performance")
# print("0.6 Meritorious Performance")
# print()
# rate = float(input("Due to services provided, please rate for the employee who served you:"))
# description = ""
# failure = ""
# amount = 2400.00
# doubled = amount * rate
#
# if rate == 0.0:
#     description = "Unacceptable Performance"
#     print("Employee rate is {} which gives you ${}".format(rate, doubled))
# elif rate == 0.4:
#     description = "Acceptable Performance"
#     print("Employee rate is {} which gives you ${}".format(rate, doubled))
# elif rate == 0.6:
#     description = "Meritorious Performance"
#     print("Employee rate is {} which gives you ${}".format(rate, doubled))
# else:
#     failure = "There is no such rating like that, here!"
#
# print(description)
# print(failure)


# Exercise 55:Wavelengths of Visible Light
# (38 Lines)
# The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
# spectrum is continuous, it is often divided into 6 colors as shown below:
# Color Wavelength (nm)
# Violet 380 to less than 450
# Blue 450 to less than 495
# Green 495 to less than 570
# Yellow 570 to less than 590
# Orange 590 to less than 620
# Red 620 to 750
# Write a program that reads a wavelength from the user and reports its color. Display
# an appropriate error message if the wavelength entered by the user is outside of the
# visible spectrum.

# print("""The wavelength of visible light ranges from 380 to 750 nanometers (nm).
#         While the spectrum is continuous, it is often divided into 6 colors.""")
#
# n = int(input("Enter the value from 380 - 750, above or below that shall be an error!"))
# color = ""
#
# if 380 <= n < 450:
#     color = "Violet"
# elif 450 <= n < 495:
#     color = "Blue"
# elif 495 <= n < 570:
#     color = "Green"
# elif 570 <= n < 590:
#     color = "Yellow"
# elif 590 <= n < 620:
#     color = "Orange"
# elif 620 <= n < 750:
#     color = "Red"
# else:
#     color = "Unknown color"
#
# print("it is: {}".format(color))


# Exercise 56: Frequency to Name
# (31 Lines)
# Electromagnetic radiation can be classified into one of 7 categories according to its
# frequency, as shown in the table below:
# Name Frequency Range (Hz)
# ---------------------------------------------------
# Radio Waves Less than 3 × 109
# Microwaves 3 × 109 to less than 3 × 1012
# Infrared Light 3 × 1012 to less than 4.3 × 1014
# Visible Light 4.3 × 1014 to less than 7.5 × 1014
# Ultraviolet Light 7.5 × 1014 to less than 3 × 1017
# X-Rays 3 × 1017 to less than 3 × 1019
# Gamma Rays 3 × 1019 or more
# ---------------------------------------------------
# Write a program that reads the frequency of some radiation from the user and
# displays name of the radiation as part of an appropriate message.

# print("The first value, example is: 3")
# print("The second value is a raised up to value, example is: ")
# print("Which gives, example is: 3 × 10^9")
# print()
# a = float(input("enter first value:"))
# b = float(input("enter second value:"))
# total = a * (10 ** b)
# name = ""
#
# if total < (3 * (10 ** 9)):
#     name = "Radio waves"
# elif (3 * (10 ** 9)) <= total < (3 * (10 ** 12)):
#     name = "Microwaves"
# elif (3 * (10 ** 12)) <= total < (4.3 * (10 ** 14)):
#     name = "Infrared Light"
# elif (4.3 * (10 ** 14)) <= total < (7.5 * (10 ** 14)):
#     name = "Visible Light"
# elif (7.5 * (10 ** 14)) <= total < (3 * (10 ** 17)):
#     name = "Ultraviolet Light"
# elif (3 * (10 ** 17)) <= total < (3 * (10 ** 19)):
#     name = "X-Rays"
# elif total >= (3 * (10 ** 19)):
#     name = "Gamma Rays"
# else:
#     name = "Error: Unknown Ray"
#
# print("This is, {}".format(name))


# Exercise 57: Cell Phone Bill
# (44 Lines)
# A particular cell phone plan includes 50 minutes of air time and 50 text messages
# for $15.00 a month. Each additional minute of air time costs $0.25, while additional
# text messages cost $0.15 each. All cell phone bills include an additional charge of
# $0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
# subject to 5 percent sales tax.
# Write a program that reads the number of minutes and text messages used in a
# month from the user. Display the base charge, additional minutes charge (if any),
# additional text message charge (if any), the 911 fee, tax and total bill amount. Only
# display the additional minute and text message charges if the user incurred costs in
# these categories. Ensure that all of the charges are displayed using 2 decimal places.

# base_charge = 15.00
# sms = 50
# calls = 50
# extra_call_charges = 0.25
# extra_sms_charges = 0.15
# sales_tax = 5 / 100
# emergency911 = 0.44
#
# monthly_sms = float(input("Enter number of text messages you used:"))
# monthly_calls = float(input("Enter number of calls you used:"))
#
# extra_call = monthly_calls - calls
# extra_sms = monthly_sms - sms
#
# extra_calls_cash = extra_call * extra_call_charges
# extra_sms_cash = extra_sms * extra_sms_charges
# tax = sales_tax * (extra_sms_cash + extra_calls_cash)
# total = tax + extra_calls_cash + extra_sms_cash + emergency911
# # Display the base charge, additional minutes charge (if any),
# # additional text message charge (if any), the 911 fee, tax and total bill amount.
# if monthly_sms > sms or monthly_calls > calls:
#     print("You used additional {}calls, and {}sms".format(extra_call, extra_sms))
#     print("You have also had ${:.2f}calls charges, ${:.2f}sms charges".format(extra_calls_cash, extra_sms_cash))
#     print("""with ${:.2f} base charge, with total charge of 911 ${:.2f},
#     and sales tax of ${:.2f}""".format(base_charge, emergency911, tax))
#     print("Total of all bill amount is: ${:.2f}".format(total))
# else:
#     print("You used additional {}calls, and {}sms".format(extra_call, extra_sms))
#     print("You have also had ${:.2f}calls charges, ${:.2f}sms charges".format(extra_calls_cash, extra_sms_cash))
#     print("""with ${:.2f} base charge, with total charge of 911 ${:.2f},
#     and sales tax of ${:.2f}""".format(base_charge, emergency911, tax))
#     print("Total of all bill amount is: ${:.2f}".format(total))


# Exercise 58: Is It a Leap Year?
# (Solved, 22 Lines)
# Most years have 365 days. However, the time required for the Earth to orbit the Sun
# is actually slightly more than that. As a result, an extra day, February 29, is included
# in some years to correct for this difference. Such years are referred to as leap years.
# The rules for determining whether or not a year is a leap year follow:
# • Any year that is divisible by 400 is a leap year.
# • Of the remaining years, any year that is divisible by 100 is not a leap year.
# • Of the remaining years, any year that is divisible by 4 is a leap year.
# • All other years are not leap years.
# Write a program that reads a year from the user and displays a message indicating
# whether or not it is a leap year.

# user = int(input("Enter an year"))
#
# if (user % 4 == 0) and (user % 100 != 0):
#     name = "This is a Leap year"
# elif (user % 100 == 0) and (user % 400 == 0):
#     name = "This is a Leap year"
# else:
#     name = "This is not a leap year"
#
# print(name)


# Exercise 59: Next Day
# (50 Lines)
# Write a program that reads a date from the user and computes its immediate successor.
# For example, if the user enters values that represent 2019-11-18 then your program
# should display a message indicating that the day immediately after 2019-11-18 is
# 2019-11-19. If the user enters values that represent 2019-11-30 then the program
# should indicate that the next day is 2019-12-01. If the user enters values that represent
# 2019-12-31 then the program should indicate that the next day is 2020-01-01. The
# date will be entered in numeric form with three separate input statements; one for
# the year, one for the month, and one for the day. Ensure that your program works
# correctly for leap years.


# Exercise 60:What Day of the Week Is January 1?
# (32 Lines)
# The following formula can be used to determine the day of the week for January 1
# in a given year:
# day_of_the_week = (year + floor((year − 1) / 4) − floor((year − 1) / 100) +
# floor((year − 1) / 400)) % 7
# The result calculated by this formula is an integer that represents the day of the
# week. Sunday is represented by 0. The remaining days of the week following in
# sequence through to Saturday, which is represented by 6.
# Use the formula above to write a program that reads a year from the user and
# reports the day of the week for January 1 of that year. The output from your program
# should include the full name of the day of the week, not just the integer returned by
# the formula.


# Exercise 61: Is a License Plate Valid?
# (Solved, 28 Lines)
# In a particular jurisdiction, older license plates consist of three uppercase letters
# followed by three digits. When all of the license plates following that pattern had
# been used, the format was changed to four digits followed by three uppercase letters.
# Write a program that begins by reading a string of characters from the user. Then
# your program should display a message indicating whether the characters are valid
# for an older style license plate or a newer style license plate. Your program should
# display an appropriate message if the string entered by the user is not valid for either
# style of license plate.


# Exercise 62: Roulette Payouts
# (Solved, 45 Lines)
# A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
# are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
# 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
# between 1 and 36 are used to number the black spaces.
# Many different bets can be placed in roulette. We will only consider the following
# subset of them in this exercise:
# • Single number (1 to 36, 0, or 00)
# • Red versus Black
# • Odd versus Even (Note that 0 and 00 do not pay out for even)
# • 1 to 18 versus 19 to 36
# Write a program that simulates a spin of a roulette wheel by using Python’s
# random number generator. Display the number that was selected and all of the bets
# that must be payed. For example, if 13 is selected then your program should display:
# The spin resulted in 13...
# Pay 13
# Pay Black
# Pay Odd
# Pay 1 to 18
# If the simulation results in 0 or 00 then your program should display Pay 0
# or Pay 00 without any further output.
