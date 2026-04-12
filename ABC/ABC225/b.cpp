#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<int> eOut(N, 0);
    for ( int i = 0; i < N - 1; i++) {
        int a, b;
        cin >> a >> b;
        eOut[a-1] += 1;
        eOut[b-1] += 1;
    }

    for (int e : eOut) {
        if (e == N - 1) {
            cout << "Yes\n";
            return 0;
        }
    }
    cout << "No\n";
    return 0;
}
