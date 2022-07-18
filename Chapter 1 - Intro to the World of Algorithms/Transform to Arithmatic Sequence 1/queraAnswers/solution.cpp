#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

const int maxn = 1005;

long long a[maxn];

int main()
{
    int n;
    long long k;
    cin >> n >> k;
    
    for(int i = 0; i < n; i++)
        cin >> a[i];

    long long val = 1000 * 1000 * 1000;

    for(int x = -100000; x < 100000; x++)
    {
        long long t = 0;
        for(int i = 0; i < n; i++)
            t += abs((x + i * k) - a[i]);        
        val = min(val, t);
    }
    cout << val << '\n';
    return 0;
}