#include<stdio.h>

int main(void){
    float weight;
    int age;
    char sex;

    printf("체중, 나이, 성별(M/F) 순으로 입력하세요.\n");
    scanf("%f %d %c", &weight, &age, &sex);

    printf("체중 : %.1f\n", weight);
    printf("나이 : %d\n", age);
    printf("성별(M/F) : %c\n", sex);

    return 0;
}