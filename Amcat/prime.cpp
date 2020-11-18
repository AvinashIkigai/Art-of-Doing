#include<bits/stdc++.h>
using namespace std;

int prime(int a){
	int flag = 0;
	for(int i=2;i<=int(a/2);i++){
		if(a%i == 0){
			flag = 1;
			break;
		}
	}
	if(flag == 0)
		cout << "Is a Prime number";
	else
		cout << "Not a Prime number";
		
}


int main(){
	int n;
	cin >> n;
	prime(n);
}
