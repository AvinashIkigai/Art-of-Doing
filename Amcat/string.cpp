#include<bits/stdc++.h>
using namespace std;
int main(){
	string s;
	getline(cin, s);
	cout << s.length()<<endl; //s.size() can also be used for finding the length of the stringgh
	cout << s.at(1) <<endl;
	for(int i=0;i<s.length();i++){ //removing number of spaces from the string
		if(!isspace(s[i]))
			cout << s[i]<<endl;
	}
	cout << s+s; //concatenation of string
}
