# Exercise 110: Sorted Order(Solved, 22 Lines)
# Write a program that reads integers from the user and stores them in a list. Your
# program should continue reading values until the user enters 0. Then it should display
# all of the values entered by the user (except for the 0) in ascending order, with one
# value appearing on each line. Use either the sort method or the sorted function
# to sort the list.


# Exercise 111: Reverse Order (20 Lines)
#  Write a program that reads integers from the user and stores them in a list. Use 0 as
#  a sentinel value to mark the end of the input. Once all of the values have been read
#  your program should display them (except for the 0) in reverse order, with one value
#  appearing on each line.


# Exercise 112: Remove Outliers
# (Solved, 44 Lines)
# When analysing data collected as part of a science experiment it may be desirable
# to remove the most extreme values before performing other calculations. Write a
# function that takes a list of values and an non-negative integer, n, as its parameters.
# The function should create a new copy of the list with the n largest elements and the
# n smallest elements removed. Then it should return the new copy of the list as the
# function’s only result. The order of the elements in the returned list does not have to
# match the order of the elements in the original list.
# Write a main program that demonstrates your function. It should read a list of
# numbers from the user and remove the two largest and two smallest values from it by
# calling the function described previously. Display the list with the outliers removed,
# followed by the original list. Your program should generate an appropriate error
# message if the user enters less than 4 values.


# Exercise 113: Avoiding Duplicates
# (Solved, 21 Lines)
# In this exercise, you will create a program that reads words from the user until the
# user enters a blank line. After the user enters a blank line your program should display each word entered by the user exactly once. The words should be displayed in
# the same order that they were first entered. For example, if the user enters:
# first
# second
# first
# third
# second
# then your program should display:
# first
# second
# third


# Exercise 114: Negatives, Zeros and Positives
# (Solved, 36 Lines)
# Create a program that reads integers from the user until a blank line is entered. Once
# all of the integers have been read your program should display all of the negative
# numbers, followed by all of the zeros, followed by all of the positive numbers. Within
# each group the numbers should be displayed in the same order that they were entered
# by the user. For example, if the user enters the values 3, -4, 1, 0, -1, 0, and -2 then
# your program should output the values -4, -1, -2, 0, 0, 3, and 1. Your program
# should display each value on its own line.


# Exercise 115: List of Proper Divisors
# (36 Lines)
# A proper divisor of a positive integer, n, is a positive integer less than n which divides
# evenly into n. Write a function that computes all of the proper divisors of a positive
# integer. The integer will be passed to the function as its only parameter. The function
# will return a list containing all of the proper divisors as its only result. Complete
# this exercise by writing a main program that demonstrates the function by reading
# a value from the user and displaying the list of its proper divisors. Ensure that your
# main program only runs when your solution has not been imported into another file.


# Exercise 116: Perfect Numbers
# (Solved, 35 Lines)
# An integer, n, is said to be perfect when the sum of all of the proper divisors of n is
# equal to n. For example, 28 is a perfect number because its proper divisors are 1, 2,
# 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.
# Write a function that determines whether or not a positive integer is perfect. Your
# function will take one parameter. If that parameter is a perfect number then your
# function will return True. Otherwise it will return False. In addition, write a main
# program that uses your function to identify and display all of the perfect numbers
# between 1 and 10,000. Import your solution to Exercise 115 when completing this
# task.


# Exercise 117: Only the Words
# (38 Lines)
# In this exercise you will create a program that identifies all of the words in a
# string entered by the user. Begin by writing a function that takes a string as
# its only parameter. Your function should return a list of the words in the string
# with the punctuation marks at the edges of the words removed.
# The punctuation marks that you must consider include commas, periods, question marks,
# hyphens, apostrophes, exclamation points, colons, and semicolons. Do not remove
# punctuation marks that appear in the middle of a word, such as the apostrophes
# used to form a contraction. For example, if your function is provided with the
# string "Contractions include: don’t, isn’t, and wouldn’t."
# then your function should return the list ["Contractions", "include",
# "don’t", "isn’t", "and", "wouldn’t"].
# Write a main program that demonstrates your function. It should read a string from
# the user and then display all of the words in the string with the punctuation marks
# removed. You will need to import your solution to this exercise when completing
# Exercises 118 and 167. As a result, you should ensure that your main program only
# runs when your file has not been imported into another program.


# Exercise 118:Word by Word Palindromes
# (34 Lines)
# Exercises 75 and 76 previously introduced the notion of a palindrome. Such palindromes
# examined the characters in a string, possibly ignoring spacing and punctuation marks,
# to see if the string was the same forwards and backwards. While
# palindromes are most commonly considered character by character, the notion of
# a palindrome can be extended to larger units. For example, while the sentence “Is
# it crazy how saying sentences backwards creates backwards sentences saying how
# crazy it is?” isn’t a character by character palindrome, it is a palindrome when examined
# a word at a time (and when capitalization and punctuation are ignored). Other
# examples of word by word palindromes include “Herb the sage eats sage, the herb”
# and “Information school graduate seeks graduate school information”.
# Create a program that reads a string from the user. Your program should report
# whether or not the entered string is a word by word palindrome. Ignore spacing and
# punctuation when determining the result.


# Exercise 119: Below and Above Average
# (44 Lines)
# Write a program that reads numbers from the user until a blank line is entered. Your
# program should display the average of all of the values entered by the user. Then
# the program should display all of the below average values, followed by all of the
# average values (if any), followed by all of the above average values. An appropriate
# label should be displayed before each list of values.


# Exercise 120: Formatting a List
# (Solved, 41 Lines)
# When writing out a list of items in English, one normally separates the items with
# commas. In addition, the word “and” is normally included before the last item, unless
# the list only contains one item. Consider the following four lists:
# apples
# apples and oranges
# apples, oranges and bananas
# apples, oranges, bananas and lemons
# Write a function that takes a list of strings as its only parameter. Your function
# should return a string that contains all of the items in the list, formatted in the manner
# described previously, as its only result. While the examples shown previously only
# include lists containing four elements or less, your function should behave correctly
# for lists of any length. Include a main program that reads several items from the user,
# formats them by calling your function, and then displays the result returned by the
# function.


# Exercise 121: Random Lottery Numbers
# (Solved, 28 Lines)
# In order to win the top prize in a particular lottery, one must match all 6 numbers
# on his or her ticket to the 6 numbers between 1 and 49 that are drawn by the lottery
# organizer. Write a program that generates a random selection of 6 numbers for a
# lottery ticket. Ensure that the 6 numbers selected do not contain any duplicates.
# Display the numbers in ascending order.


# Exercise 122: Pig Latin
# (32 Lines)
# Pig Latin is a language constructed by transforming English words. While the ori
# gins of the language are unknown, it is mentioned in at least two documents from
# the nineteenth century, suggesting that it has existed for more than 100 years. The
# following rules are used to translate English into Pig Latin:
# • If the word begins with a consonant (including y), then all letters at the beginning of
# the word, up to the first vowel (excluding y), are removed and then added to the end
# of the word, followed by ay. For example, computer becomes omputercay
# and think becomes inkthay.
# • If the word begins with a vowel (not including y), then way is added to the end
# of the word. For example, algorithm becomes algorithmway and office
# becomes officeway.
# Write a program that reads a line of text from the user. Then your program should
# translate the line into Pig Latin and display the result. You may assume that the string
# entered by the user only contains lowercase letters and spaces.


# Exercise 123: Pig Latin Improved
# (51 Lines)
# Extend your solution to Exercise 122 so that it correctly handles uppercase letters and
# punctuation marks such as commas, periods, question marks and exclamation marks.
# If an English word begins with an uppercase letter then its Pig Latin representation
# should also begin with an uppercase letter and the uppercase letter moved to the end of
# the word should be changed to lowercase. For example, Computer should become
# Omputercay. If a word ends in a punctuation mark then the punctuation mark
# should remain at the end of the word after the transformation has been performed.
# For example, Science! should become Iencescay!.


# Exercise 124: Line of Best Fit
# (41 Lines)
# A line of best fit is a straight line that best approximates a collection of n data points.
# In this exercise, we will assume that each point in the collection has an x coordinate
# and a y coordinate. The symbols x¯ and y¯ are used to represent the average x value in
# the collection and the average y value in the collection respectively. The line of best
# fit is represented by the equation y = mx + b where m and b are calculated using
# the following formulas:
# m = summation(x y) − summation( x) summation( y)
#                      ---------------------------
#                                  n
# summation(x2) − summation(squareroot(x))
#                 ------------------------
#                          n
#    --    --
# b = y − mx
# Write a program that reads a collection of points from the user. The user will enter
# the first x coordinate on its own line, followed by the first y coordinate on its own
# line. Allow the user to continue entering coordinates, with the x and y values each
# entered on their own line, until your program reads a blank line for the x coordinate.
# Display the formula for the line of best fit in the form y = mx + b by replacing m
# and b with the values calculated by the preceding formulas. For example, if the user
# inputs the coordinates (1, 1), (2, 2.1) and (3, 2.9) then your program should display
# y = 0.95x + 0.1.


# Exercise 125: Shuffling a Deck of Cards
# (Solved, 49 Lines)
# A standard deck of playing cards contains 52 cards. Each card has one of four suits
# along with a value. The suits are normally spades, hearts, diamonds and clubs while
# the values are 2 through 10, Jack, Queen, King and Ace.
# Each playing card can be represented using two characters. The first character is
# the value of the card, with the values 2 through 9 being represented directly. The
# characters “T”, “J”, “Q”, “K” and “A” are used to represent the values 10, Jack,
# Queen, King and Ace respectively. The second character is used to represent the suit
# of the card. It is normally a lowercase letter: “s” for spades, “h” for hearts, “d” for
# diamonds and “c” for clubs. The following table provides several examples of cards
# and their two-character representations.
# 5.5 Exercises 89
# Card Abbreviation
# Jack of spades Js
# Two of clubs 2c
# Ten of diamonds Td
# Ace of hearts Ah
# Nine of spades 9s
# Begin by writing a function named createDeck. It will use loops to create a
# complete deck of cards by storing the two-character abbreviations for all 52 cards
# into a list. Return the list of cards as the function’s only result. Your function will
# not require any parameters.
# Write a second function named shuffle that randomizes the order of the cards
# in a list. One technique that can be used to shuffle the cards is to visit each element
# in the list and swap it with another random element in the list. You must write your
# own loop for shuffling the cards. You cannot make use of Python’s built-in shuffle
# function.
# Use both of the functions described in the previous paragraphs to create a main
# program that displays a deck of cards before and after it has been shuffled. Ensure
# that your main program only runs when your functions have not been imported into
# another file.
# A good shuffling algorithm is unbiased, meaning that every different arrangement of the elements is equally probable when the algorithm completes. While
# the approach described earlier in this problem suggested visiting each element
# in sequence and swapping it with an element at a random index, such an algorithm is biased. In particular, elements that appear later in the original list are
# more likely to end up later in the shuffled list. Counterintuitively, an unbiased
# shuffle can be achieved by visiting each element in sequence and swapping it
# to a random index between the position of the current element and the end of
# the list instead of randomly selecting any index.


# Exercise 126: Dealing Hands of Cards
# (44 Lines)
# In many card games each player is dealt a specific number of cards after the deck
# has been shuffled. Write a function, deal, which takes the number of hands, the
# number of cards per hand, and a deck of cards as its three parameters. Your function
# should return a list containing all of the hands that were dealt. Each hand will be
# represented as a list of cards.
# When dealing the hands, your function should modify the deck of cards passed
# to it as a parameter, removing each card from the deck as it is added to a player’s
# hand. When cards are dealt, it is customary to give each player a card before any
# player receives an additional card. Your function should follow this custom when
# constructing the hands for the players.
# Use your solution to Exercise 125 to help you construct a main program that
# creates and shuffles a deck of cards, and then deals out four hands of five cards each.
# Display all of the hands of cards, along with the cards remaining in the deck after
# the hands have been dealt.


# Exercise 127: Is a List already in Sorted Order?
# (41 Lines)
# Write a function that determines whether or not a list of values is in sorted order
# (either ascending or descending). The function should return True if the list is
# already sorted. Otherwise it should return False. Write a main program that reads
# a list of numbers from the user and then uses your function to report whether or not
# the list is sorted.
# Make sure you consider these questions when completing this exercise: Is a
# list that is empty in sorted order? What about a list containing one element?


# Exercise 128: Count the Elements
# (Solved, 48 Lines)
# Python’s standard library includes a method named count that determines how
# many times a specific value occurs in a list. In this exercise, you will create a new
# function named countRange. It will determine and return the number of elements
# within a list that are greater than or equal to some minimum value and less than some
# maximum value. Your function will take three parameters: the list, the minimum
# value and the maximum value. It will return an integer result greater than or equal to
# 0. Include a main program that demonstrates your function for several different lists,
# minimum values and maximum values. Ensure that your program works correctly
# for both lists of integers and lists of floating-point numbers.


# Exercise 129: Tokenizing a String
# (Solved, 47 Lines)
# Tokenizing is the process of converting a string into a list of substrings, known as
# tokens. In many circumstances, a list of tokens is far easier to work with than the
# original string because the original string may have irregular spacing. In some cases
# substantial work is also required to determine where one token ends and the next one
# begins.
# In a mathematical expression, tokens are items such as operators, numbers and
# parentheses. The operator symbols that we will consider in this (and subsequent)
# problems are *, /, ˆ, - and +. Operators and parentheses are easy to identify because
# the token is always a single character, and the character is never part of another token.
# Numbers are slightly more challenging to identify because the token may consist of
# multiple characters. Any sequence of consecutive digits should be treated as one
# number token.
# Write a function that takes a string containing a mathematical expression as its
# only parameter and breaks it into a list of tokens. Each token should be a parenthesis,
# an operator, or a number. (For simplicity we will only work with integers in this
# problem). Return the list of tokens as the function’s only result.
# You may assume that the string passed to your function always contains a valid
# mathematical expression consisting of parentheses, operators and integers. However,
# your function must handle variable amounts of whitespace (including no whitespace)
# between these elements. Include a main program that demonstrates your tokenizing
# function by reading an expression from the user and printing the list of tokens. Ensure
# that the main program will not run when the file containing your solution is imported
# into another program.


# Exercise 130: Unary and Binary Operators
# (Solved, 45 Lines)
# Some mathematical operators are unary while others are binary. Unary operators act
# on one value while binary operators act on two. For example, in the expression 2 *
# -3 the * is a binary operator because it acts on both the 2 and the −3 while the - is
# a unary operator because it only acts on the 3.
# An operator’s symbol is not always sufficient to determine whether it is unary or
# binary. For example, while the - operator was unary in the previous expression, the
# same character is used to represent the binary - operator in an expression such as
# 2-3. This ambiguity, which is also present for the + operator, must be removed
# before other interesting operations can be performed on a list of tokens representing
# a mathematical expression.
# Create a function that identifies unary + and - operators in a list of tokens and
# replaces them with u+ and u- respectively. Your function will take a list of tokens
# for a mathematical expression as its only parameter and return a new list of tokens
# where the unary + and - operators have been substituted as its only result. A +
# or - operator is unary if it is the first token in the list, or if the token that immediately
# precedes it is an operator or open parenthesis. Otherwise the operator is
# binary.
# Write a main program that demonstrates that your function works correctly by
# reading, tokenizing, and marking the unary operators in an expression entered by
# the user. Your main program should not execute when your function is imported into
# another program.


# Exercise 131: Infix to Postfix
# (63 Lines)
# Mathematical expressions are often written in infix form, where operators appear
# between the operands on which they act. While this is a common form, it is also
# possible to express mathematical expressions in postfix form, where the operator
# appears after all of its operands. For example, the infix expression 3+4 is written
# as 34+ in postfix form. One can convert an infix expression to postfix form using
# the following algorithm:
# Create a new empty list, operators
# Create a new empty list, postfix
# For each token in the infix expression
# If the token is an integer then
# Append the token to postfix
# If the token is an operator then
# While operators is not empty and
# the last item in operators is not an open parenthesis and
# precedence(token) < precedence(last item in operators) do
# Remove the last item from operators and append it to postfix
# Append the token to operators
# If the token is an open parenthesis then
# Append the token to operators
# If the token is a close parenthesis then
# While the last item in operators is not an open parenthesis do
# Remove the last item from operators and append it to postfix
# Remove the open parenthesis from operators
# While operators is not the empty list do
# Remove the last item from operators and append it to postfix
# Return postfix as the result of the algorithm
# Use your solutions to Exercises 129 and 130 to tokenize a mathematical expression
# and identify any unary operators in it. Then use the algorithm above to transform the
# expression from infix form to postfix form. Your code that implements the preceding
# algorithm should reside in a function that takes a list of tokens representing an
# infix expression (with the unary operators marked) as its only parameter. It should
# return a list of tokens representing the equivalent postfix expression as its only result.
# Include a main program that demonstrates your infix to postfix function by reading
# an expression from the user in infix form and displaying it in postfix form.
# The purpose of converting from infix form to postfix form will become apparent
# when you read Exercise 132. You may find your solutions to Exercises 96 and 97
# helpful when completing this problem. While you should be able to use your solution
# to Exercise 96 without any modifications, your solution to Exercise 97 will need to
# be extended so that it returns the correct precedence for the unary operators. The
# unary operators should have higher precedence than multiplication and division, but
# lower precedence than exponentiation.


# Exercise 132: Evaluate Postfix
# (63 Lines)
# Evaluating a postfix expression is easier than evaluating an infix expression because
# it does not contain any parentheses and there are no operator precedence rules to
# consider. A postfix expression can be evaluated using the following algorithm:
# Create a new empty list, values
# For each token in the postfix expression
# If the token is a number then
# Convert it to an integer and append it to values
# Else if the token is a unary minus then
# Remove an item from the end of values
# Negate the item and append the result of the negation to values
# Else if the token is a binary operator then
# Remove an item from the end of values and call it right
# Remove an item from the end of values and call it left
# Compute the result of applying the operator to left and right
# Append the result to values
# Return the first item in values as the value of the expression
# Write a program that reads a mathematical expression in infix form from the user,
# converts it to postfix form, evaluates it, and displays its value. Use your solutions
# to Exercises 129, 130 and 131, along with the algorithm shown above, to solve this
# problem.
# The algorithms provided in Exercises 131 and 132 do not perform any error
# checking. As a result, your programs may crash or generate incorrect results if
# you provide them with invalid input. The algorithms presented in these exercises can be extended to detect invalid input and respond to it in a reasonable
# manner. Doing so is left as an independent study exercise for the interested
# student.


# Exercise 133: Does a List Contain a Sublist?
# (44 Lines)
# A sublist is a list that is part of a larger list. A sublist may be a list containing a
# single element, multiple elements, or even no elements at all. For example, [1],
# [2], [3] and [4] are all sublists of [1, 2, 3, 4]. The list [2, 3] is also a
# sublist of [1, 2, 3, 4], but [2, 4] is not a sublist [1, 2, 3, 4] because
# the elements 2 and 4 are not adjacent in the longer list. The empty list is a sublist of
# any list. As a result, [] is a sublist of [1, 2, 3, 4]. A list is a sublist of itself,
# meaning that [1, 2, 3, 4] is also a sublist of [1, 2, 3, 4].
# In this exercise you will create a function, isSublist, that determines whether
# or not one list is a sublist of another. Your function should take two lists, larger
# and smaller, as its only parameters. It should return True if and only if smaller
# is a sublist of larger. Write a main program that demonstrates your function.


# Exercise 134: Generate All Sublists of a List
# (Solved, 41 Lines)
# Using the definition of a sublist from Exercise 133, write a function that returns a
# list containing every possible sublist of a list. For example, the sublists of [1, 2,
# 3] are [], [1], [2], [3], [1, 2], [2, 3] and [1, 2, 3]. Note that your
# function will always return a list containing at least the empty list because the empty
# list is a sublist of every list. Include a main program that demonstrate your function
# by displaying all of the sublists of several different lists.


# Exercise 135: The Sieve of Eratosthenes
# (Solved, 33 Lines)
# The Sieve of Eratosthenes is a technique that was developed more than 2,000 years
# ago to easily find all of the prime numbers between 2 and some limit, say 100. A
# description of the algorithm follows:
# Write down all of the numbers from 0 to the limit
# Cross out 0 and 1 because they are not prime
# Set p equal to 2
# While p is less than the limit do
# Cross out all multiples of p (but not p itself)
# Set p equal to the next number in the list that is not crossed out
# Report all of the numbers that have not been crossed out as prime
# The key to this algorithm is that it is relatively easy to cross out every nth number
# on a piece of paper. This is also an easy task for a computer—a for loop can simulate
# this behavior when a third parameter is provided to the range function. When a
# number is crossed out, we know that it is no longer prime, but it still occupies space
# on the piece of paper, and must still be considered when computing later prime
# numbers. As a result, you should not simulate crossing out a number by removing
# it from the list. Instead, you should simulate crossing out a number by replacing it
# with 0. Then, once the algorithm completes, all of the non-zero values in the list are
# prime.


# 5.5 Exercises 95
# Create a Python program that uses this algorithm to display all of the prime
# numbers between 2 and a limit entered by the user. If you implement the algorithm
# correctly you should be able to display all of the prime numbers less than 1,000,000
# in a few seconds.
# This algorithm for finding prime numbers is not Eratosthenes’ only claim to
# fame. His other noteworthy accomplishments include calculating the circumference of the Earth and the tilt of the Earth’s axis. He also served as the Chief
# Librarian at the Library of Alexandria.
