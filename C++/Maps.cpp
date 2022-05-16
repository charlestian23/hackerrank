#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int queries;
    cin >> queries;
    map<string, int> students;
    for (int i = 0; i < queries; i++)
    {
        int type;
        string name;
        cin >> type >> name;
        if (type == 1)
        {
            int marks;
            cin >> marks;
            map<string, int>::iterator itr = students.find(name);
            if (itr == students.end())
                students.insert(make_pair(name, marks));
            else
                students[name] += marks;
        }
        else if (type == 2)
            students.erase(name);
        else if (type == 3)
        {
            map<string, int>::iterator itr = students.find(name);
            if (itr == students.end())
                cout << 0 << endl;
            else
                cout << students[name] << endl;
        }
    }
    
    return 0;
}