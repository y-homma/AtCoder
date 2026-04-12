#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string X;
    cin >> X;
    int dotIdx = X.find('.');
    int ans = stoi(X.substr(0, dotIdx));
    int p1 = stoi(X.substr(dotIdx + 1, 1));
    if (p1 >= 5) {
        ans += 1;
    } 
    cout << ans;

    return 0;
}
