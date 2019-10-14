#include <bits/stdc++.h>
using namespace std;
#define ll long long
const ll MOD = 1e9 + 7;

ll fact[1000001];     // stores the factorial of the numbers

ll calc(ll n)
{
    if(n == 0)
        return 1;
        
    if(fact[n] != -1)
        return fact[n];
    
    // calculate recursively the factorial and store it for future use
    else
        return fact[n] = (n * calc(n-1)) % MOD;
}

int main()
{
    memset(fact, -1, sizeof(fact));
    int t;
    cout << "\nEnter the number of test cases : ";
    cin >> t;
    while(t--)
    {
        ll n;
        cout << "Enter the number : ";
        cin >> n;
        cout << "The factorial of " << n << "  =  " << calc(n) << "\n";
    }
    return 0;
}