#include<bits/stdc++.h>
using namespace std;
int prime(int n)
{
if(n<0)
return 0;
for(int i=2;i<n;i++)
{
if(n%i==0)
return 0;
}
return 1;
}
int main()
{
for(int i=1;i<=100;i++)
{
if(prime(i))
cout<<i<<" " ;
}


}