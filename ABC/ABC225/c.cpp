#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    cin >> N >> M;
    // A * 7 + modが始点
    int A = 0;
    int mod = 0;
    bool ans = true;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            int b;
            cin >> b;
            if (i == 0 && j == 0) {
                A = b / 7;
                mod = b % 7;
                if (mod == 0) {
                    mod = 7;
                    A -= 1;
                }
            } else {
                if (mod + j > 7 || (A + i) * 7 + (mod + j) != b) {
                    ans = false;
                }
            }
        }
    }
    if (ans) {
        cout << "Yes\n";
    } else {
        cout << "No\n";
    }
    return 0;
}
