#include<bits/stdc++.h>
using namespace std;

int main(){
	int i ,simulate,j,k;
	int arr[8], ans[8];
	for(i=0;i<8;i++){
		cin >> arr[i];
	}
	
	cin >> simulate;
	
	while(simulate != 0){
	
		for(i=0;i<8;i++){
			
			if((i == 0 && arr[i+1] == 1) || (i == 7 && arr[i-1] == 1)) {
				ans[i] = 1;			
			}
			if((i == 0 && arr[i+1] == 0) || (i == 7 && arr[i-1] == 0))
				ans[i] = 0;
			
			if((arr[i] == 0 && arr[i+2] == 0) || (arr[i] == 1 && arr[i+2] == 1)){
				ans[i+1] = 0;			
			}
			else{
				ans[i+1] = 1;
			}
		}
		
		for(k=0;k<8;k++){
				arr[k] = ans[k];
		}
				simulate-=1;
		}
				
		for(i=0;i<8;i++){
			cout << ans[i] <<" ";
		}
	}

		
	
