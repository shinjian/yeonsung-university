#include<stdio.h>

int main(void){
    char ch;
    int num;
    double x;

    printf("char형의 바이트 크기: %lu\n", sizeof(char));
    printf("short형의 바이트 크기: %lu\n", sizeof(short));
    printf("int형의 바이트 크기: %lu\n", sizeof(int));
    printf("long형의 바이트 크기: %lu\n", sizeof(long));
    printf("long long형의 바이트 크기: %lu\n", sizeof(long long));
    printf("float형의 바이트 크기: %lu\n", sizeof(float));
    printf("double형의 바이트 크기: %lu\n", sizeof(double));
    printf("long double형의 바이트 크기: %lu\n", sizeof(long double));

    printf("ch형의 바이트 크기: %lu\n", sizeof(ch));
    printf("num형의 바이트 크기: %lu\n", sizeof(num));
    printf("x형의 바이트 크기: %lu\n", sizeof(x));
}