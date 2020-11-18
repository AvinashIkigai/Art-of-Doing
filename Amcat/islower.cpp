#include<bits/stdc++.h>
using namespace std;

void lowertoupper(char *str){
	for(int i=0;i<strlen(str);i++){
		if(islower(str[i]))
			str[i] = str[i]-32;
	}
	
	for(int i=0;i<strlen(str);i++){
		cout << str[i];
	}
}

int main(){
	char str[] = "preparing For Amcat";
//	string str;
//	getline(cin,str);
	lowertoupper(str);

}
