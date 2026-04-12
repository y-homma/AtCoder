#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N;
    cin >> N;
    vector<vector<int>> fuses(N, vector<int>(2, 0));
    vector<ll> start(N, 0);
    for (int i = 0; i < N; i++) {
        cin >> fuses[i][0] >> fuses[i][1];
    }
    float left = 0.0;
    float right = 0.0;
    int li = 0;
    int ri = N-1;
    ll lL = 0;
    for (;;) {
        if (li < ri) {
            float lt = fuses[li][0] / (float) fuses[li][1];
            float rt = fuses[ri][0] / (float) fuses[ri][1];
            if (left + lt < right + rt) {
                lL += fuses[li][0];
                li++;
                left += lt;
            } else {
                ri--;
                right += rt;
            }
        } else {
            int a = fuses[li][0];
            int b = fuses[li][1];
            float x = (a + b * right - b * left) / 2.0;
            cout << lL + x << "\n";
            break;
        }
    }
    return 0;
}
