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
        A[i] %= K;
    }
    sort(A.begin(), A.end());
    deque<int> q;
    for (int a : A) {
        q.push_back(a);
    }

    int minD = q.back() - q.front();
    for (int i = 0; i < N; i++) {
        int a = q.front();
        q.pop_front();
        q.push_back(a + K);
        int diff = a + K - q.front();
        minD = min(minD, diff);
    }
    cout << minD << "\n";
    return 0;
}
