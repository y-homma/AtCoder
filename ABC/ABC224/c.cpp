#include <bits/stdc++.h>
using namespace std;
using ll = long long;

bool isTriangle(pair<int, int>a, pair<int, int> b, pair<int, int>c) {
    if (a.first == b.first) {
        // y軸平行
        if (a.first == c.first) {
            return false;
        } else {
            return true;
        }
    } else {
        int xa = a.first;
        int ya = a.second;
        int xb = b.first;
        int yb = b.second;
        int xc = c.first;
        int yc = c.second;
        ll left = (yb - ya) * (xc - xa);
        ll right = (yc - ya) * (xb - xa);
        return left != right;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<pair<int, int>> P(N);
    for (int i = 0; i < N; i++) {
        int x, y;
        cin >> x >> y;
        P[i] = pair<int, int>{x, y};
    }

    int ans = 0;
    for (int i = 0; i < N-2; i++) {
        pair<int, int> a = P[i];
        for (int j = i + 1; j < N - 1; j++) {
            pair<int, int> b = P[j];
            for (int k = j + 1; k < N; k++) {
                pair<int, int> c = P[k];
                bool isT = isTriangle(a, b, c);
                if (isT) {
                    ans++;
                }
            }
        }
    }
    cout << ans << "\n";

    
    return 0;
}
