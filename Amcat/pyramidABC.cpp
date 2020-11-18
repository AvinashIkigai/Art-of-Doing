#include<bits/stdc++.h>
using namespace std;
/*
pattern printed

5
A
ABA
ABCBA
ABCDCBA
ABCDEDCBA

if you want to print small letters replace 65 by 97 only..

5
a
aba
abcba
abcdcba
abcdedcba

*/


int main(){
	int n,i,j;
	cin >> n;
	for(i=1;i<=n;i++){
		for(j=1;j<=i;j++){
			cout << char(j+65-1);
		}
		
		for(j=i-1;j>=1;j--){
				cout << char(j+65-1);
		}
		
		cout <<endl;
	}
}
