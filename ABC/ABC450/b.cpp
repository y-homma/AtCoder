#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<vector<int>> C(N, vector<int>(N, 0));
    for (int i = 0; i < N - 1; i++) {
        for (int j = i + 1; j < N; j++) {
            cin >> C[i][j];
        }
    }

    for (int i = 0; i < N - 2; i++) {
        for (int j = i + 1; j < N - 1; j++) {
            for (int k = j + 1; k < N; k++) {
                if (C[i][j] + C[j][k] < C[i][k]) {
                    cout << "Yes" << "\n";
                    return 0;
                }
            }
        }
    }
    cout << "No\n";
    
    return 0;
}
