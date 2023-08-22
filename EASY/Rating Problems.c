#include <stdio.h>

int main(int argc, char **argv)
{
    float a,b,i,s=0,r;
    scanf("%f %f",&a, &b);
    for (i=0; i<b; i++)
    {
        scanf("%f",&r);
        s += r;
    }
    printf("%f %f",(((a-b)*-3)+s)/a,(((a-b)*3)+s)/a);
}