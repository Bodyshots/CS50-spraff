//Caesar

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //Makes sure 2nd idea is inputted
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    //Checks every character
    int n = strlen(argv[1]);
    for (int i = 0; i < n; i++)
    {
        //Checks if each character is a digit
        if (!isdigit(argv[1][i]))
        {
            printf("Usage ./caesar key\n");
            return 1;
        }
    }
    //Converting digit (string) into integer
    int k = atoi(argv[1]);
    //Telling to input text to encipher
    string s = get_string("plaintext: ");
    
    printf("ciphertext: ");
    for (int j = 0, m = strlen(s); j < m; j++) //WATCH OUT FOR RETURN CODE. IF FOR LOOP DOESN'T WORK THAT'S PROBABLY WHY!!!!!!!!!!!!!
    {
        char c = s[j];
        if (isupper(c))
        {
            char a = 'A';
            printf("%c", (((c - a) + k) % 26) + a);
        }
        else if (islower(c))
        {
            char a = 'a';
            printf("%c", (((c - a) + k) % 26) + a);
        }
        else
        {
            printf("%c", c);
        }
    }
    printf("\n");
}
