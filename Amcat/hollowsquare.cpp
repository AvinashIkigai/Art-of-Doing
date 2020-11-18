#include<bits/stdc++.h>
using namespace std;

/*
pattern printed

5
*****
*   *
*   *
*   *
*****


*/

int main(){
	int i,j,n;
	cin >> n;
	for(i=0;i<n;i++){
		for(j=0;j<n;j++){
			if(i==0 || i==n-1 || j==0 || j==n-1)
				cout << "*";
			else
				cout << " ";
		}
		cout <<endl;
	}
}

