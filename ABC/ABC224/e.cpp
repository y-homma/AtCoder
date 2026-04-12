#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int H, W, N;
    cin >> H >> W >> N;
    vector<vector<int>> A(N, vector<int>(3, 0));
    map<int, vector<int>> rd, cd;
    vector<int> D(N, 0);
    vector<pair<int, int>> S(N);
    for (int i = 0; i < N; i++) {
        int r, c, a;
        cin >> r >> c >> a;
        A[i] = {r, c, a};
        if (!rd.contains(r)) {
            rd[r] = {};
        }
        rd[r].push_back(i);
        if (!cd.contains(c)) {
            cd[c] = {};
        }
        cd[c].push_back(i);
        S[i] = {a, i};
    }
    sort(S.begin(), S.end(), [](const pair<int, int>& x, const pair<int, int>& y) {
        if (x.first != y.first) {
            return x.first > y.first;
        }
        return x.second > y.second;
    });

    vector<int> DP(N, 0);
    for (pair<int, int> n : S) {
        int a = n.first;
        int i = n.second;
        int r = A[i][0];
        int c = A[i][1];
        for (int ni : rd[r]) {
            if (ni != i && A[ni][2] < a) {
                DP[ni] = max(DP[ni], DP[i] + 1);
            }
        }
        for (int ni : cd[c]) {
            if (ni != i && A[ni][2] < a) {
                DP[ni] = max(DP[ni], DP[i] + 1);
            }
        }
    }
    for (int ans : DP) {
        cout << ans << "\n";
    }
    
    
    return 0;
}
