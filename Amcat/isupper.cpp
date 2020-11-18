#include<bits/stdc++.h>
using namespace std;

void uppertolower(char *str){
	for(int i=0;i<strlen(str);i++){
		if(isupper(str[i]))
			str[i] = str[i]+32;
	}
	
	for(int i=0;i<strlen(str);i++){
		cout << str[i];
	}
}

int main(){
	char str[] = "pREPARING For Amcat";
//	string str;
//	getline(cin,str);
	uppertolower(str);

}
