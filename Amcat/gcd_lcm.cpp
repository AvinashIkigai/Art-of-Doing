//GCD and LCM of two numbers

#include<bits/stdc++.h>
using namespace std;

int gcd(int a, int b){
	if(a == b)
		return a;
	
	while(a!=b){
		if(a>b)
			a-=b;
		else
			b-=a;
	}
	return a;
}

int lcm(int a, int b){
	int l;
	l = (a*b)/gcd(a,b);
	return l;
}

//driver program
int main(){
	int a,b;
	cin >> a;
	cin >> b;
	cout <<"GCD is" << gcd(a,b)<<endl;
	cout << "LCM is"<< lcm(a,b);

}
