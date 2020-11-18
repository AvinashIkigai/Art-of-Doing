#include<bits/stdc++.h>
using namespace std;

void printfib(int n){
	int oldnum = 0, newnum = 1, currentnum, i;
	
	for(i=1; i<=n; i++){
		if(i == 1){
		
			cout << oldnum << " ";
			continue;
		}
		
		if(i == 2){
		
			cout <<newnum << " ";
			continue;
		}
		currentnum = oldnum+newnum;
		cout << currentnum << " ";
		oldnum = newnum;
		newnum = currentnum;
	}
	

}

int main(){
	int n;
	cin >> n;
	printfib(n);
}
