#include<bits/stdc++.h>
using namespace std;
//if binary number is in format of integer following program will work
int binary2decimal(int n){
	int temp,sum=0;
	int count = 0;
	while(n!=0){
		temp = n%10;
		sum+=(temp * pow(2,count));
		count+=1;
		n = n/10;
	}
	cout <<sum;
}

int main(){
	int n;
	cin >> n;
	binary2decimal(n);
}
