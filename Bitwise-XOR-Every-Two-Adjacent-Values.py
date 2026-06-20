#include <stdio.h>
int main()
{ 
    int n;
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
        printf("%d ",a[j]^a[j+1]);
        a[j]=a[j]^a[j+1];
        }
        printf("\n");
    }
    return 0;
}
