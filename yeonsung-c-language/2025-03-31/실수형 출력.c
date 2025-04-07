#include<stdio.h>

int main(void){
    float x = 12.34567;

    printf("%f\n", x);
    printf("%.2f\n", x);
    printf("%8.2f\n", x);
    printf("%08.2f\n", x);

    printf("%e\n", x);
    printf("%.2e\n", x);
    printf("%16.2e\n", x);
    printf("%016.2e\n", x);

    return 0;
}