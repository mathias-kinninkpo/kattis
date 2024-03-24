#include <stdio.h>

int main(){
    // declaration
    char tab[10];
    int n, i;
    scanf("%s", &tab);
    scanf("%d", &n);
    for (i=0; i < n; i++){
        printf("%s", tab);
    }
    return (0);
}