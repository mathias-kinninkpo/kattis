#include <stdio.h>

int main(int argc, char **argv){
    int mul = 1, i, j;

    for( i = 0; i < 3; i++){
        scanf("%d", &j);
        mul *= j;
    }
    printf("%d", mul);
}