#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int queries;
    cin >> queries;
    set<int> s;
    for (int i = 0; i < queries; i++)
    {
        int type, num;
        cin >> type >> num;
        if (type == 1)
            s.insert(num);
        else if (type == 2)
            s.erase(num);
        else if (type == 3)
        {
            set<int>::iterator itr = s.find(num);
            if (itr == s.end())
                cout << "No" << endl;
            else
                cout << "Yes" << endl;
        }
    }

    return 0;
}