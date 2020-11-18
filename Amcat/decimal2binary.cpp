#include<bits/stdc++.h>
using namespace std;


int decimal2binary(int n){
	int temp;
	if(n==0)
		return 0;
		
	temp = n%2;
	n = n/2;
	decimal2binary(n);
	cout << temp;
	
	return 0;
		
}

int main(){
	int n;
	cin >> n;
	decimal2binary(n);
}
