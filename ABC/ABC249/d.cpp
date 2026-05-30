#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<int> A(N);
    map<int, int> D;
    int maxA = 0;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        if (!D.contains(A[i])){
            D[A[i]] = 0;
        }
        D[A[i]] += 1;
        maxA = max(maxA, A[i]);
    }
    ll ans = 0;
    for (int i = 1; i < maxA + 1; i++) {
        if (D.contains(i)) {
            for (int j = 1; i * j < maxA + 1; j++) {
                if (D.contains(j) && D.contains(i*j)) {
                    ans += (ll) D[i] * D[j] * D[i*j];
                }
            }
        }
    }
    cout << ans << "\n";

    return 0;
}
