#include<stdio.h>

int main(void){
    int a = 123, c = 0;
    double b = 0;

    printf(" a = %d\n", a);
    printf(" a = %d\n", a = 456);
    printf(" b = %f\n", b = a + 0.5);
    printf(" c = %d\n", c = printf("ABC\n"));

    return 0;
}