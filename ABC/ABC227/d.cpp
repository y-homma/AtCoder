#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, K;
    cin >> N >> K;
    vector<ll> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    ll ok = 0;
    ll ng = 1e18 / K;
    while (ng - ok > 1) {
        ll mid = (ok + ng) / 2;
        ll sum = 0;
        for (ll a : A) {
            sum += min(a, mid);
        }
        if (K * mid <= sum) {
            ok = mid;
        } else {
            ng = mid;
        }
    }
    cout << ok << "\n";

    return 0;
}
