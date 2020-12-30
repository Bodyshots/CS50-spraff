//Read Writing pls

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main(void)
{
    //Prompting for text input from user
    string Input = get_string("Enter your text here: ");
    
    //Counter for number of letters, words, and sentences
    int NumberOfLetters = 0;
    int NumberOfWords = 1;
    int NumberOfSentences = 0;
    
    //Determining length of string
    int Length = strlen(Input);
    
    //Counting Number of Letters and Sentences
    for (int i = 0; i < Length; i++)
    {
        //Alphabet or not
        if (isalpha(Input[i]))
        {
            NumberOfLetters++;
        }
        if (i > 0 && (Input[i] == '?' || Input[i] == '!' || Input[i] == '.'))
        {
            NumberOfSentences++;
        }
    }
    //Determining number of words
    for (int i = 1; i < Length; i++)
    {
        if (isspace(Input[i]))
        {
            NumberOfWords++;
        }
    }
    //Using Coleman-Liau Index Formula
    float index = 0.0588 * (100 * (float) NumberOfLetters / (float) NumberOfWords) - 0.296 * (100 * (float) NumberOfSentences /
                  (float) NumberOfWords) - 15.8;

    //Stating Grade Levels    
    int grade = round(index);
    {
        if (grade <= 0)
        {
            printf("Before Grade 1");
        }
        else if (grade >= 16)
        {
            printf("Grade 16+");
        }
        else
        {
            printf("Grade %i", grade);
        }
    }
    printf("\n");
}