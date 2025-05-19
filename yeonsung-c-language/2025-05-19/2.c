#include<stdio.h>

void main(){
    int i = 4, j = 9, min = 0;

    i > j ? printf("%d가 %d 보다 크다\n", i, j) : printf("%d가 %d 보다 작거나 같다\n", i, j);

    min = i < j ? i : j;

    printf("%d와 %d 중 작은 수는 %d이다\n", i, j, min);

    return;
}