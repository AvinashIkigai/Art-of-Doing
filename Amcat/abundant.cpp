#include<bits/stdc++.h>
using namespace std;

void abundant(int n){
	int i, sum = 0;
	
	for(i=1;i<=n/2;i++){
		if(n%i == 0){
			sum+=i;
		}
	}
	if(n < sum)
		cout << "Abundant";
	else
		cout << "False";
}

int main(){
	int n;
	cin >> n;
	abundant(n);
}
