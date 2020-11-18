#include<bits/stdc++.h>
using namespace std;
int main(){
	string s;
	getline(cin, s);
	for(int i=0;i<s.length();i++) //printing the string if its special symbol like @#^&* etc.
		if(ispunct(s[i]))
			cout << s[i];
}
