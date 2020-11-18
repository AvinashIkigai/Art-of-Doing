#include<bits/stdc++.h>
using namespace std;

int factorial(int n){
	if(n <= 0){
		return 0;
	}
	
	if(n == 1){
		return 1;
	}
	
	return n*factorial(n-1);
}

int strong(int n){
	int sum = 0,temp;
	int oldnum = n;
	while(n!=0){
		temp = n%10;
		sum += factorial(temp);
		n = n/10;
	}
	if(oldnum == sum)
		cout << "strong";
	else
		cout << "False";
}


int main(){
	int n;
	cin >> n;
	strong(n);
}
