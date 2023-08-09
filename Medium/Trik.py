#include <stdio.h>
#include <stdlib.h>
int move (int x, char y)
{
    if (x == 1){
        if (y == 'A') return 2;
        else if (y == 'B') return 1;
        else return 3;
    }
    if (x == 2){
        if (y == 'A') return 1;
        else if (y == 'B') return 3;
        else return 2;
    }
    if (x == 3){
        if (y == 'A') return 3;
        else if (y == 'B') return 2;
        else return 1;
    }
}

int main()
{
    char *tab;
    int position = 1, i = 0;
    tab = (char *)malloc(sizeof(char)*50);
    scanf("%s", tab);
    while (tab)
    {
        position = move(position,tab[i]);
        i++;
    }
    printf("%d", position);
}