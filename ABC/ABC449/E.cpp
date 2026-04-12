#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N, M, Q;
    cin >> N >> M;
    vector<int> A(N);
    map<int, int> AC;
    for (int i = 0; i < M; i++) {
        AC[i + 1] = 0;
    }
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        AC[A[i]] += 1;
    }
    // <count, a>
    vector<pair<int, int>> CTK;
    for (const auto& [key, value] : AC) {
        CTK.push_back({value, key});
    }
    sort(CTK.begin(), CTK.end());
    vector<ll> countSum(AC.size() + 1);
    countSum[0] = N;
    for (long unsigned int i = 1; i < CTK.size(); i++) {
        countSum[i] = countSum[i-1] + (CTK[i].first - CTK[i-1].first) * i;
    }

    // [1, 1, 2]
    // CTK: [<0, 3>, <1, 2>, <2, 1>]
    // cS: [3, 4, 6]
    // [1, 1, 2, 3, 3, 3, 2, 1, 2, 1, 2, 3, ...]
    cin >> Q;
    ll x;
    for (int q = 0; q < Q; q++) {
        cin >> x;
        x -= 1;
        ll low = -1;
        ll high = countSum.size();
        while (high - low > 1) {
            ll mid = (low + high) / 2;
            if (countSum[mid] > x) {
                high = mid;
            } else {
                low = mid;
            }
        }
        cout << "Bound; " << low << "\n";
        if (low == -1) {
            cout << A[x] << "\n";
        } else if (low > (int) CTK.size()) {
            cout << (x - CTK[CTK.size() - 1].first) % M + 1 << "\n";
        }
        else {
            int m = (x - CTK[low].first) % (CTK[low].first + 1);
            cout << CTK[m].second << "\n";
        }
    }


    return 0;
}
