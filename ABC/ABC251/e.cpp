#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<ll> A(N);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    ll ans = 1000000000000000000;
    // A0を使う場合
    vector<vector<ll>> DP1(N, vector<ll>(2, 0));
    DP1[0][0] = 1000000000000000000; 
    DP1[0][1] = A[0]; 
    // A0を使わない場合(AN-1を使う場合)
    vector<vector<ll>> DP2(N, vector<ll>(2, 0));
    DP2[0][0] = 0;
    DP2[0][1] = 1000000000000000000;

    for (int i = 1; i < N; i++) {
        // 使わない場合は前段階で必ず使う必要がある
        DP1[i][0] = DP1[i-1][1];
        DP2[i][0] = DP2[i-1][1];
        // 使う場合は前段階はどっちでもいい
        DP1[i][1] = min(DP1[i-1][0], DP1[i-1][1]) + A[i];
        DP2[i][1] = min(DP2[i-1][0], DP2[i-1][1]) + A[i];
    }
    ans = min(ans, min(DP1[N-1][0], DP1[N-1][1]));

    // A0を使わない場合は必ずAN-1を使う必要がある
    ans = min(ans, DP2[N-1][1]);

    cout << ans << "\n";

    return 0;
}
