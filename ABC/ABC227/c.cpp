#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll N;
    cin >> N;
    ll ans = 0;
    for (ll a = 1; a * a * a <= N; a++) {
        for (ll b = a; b * b <= N / a; b++) {
            ans += floor(N / (a * b)) - b + 1;
        }
    }
    cout << ans << "\n";

    return 0;
}
