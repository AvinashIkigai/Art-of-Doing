// C++ program to rotate an array by 
 
#include <bits/stdc++.h> 
using namespace std; 
  

void rightrotateby1(int arr[], int n) 
{ 
    int temp = arr[n-1], i; 
    for (i = n-1; i > 0; i--) 
        arr[i] = arr[i-1]; 
  
    arr[0] = temp; 
} 
  

void rightrotate(int arr[], int d, int n) 
{ 
    for (int i = 0; i < d; i++) 
        rightrotateby1(arr, n); 
} 
  

int main() 
{ 
    int times; 
    int n;
	cout << "Size of array: "; 
	cin >> n;
   	int arr[n];
   	cout << "Enter number of times to rotate: ";
   	cin >> times;
   	cout <<"Values in array: "<<endl;
   	for (int i = 0; i < n; i++) 
        cin >> arr[i];
   	
    rightrotate(arr, times, n); 
    for (int i = 0; i < n; i++) 
        cout << arr[i] << " ";
  
    return 0; 
}
