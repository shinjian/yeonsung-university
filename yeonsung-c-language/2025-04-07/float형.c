#include<stdio.h>

int main(void){
    float x = 3.40282e38;
    float y = 1.17549e-38;

    printf("x = %30.25e\n", x);
    printf("y = %30.25e\n", y);

    x *= 100;

    printf("x = %30.25e\n", x);

    y /= 1000; printf("y = %30.25e\n", y);
    y /= 1000; printf("y = %30.25e\n", y);
    y /= 1000; printf("y = %30.25e\n", y);

    return 0;
}