#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int arrays, queries;
    cin >> arrays >> queries;
    vector<vector<int>> v;
    for (int i = 0; i < arrays; i++)
    {
        int len;
        cin >> len;
        vector<int> temp;
        for (int j = 0; j < len; j++)
        {
            int num;
            cin >> num;
            temp.push_back(num);
        }
        v.push_back(temp);
    }
    for (int i = 0; i < queries; i++)
    {
        int x, y;
        cin >> x >> y;
        cout << v[x][y] << endl;
    }
    return 0;
}
