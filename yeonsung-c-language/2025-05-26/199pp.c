#include<stdio.h>

int main(void){
    int menu = 0;

    printf("1. 파일 열기\n");
    printf("2. 재생\n");
    printf("3. 재생 음성\n");
    printf("선택 : \n");
    scanf("%d", &menu);

    if(menu == 1){
        printf("파일 열기 메뉴를 선택했습니다.\n");
    }
    else if(menu == 2){
        printf("재생 메뉴를 선택했습니다.\n");
    }
    else if(menu == 3){
        printf("재생 음성 메뉴를 선택했습니다.\n");
    }
    else{
        printf("잘못선택하셨습니다\n");
    }

    return 0;
}