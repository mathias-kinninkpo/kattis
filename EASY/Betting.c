#include <stdio.h>

int main(int argc, char **argv)
{
    float n;
    scanf("%f", &n);
    printf("%f\n%f", (0.5/(n/100)) * 2, (0.5/((100-n)/100))*2);
}