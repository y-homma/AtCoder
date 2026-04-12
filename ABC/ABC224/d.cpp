#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int M;
    cin >> M;
    vector<vector<int>> edge(10, vector<int>{});
    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        edge[u].push_back(v);
        edge[v].push_back(u);
    }
    vector<string> P(9, "9");
    for (int i = 1; i < 9; i++) {
        int pi;
        cin >> pi;
        P[pi-1] = to_string(i);
    }
    string init ="";
    for (string p : P) {
        init += p;
    }

    map<string, int> dist = {};
    vector<int> num = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    do {
        string key = "";
        for (int n : num) {
            key += to_string(n);
        }
        dist[key] = INT_LEAST32_MAX;
    } while (next_permutation(num.begin(), num.end()));

    deque<pair<string, int>> q;
    q.push_back(pair{init, 0});
    while (!q.empty()) {
        pair<string, int> cn = q[0];
        q.pop_front();
        const string key = cn.first;
        int d = cn.second;
        if (d < dist[key]) {
            dist[key] = d;
            int i9 = key.find('9');
            for (int nn : edge[i9 + 1]) {
                string nk = key;
                string nc = nk.substr(nn - 1, 1);
                nk.replace(i9, 1, nc);
                nk.replace(nn - 1, 1, "9");
                if (dist[nk] > d + 1) {
                    q.push_back(pair{nk, d+1});
                }
            }
        }
    }
    int ans = dist["123456789"];
    if (ans == INT_LEAST32_MAX) {
        cout << "-1\n";
    } else {
        cout << ans << "\n";
    }
    
    return 0;
}
