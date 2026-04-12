#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    string S;
    cin >> S;
    regex er("^.*er$");

    if (regex_match(S, er)) {
        cout << "er" << "\n";
    } else {
        cout << "ist" << "\n";
    }
    return 0;
}
