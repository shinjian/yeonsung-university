#include<stdio.h>

int main(void){
    char n = 128;
    char x = -129;
    unsigned char m = 256;
    unsigned char y = -1;

    printf(" 128 = %d (char type)\n", n);
    printf(" 256 = %d (unsigned char type)\n", m);
    printf(" -129 = %d (char type)\n", x);
    printf(" -1 = %d (unsigned char type)\n", y);

    return 0;
}