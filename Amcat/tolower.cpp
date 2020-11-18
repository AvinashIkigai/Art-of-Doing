#include<bits/stdc++.h>
using namespace std;

void lowercase(char * str){
//	transform(str.begin(),str.end(),str.begin(),::tolower); //using stl library
//	cout << str <<endl;
	for(int i=0;i<strlen(str);i++)
		putchar(tolower(str[i])); //putchar(toupper(str[i]))
		cout<<endl;
}



int main(){
	char str[] = "PRPARING For Amcat";
//	string str;
//	getline(cin,str);
	lowercase(str);	
}
