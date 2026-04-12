#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int X;
    cin >> X;
    if (X % 100 == 0) {
        if (X == 0) {
            cout << "No" << "\n";
        } else {
            cout << "Yes" << "\n";
        }
    } else {
        cout << "No";
    }

    return 0;
}
