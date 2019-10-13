#include<bits/stdc++.h>
#include<iostream>
using namespace std;
int total;

void print_coin_combination(int r[], int coins[])
{
    if(r[total] == -1)
    {
        cout << "\n\nNot possible to form the total with the given coins...." << endl;
        return;
    }
    int start = total;
    cout << "\n\nCoins used to form the total are ....  ";
    while(start != 0)
    {
        int i = r[start];
        cout << coins[i] << " , ";
        start -= coins[i];
    }
    cout << "\n\n";
}

void get_min_coins(int coins[], int n)
{
    int t[total + 1], r[total + 1];
    t[0] = 0;
    r[0] = -1;
    for(int i = 1; i <= total; ++i)
    {
        t[i] = INT_MAX - 1;
        r[i] = -1;
    }

    for(int i = 0; i < n; ++i)
    {
        for(int j = coins[i]; j <= total; ++j)
        {
            if( 1 + t[j - coins[i]] < t[j] )
            {
                t[j] = 1 + t[j - coins[i]];
                r[j] = i;
            }           
        }
    }
    print_coin_combination(r, coins);
    cout << "total coins needed = " << t[total] << "\n\n";
}

int main()
{
    int n;
    cout << "enter the total : ";
    cin >> total;
    cout << "enter the number of coins : ";
    cin >> n;
    int coins[n+1];
    cout << "enter the coins : ";
    for(int i = 0; i < n; cin >> coins[i], ++i);

    get_min_coins(coins, n);

    return 0;
}