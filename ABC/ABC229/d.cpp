#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string S;
    cin >> S;
    int K;
    cin >> K;
    int N = S.size();
    vector<int> dots(N + 1);
    dots[0] = 0;
    for (int i = 0; i < N; i++) {
        char s = S.at(i);
        int add = 0;
        if (s == '.') {
            add = 1;
        }
        dots[i+1] = dots[i] + add;
    }

    int ans = 0;
    int right = 0;
    for (int i = 0; i < N; i++) {
        while (right < N && dots[right + 1] - dots[i] <= K) {
            right++;
        }
        ans = max(ans, right - i);
    }
    cout << ans << "\n";

    return 0;
}
