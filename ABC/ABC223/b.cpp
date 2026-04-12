#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    string S;
    cin >> S;
    int size = (int) S.size();
    vector<string> ss(size);
    for (int i = 0; i < size; i++) {
        ss[i] = S.substr(i, size) + S.substr(0, i);
    }
    sort(ss.begin(), ss.end());
    cout << ss[0] << "\n" << ss[size - 1] << "\n";

    return 0;
}
