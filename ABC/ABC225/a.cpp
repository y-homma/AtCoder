#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> A = {0, 1, 2};
    string s;
    cin >> s;

    set<string> found = {};
    do {
        string newS = s.substr(A[0], 1) + s.substr(A[1], 1) + s.substr(A[2], 1);
        found.insert(newS);
    } while (next_permutation(A.begin(), A.end()));

    cout << found.size() << "\n";
    return 0;
}
