#include<stdio.h>

int main(void){
    int i = 0;

    printf("while 구문을 이용한 출력");

    while (i < 10)
    {
        printf("%d", i);
        i += 1;
    }
    printf("\n");

    printf("for 구문을 이용한 출력");
    for (i = 0; i < 10; i++){
        printf("%d", i);
    }

    return 0;
}