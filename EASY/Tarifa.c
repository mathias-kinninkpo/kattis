#include <stdio.h>

int main(int argc, char **argv)
{
    int a,b,p,s=0,i;
    scanf("%d",&a);
    scanf("%d",&b);
    for (p=0; p<b; p++)
    {
        scanf("%d",&i);
        s += (a-i);
    }
    printf("%d",s+a);
}