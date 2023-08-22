#include <stdio.h>

int main(int argc, char **argv)
{
    int a,b,m;
    scanf("%d %d",&a, &b);
    m = (a*60 + b) - 45;
    if (m < 0)
        m += 24*60;

    printf("%d %d",m/60, m%60);
}