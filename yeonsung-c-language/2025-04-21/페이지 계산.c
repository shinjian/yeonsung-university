#include<stdio.h>

int main(void){
    int items = 0, pages = 0, left = 0;
    int items_per_page = 0;

    printf("항목수? ");
    scanf("%d", &items);

    printf("한 페이지 당 항목수? ");
    scanf("%d", &items_per_page);

    pages = items / items_per_page;
    left = items % items_per_page;

    printf("%d 페이지와 %d 항목\n", pages, left);

    return 0;
}