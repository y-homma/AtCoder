#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<int> S(N, 0);
    for (int i = 0; i < N; i++) {
        cin >> S[i];
    }
    set<int> Area;
    for (int a = 1; a < 500; a++) {
        for (int b = 1; b < 500; b++) {
            int s = 4 * a * b + 3 * (a + b);
            if (s <= 1000) {
                Area.insert(s);
            }
        }
    }
    int ans = 0;
    for (int s : S) {
        if (!Area.contains(s)) {
            ans += 1;
        }
    }
    cout << ans << "\n";

    return 0;
}
