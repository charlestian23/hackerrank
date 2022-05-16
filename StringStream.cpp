#include <sstream>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> parseInts(string str) {
	vector<int> v;

    if (str.size() == 0)
        return v;

    int commas = count(str.begin(), str.end(), ',');
    char ch;

    stringstream ss(str);
    for (int i = 0; i < commas + 1; i++)
    {
        int temp;
        ss >> temp >> ch;
        v.push_back(temp);
    }
    return v;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }
    
    return 0;
}