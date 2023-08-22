#include <stdio.h>

/**
 * Affichage des indexes dont la leur valeur est
 * differente de -1
 */

int main(int argc, char **argv)
{
    int tab[101][101], n, sum = 0;
    scanf("%d", &n);
    for (int i = 0; i < n ; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &tab[i][j]);
            if (tab[i][j] != -1){
                sum += 1;
            }
        }
    }
    printf("%d\n", sum);

    for (int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if (tab[i][j] != -1)
            {
                printf("%d %d %d\n", i+1, j+1, tab[i][j]);
            }
        }
    }
}