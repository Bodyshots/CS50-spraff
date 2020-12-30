#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h, r, c, space;
    do
    {
        h = get_int("Height: ");
    }
    while (h < 1 || h > 8);
    for (r = 0; r < h; r++)
    {
        for (space = 0; space < h - r - 1; space++)
        {
            printf(" ");
        }
        for (c = 0; c <= r; c++)
        {
            printf("#");
        }
        printf("\n");
    }
}