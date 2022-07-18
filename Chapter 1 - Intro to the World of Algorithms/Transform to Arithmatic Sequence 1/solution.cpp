#include <iostream>
#include <bits/stdc++.h>
#include <cstdlib>

using namespace std;

int main() 
{
    int n, k;
    cin >> n >> k;
    int a[n];
   
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    
    int leastCount = INT_MAX;
    for (int j = a[0] - (n - 1) * k; j <= a[n - 1]; j++)
    {
        int cost = 0;
        for (int i = 0; i < n; i++)
        {
            cost += abs((j + ((i - 1) * k)) - a[i]);
        }
        
        if (leastCount > cost)
        {
            leastCount = cost;
        }
    }
    
    cout << leastCount << endl;
}