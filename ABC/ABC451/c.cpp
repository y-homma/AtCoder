#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int Q;
    cin >> Q;
    priority_queue<int> q;
    int ans = 0;
    for (int i = 0; i < Q; i++) {
        int o, h;
        cin >> o >> h;
        if (o == 1) {
            ans += 1;
            q.push(-h);
        } else {
            while (!q.empty()) {
                int top = -1 * q.top();
                if (top <= h) {
                    ans -= 1;
                    q.pop();
                } else {
                    break;
                }
            }
        }
        cout << ans << "\n";
    }
    
    return 0;
}
