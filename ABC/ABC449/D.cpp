#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int L, R, D, U;
    cin >> L >> R >> D >> U;
    ll ans = 0;
    // abs(x) >= abs(y)
    for (int i = L; i <= R; i++) {
        if (i % 2 == 0) {
            int posY = U;
            int negY = D;
            if (D <= 0) {
                negY = max(-abs(i), D);
            } 
            if (U >= 0) {
                posY = min(abs(i), U);
            }
            ans += max(posY - negY + 1, 0);
        }
    }

    // abs(y) > abs(x)
    for (int i = D; i <= U; i++) {
        if (i % 2 == 0) {
            int posX = R;
            int negX = L;
            if (R >= 0) {
                posX = min(abs(i) - 1, R);
            }
            if (L <= 0) {
                negX = max(-abs(i) + 1, L);
            }
            ans += max(posX - negX + 1, 0);
        }
    }
    cout << ans << "\n";

    return 0;
}
