#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, K;
    cin >> N >> K;
    vector<int> A(N);
    for (int i = 0; i < N; i ++) {
        cin >> A[i];
    }
    int maxA = *max_element(begin(A), end(A));
    int minA = *min_element(begin(A), end(A));
    ll maxDiff = 0;
    for (int a : A) {
        if (a == maxA) {
            continue;
        }
        int floor = (maxA - a) / K;
        ll lower = a + floor * K;
        ll higher = a + floor * (K + 1);
        maxDiff = max(min(maxA - lower, higher - maxA), maxDiff);
    }
    cout << maxDiff << "\n";

    
    return 0;
}
