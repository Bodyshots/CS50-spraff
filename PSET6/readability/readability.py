from cs50 import get_string
import re

# Prompting text input from user
Input = get_string("Text: ")

Length = len(Input)
# Counting number of sentences
NumberofSentences = Input.count(".") + Input.count("?") + Input.count("!")

# Counting number of Letters
i = 0
NumberofLetters = 0
for i in range(Length):
    if Input[i].isalpha() == True:
        NumberofLetters += 1
    
# Counting number of Words
NumberofWords = Input.count(" ") + 1

# Using Coleman-Liau Index Formula
index = 0.0588 * (100 * NumberofLetters / NumberofWords) - 0.296 * (100 * NumberofSentences / NumberofWords) - 15.8

# Stating Grade Levels
grade = round(index)
if (grade <= 0):
    print("Before Grade 1")
elif (grade >= 16):
    print("Grade 16+")
else:
    print(f"Grade {grade}")