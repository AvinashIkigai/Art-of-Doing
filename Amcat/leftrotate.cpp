// C++ program to rotate an array by n times

#include <bits/stdc++.h> 
using namespace std; 

void leftrotateby1(int arr[], int n) 
{ 
    int temp = arr[0], i; 
    for (i = 0; i < n - 1; i++) 
        arr[i] = arr[i + 1]; 
  
    arr[i] = temp; 
} 
void leftrotate(int arr[], int d, int n) 
{ 
    for (int i = 0; i < d; i++) 
        leftrotateby1(arr, n); 
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
   	
    leftrotate(arr, times, n); 
    for (int i = 0; i < n; i++) 
        cout << arr[i] << " ";
  
    return 0; 
}
