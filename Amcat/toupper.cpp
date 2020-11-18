#include<bits/stdc++.h>
using namespace std;

void uppercase(char * str){
//	cout << str <<endl;
//	transform(str.begin(),str.end(),str.begin(),::toupper); //using stl library
	for(int i=0;i<strlen(str);i++)
		putchar(toupper(str[i])); //putchar(tolower(str[i]))
	cout <<endl;
}

int main(){
	char str[] = "preparing For Amcat";
//	string str;
//	getline(cin,str);
	uppercase(str);

}
