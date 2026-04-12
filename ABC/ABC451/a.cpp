#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string S;
    cin >> S;
    if (S.size() % 5 == 0) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
    
    return 0;
}
