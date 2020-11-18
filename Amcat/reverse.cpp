#include<bits/stdc++.h>
using namespace std;

int reverse(int *arr,int n){
	sort(arr,arr+n,greater<int>()); //to sort array decreasing order
	sort(arr,arr+n);				//to sort array in increasing order
	reverse(arr,arr+n);				//to reverse the array
	for(int i=0;i<n;i++)
		cout << arr[i] << " ";
}




int main(){
	int n;
	cin >> n;
	int arr[n];
	len_arr = sizeof(arr)/sizeof(arr[0]); //to calculate the length integer of array
	for(int i=0;i<n;i++)
		cin >> arr[i];
	reverse(arr,n);	
}
