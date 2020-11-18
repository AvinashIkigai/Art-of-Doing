#include<bits/stdc++.h>
using namespace std;

int main()
{
    char str[] = "hj;pq910js54";
	cout << strlen(str); //to calculate length of char array
    cout << "The digit in the string are:" << endl;
    for (int i=0; i<strlen(str); i++)
    {
        if (isdigit(str[i]))
            cout << str[i] << " ";
    }

    return 0;
}
