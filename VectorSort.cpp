#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int nums;
    cin >> nums;
    vector<int> v;
    for (int i = 0; i < nums; i++)
    {
        int temp;
        cin >> temp;
        v.push_back(temp);
    }  
    sort(v.begin(), v.end());
    for (int i : v)
        cout << i << " ";
    return 0;
}
