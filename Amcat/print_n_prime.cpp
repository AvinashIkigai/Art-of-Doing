#include<bits/stdc++.h>
using namespace std;

bool isprime(int a){
	int flag = 0;
	
	if(a <= 1)
		return false;
	
	for(int i=2;i<=int(a/2);i++){
		if(a%i == 0){
			return false;
			break;
		}
	}

	return true;	
}

void printprime(int a){
	int i;
	for(i=2;i<a;i++){
		if(isprime(i)){
			cout << i <<" ";
		}
	}
}


int main(){
	int n;
	cin >> n;
	printprime(n);
}
