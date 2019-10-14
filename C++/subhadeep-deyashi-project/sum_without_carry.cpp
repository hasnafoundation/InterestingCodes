#include "stdc++.h"
#define ll long long
using namespace std;

int add(int param1, int param2) 
{
    string p1 = to_string(param1); 
    string p2 = to_string(param2); 
    int sum = 0;
    for(int index = 0; index < max(p1.length(), p2.length()) ; ++index) 
    {
        int a1 = 0, a2 = 0;
        if(index < p1.length()) 
        {
            string s1;
            s1 += p1[p1.length() -1 - index];
            a1 = stoi(s1);
        }
        if(index < p2.length()) 
        {
            string s2;
            s2 += p2[p2.length() -1 - index];
            a2 = stoi(s2);
        }
        int total = (a1 + a2);
        if(total >= 10)
            total -= 10;
        sum += total * (int)pow(10, index);
    }
    return sum;
}

int main()
{
    int t;
    cin >> t;
    while(t--)
    {
        int a, b, s;
        cin >> a >> b;
        cout << add(a, b) << "\n";
    }
    return 0;
}