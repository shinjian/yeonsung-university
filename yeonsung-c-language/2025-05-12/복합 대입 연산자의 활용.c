#include<stdio.h>

int main(void){
    int items = 0, pages = 0;
    int items_per_page = 0;

    printf("항목 수: ");
    scanf("%d", &items);

    printf("한 페이지당 항목 수: ");
    scanf("%d", &items_per_page);

    pages = items / items_per_page;
    items = items % items_per_page;

    printf("%d 페이지의 %d 항목\n", pages, items);

    return 0;
}