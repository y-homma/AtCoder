#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<int> T(N);
    map<int, vector<int>> K;
    for (int i = 0; i < N; i++) {
        int t, k;
        cin >> t >> k;
        T[i] = t;

        vector<int> A(k);
        for (int j = 0; j < k; j++) {
            int a;
            cin >> a;
            A[j] = a - 1;
        }
        K[i] = A;
    }

    set<int> need;
    deque<int> q;
    q.push_back(N-1);
    ll ans = 0;
    while(!q.empty()) {
        int cn = q.front();
        q.pop_front();
        if (!need.contains(cn)) {
            need.insert(cn);
            ans += T[cn];
            for (int a : K[cn]) {
                if (!need.contains(a)) {
                    q.push_back(a);
                }
            }
        }
    }
    cout << ans << "\n";
    return 0;
}
