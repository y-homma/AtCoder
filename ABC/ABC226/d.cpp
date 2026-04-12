#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<vector<int>> P(N, vector<int>(2, 0));
    for (int i = 0; i < N; i++) {
        cin >> P[i][0] >> P[i][1];
    }

    set<pair<int, int>> magic;
    for (int i = 0; i < N; i++) {
        int x0 = P[i][0];
        int y0 = P[i][1];
        for (int j = 0; j < N; j++) {
            if (i == j) {
                continue;
            }
            int x1 = P[j][0];
            int y1 = P[j][1];
            int dx = x1 - x0;
            int dy = y1 - y0;
            int d = gcd(abs(dx), abs(dy));
            magic.insert({dx / d, dy / d});
        }
    }
    cout << magic.size() << "\n";

    return 0;
}
