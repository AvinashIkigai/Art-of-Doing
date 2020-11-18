#include<bits/stdc++.h>
using namespace std;
//if binary number is in format of string following program will work
int binary2decimal(string n){
	int sum=0, i;
	for(i=0;i<n.length();i++){
		if(n.at(i) == '1'){
			sum+=pow(2,i);
		}
	}
	cout << sum;
}

int main(){
	string n;
	getline(cin, n);
	binary2decimal(n);
}
