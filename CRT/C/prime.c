#include<stdio.h>
#include<stdbool.h>
bool isprime(int a){
    for(int i; i< a;i++){
        if(a%i ==0){
            return false;
        }
    }
    return true;
}
int main()
{
    int n;
    printf("Enter a value:");
    scanf("%d",&n);
    printf("%d \n",isprime(n));
    return 0;
}