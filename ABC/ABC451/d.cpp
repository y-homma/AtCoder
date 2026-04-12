#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll N;
    cin >> N;
    vector<vector<int>> p2(10, vector<int>{});

    for (int k = 0; k < 30; k++) {
        string num = to_string(static_cast<int>(pow(2, k)));
        int length = num.size();
        if (length < 10) {
            p2[length].push_back(stoi(num));
        }
        // cout << "Insert " + num + " to " << length << "\n";
    }

    vector<set<int>> X(10, set<int>{});
    X[0].insert(0);
    vector<int> ans;
    for (int k = 1; k < 10; k++) {
        for (int i = 1; i < k + 1; i++) {
            for (int x : X[k-i]) {
                for (int p : p2[i]) {
                    X[k].insert(x * pow(10, i) + p);
                }
            }
        }
        copy(X[k].begin(), X[k].end(), back_inserter(ans));
    }
    sort(ans.begin(), ans.end());
    cout << ans[N-1] << "\n";
    
    return 0;
}
