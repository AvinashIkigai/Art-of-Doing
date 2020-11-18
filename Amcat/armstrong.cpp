#include<bits/stdc++.h>
using namespace std;

int count_digit(int num){
	int temp;
	int count = 0;
	while(num!=0){
		count+=1;
		num = num/10;
	}
	return count;
}


void printarm(int n){
	int digits = count_digit(n);
	int i, val=0, temp;
	int oldnum = n;
	while(n!=0){
		temp = n%10;
		val = val + pow(temp,digits);
		n = n/10;
	}
	if(oldnum == val)
		cout << "Armstrong";
	else
	cout << "False";
}


int main(){
	int n;
	cin >> n;
	printarm(n);
}
