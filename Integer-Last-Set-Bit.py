#include <stdio.h>
int main()
{ 
    int n,b=0;
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(int i=0;i<n;i++){
        for(int j=1;j>0;j*=2){
            if(a[i]&j){
            b=b+j;
            break;
            }
        }
    }
    printf("%d ",b);
    return 0;
}
