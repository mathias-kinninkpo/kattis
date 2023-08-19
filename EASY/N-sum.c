#include <stdio.h>

int main(int argc, char **argv){
    int i , n , sum = 0, num;

    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&num);
        sum += num;
    }
    printf("%d",sum);
}