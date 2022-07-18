#include<iostream>
using namespace std;

const int maxn = 1000 + 5;

int main()
{
    int n, q;
    int c[maxn], d[maxn];

    cin >> n >> q;
    for(int i = 0; i < n; i++)
        cin >> c[i];
    for(int i = 0; i < q; i++)
        cin >> d[i];

    for(int i = 0; i < q; i++)
    {
        int t = 0;
        for(int j = 0; j < n; j++)
            if(d[i] > c[j])
                t++;
        cout << t << endl;
    }
    return 0;
}