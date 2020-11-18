#include <iostream>  
using namespace std;  
int main()  
{  
int n, reverse=0, rem,count = 0;    
cout<<"Enter a number: ";    
cin>>n;    
  while(n!=0)    
  {    
     rem=n%10;
	 count+=1;    //count the number of digits  
     reverse=reverse*10+rem;    
     n/=10;    
  }    
 cout<<"Reversed Number: "<<reverse<<endl << count;     
return 0;  
} 
