#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N, L, R;
    cin >> N >> L >> R;
    string S;
    cin >> S;
    vector<vector<int>> counts(N, vector<int>(26, 0));
    counts.at(0).at(S.at(0) - 'a') = 1;
    ll ans = 0;
    for (int i = 1; i < N; i++){
        for (int j = 0; j < 26; j++) {
            counts.at(i).at(j) = counts.at(i-1).at(j);
        }
        counts.at(i).at(S.at(i) - 'a') += 1;
    }
    for (int i = 0; i < N - L; i++) {
        int cL = i + L - 1;
        int cR = min(N - 1, i + R);
        int j = S.at(i) - 'a';
        // cout << "Add for " << i << ": " << counts.at(cR).at(j) - counts.at(cL).at(j) << "\n";
        ans += counts.at(cR).at(j) - counts.at(cL).at(j);
    }
    cout << ans << "\n";

    return 0;
}
