#include<stdio.h>

int main(void){
    int i = 5, j = 9;

    printf("%d & %d = %d\n", i, j, i&j);
    printf("%d | %d = %d\n", i, j, i|j);
    printf("%d ^ %d = %d\n", i, j, i^j);
    printf("~%d = %d\n", i, ~i);

    return 0;
}