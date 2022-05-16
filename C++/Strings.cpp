#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string first, second;
    cin >> first >> second;
    cout << first.size() << " " << second.size() << endl;
    cout << first + second << endl;
    char firstChar = first[0];
    char secondChar = second[0];
    cout << secondChar + first.substr(1) << " " << firstChar + second.substr(1) << endl;
    
    return 0;
}