#include<stdio.h>

int main(void){
    printf("sizeof(\'a\') = %d\n", sizeof('a'));
    printf("sizeof(12345) = %d\n", sizeof(12345));
    printf("sizeof(12345u) = %d\n", sizeof(12345u));
    printf("sizeof(12345L) = %d\n", sizeof(12345L));
    printf("sizeof(12.34f) = %d\n", sizeof(12.34f));
    printf("sizeof(12.34567) = %d\n", sizeof(12.34567));
    printf("sizeof(1.234e-5) = %d\n", sizeof(1.234e-5));
    printf("sizeof(\"abc\") = %d\n", sizeof("abc"));
    
    return 0;
}