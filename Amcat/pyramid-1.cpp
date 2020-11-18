#include<bits/stdc++.h>
using namespace std;
/*
pattern printed

5
1
121
12321
1234321

*/


int main(){
	int n,i,j;
	cin >> n;
	for(i=1;i<=n;i++){
		for(j=1;j<=i;j++){
			cout << j;
		}
		
		for(j=i-1;j>=1;j--){
				cout << j;
		}
		
		cout <<endl;
	}
}
