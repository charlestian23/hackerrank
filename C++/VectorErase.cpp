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
    int remove;
    cin >> remove;
    v.erase(v.begin() + (remove - 1));
    int begin, end;
    cin >> begin >> end;
    v.erase(v.begin() + (begin - 1), v.begin() + (end - 1));
    cout << v.size() << endl;
    for (int i : v)
        cout << i << " ";
    return 0;
}
