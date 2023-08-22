#include <stdio.h>


/**
 * Verifier si une somme est divisible par 11
 * @chaine : char of ten digits
 * 
 */

int main(int argc, char **argv)
{
    int coef[10] = {4, 3, 2, 7, 6, 5, 4, 3, 2,1}, integer, sum = 0, i=0,c=0;
    char chaine[12];
    scanf("%s", chaine);
    
    while (chaine[i] != '\0')
    {
        if (chaine[i] != '-')
        {
            integer = chaine[i] - '0';
            sum += (integer * coef[c]);
            c++;
            
        }
        i++;
    }
    if (sum%11 == 0)
        putchar('1');
    else
        putchar('0');
    

}