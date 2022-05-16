#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int len;
    cin >> len;
    vector<int> v;
    for (int i = 0; i < len; i++)
    {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }
    int queries;
    cin >> queries;
    for (int i = 0; i < queries; i++)
    {
        int num;
        cin >> num;
        vector<int>::iterator lower = lower_bound(v.begin(), v.end(), num);
        if (v[lower - v.begin()] == num)
            cout << "Yes " << lower - v.begin() + 1 << endl;
        else
            cout << "No " << lower - v.begin() + 1 << endl;
    }
    return 0;
}
