#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, Q;
    cin >> N >> Q;
    vector<int> E(N+1, -1);
    vector<int> RE(N+1, -1);
    
    for (int q = 0; q < Q; q++) {
        int n;
        cin >> n;
        if (n == 1) {
            int x, y;
            cin >> x >> y;
            E[x] = y;
            RE[y] = x;
        } else if (n == 2) {
            int x, y;
            cin >> x >> y;
            E[x] = -1;
            RE[y] = -1;
        } else {
            int x;
            cin >> x;
            int current = x;
            while (RE[current] > -1) {
                current = RE[current];
            }

            vector<int> ans = {current};
            while (E[current] > -1) {
                ans.push_back(E[current]);
                current = E[current];
            }
            cout << ans.size();
            for (int a : ans) {
                cout << " " << a;
            }
            cout << "\n";
        }
    }


    return 0;
}
