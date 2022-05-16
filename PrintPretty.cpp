#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
	int T; cin >> T;
	cout << setiosflags(ios::uppercase);
	cout << setw(0xf) << internal;
	while(T--) {
		double A; cin >> A;
		double B; cin >> B;
		double C; cin >> C;

		// formatting for A
		cout << hex << left << showbase << nouppercase;
		// printing A
		cout << (long long) A << endl;

		// formatting for B
		cout << dec << right << setw(15) << setfill('_') << showpos << fixed << setprecision(2);
		// printing A
		cout << B << endl;

		// formatting for C
		cout << scientific << uppercase << noshowpos << setprecision(9);
		// printing C
		cout << C << endl;
	}
	return 0;

}