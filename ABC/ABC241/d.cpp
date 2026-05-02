#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q;
    cin >> Q;
    multiset<ll> S;
    int op, k;
    ll x;
    for (int i = 0; i < Q; i++) {
        cin >> op;
        cin >> x;
        if (op == 1) {
            S.insert(x);
        } else if (op == 2) {
            cin >> k;
            bool ok = true;
            auto idx = S.upper_bound(x);
            for (int j = 0; j < k; j++) {
                if (idx == S.begin()) {
                    ok = false;
                    break;
                }
                idx--;
            }
            if (ok) {
                cout << *idx << "\n";
            } else {
                cout << "-1\n";
            }
        } else {
             cin >> k;
            bool ok = true;
            auto idx = S.lower_bound(x);
            for (int j = 0; j < k; j++) {
                if (j != 0) {
                    idx++;
                }
                if (idx == S.end()) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                cout << *idx << "\n";
            } else {
                cout << "-1\n";
            }
        }
    }

    return 0;
}
