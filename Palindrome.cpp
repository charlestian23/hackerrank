#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool isPalindrome(int x) {
    string s = to_string(x);
    for (int i = 0; i < s.length(); i++)
    {
        if (s.at(i) != s.at(s.length() - 1 - i))
            return false;
    }
    return true;
}

int main() {
    int n;
    cin >>n;
    
    if(isPalindrome(n)) {
        cout <<n<<" is a palindrome";
    }
    else {
        cout << n<<" is NOT a palindrome";
    }
    return 0;
}