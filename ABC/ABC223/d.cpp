#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N, M;
    cin >> N >> M;
    vector<set<int>> E(N, set<int>{}), ER(N, set<int>{});
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        E[a-1].insert(b-1);
        ER[b-1].insert(a-1);
    }

    set<int> rem;
    for (int i = 0; i < N; i++) {
        rem.insert(i);
    }

    priority_queue<int> q;
    for (int i = 0; i < N; i++) {
        if (ER[i].empty()) {
            q.push(-i);
            rem.erase(i);
        }
    }

    vector<int> ans;
    while (!q.empty()) {
        int ci = -1 * q.top();
        q.pop();
        ans.push_back(ci);
        for (int nn : E[ci]) {
            ER[nn].erase(ci);
            if (ER[nn].empty()) {
                q.push(-nn);
                rem.erase(nn);
            }
        }
    }

    if (rem.empty()) {
        for (int n : ans) {
            cout << n + 1 << " ";
        }
        cout << "\n";
    } else {
        cout << -1 << "\n";
    }
    return 0;
}
