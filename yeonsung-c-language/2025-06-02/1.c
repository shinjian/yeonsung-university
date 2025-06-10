#include<stdio.h>

int main(void){
    int a, b;
    char op, yesno = 'Y';

    while (yesno == 'Y' || yesno == 'y')
    {
        printf("수식 ? :");
        scanf("%d", &a, sizeof(a));
        scanf("%c", &op, sizeof(op));
        scanf("%d", &b, sizeof(b));

        switch (op)
        {
        case '+':
            printf("%d + %d = %d\n", a, b, a+b);
            break;
        case '-':
            printf("%d - %d = %d\n", a, b, a-b);
            break;
        case '*':
            printf("%d * %d = %d\n", a, b, a*b);
            break;
        case '/':
            if(b != 0)
                printf("%d / %d = %d\n", a, b, a/b);
            break;
        
        default:
            printf("잘못된 수식입니다.\n");
        }

        printf("계속 하시겠습니까(Y/N)?");
        scanf("%c", &yesno, sizeof(yesno));
    }
    return 0;
}