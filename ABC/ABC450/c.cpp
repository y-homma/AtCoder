#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int H, W;
    cin >> H >> W;
    // white: 0, black: 1
    vector<vector<int>> S(H, vector<int>(W, 0));
    vector<vector<bool>> V(H, vector<bool>(W, false));
    for (int h = 0; h < H; h++) {
        string s;
        cin >> s;
        for (int w = 0; w < W; w++) {
            if (s.at(w) == '.') {
                S[h][w] = 0;
            } else {
                S[h][w] = 1;
            }
        }
    }
    vector<pair<int, int>> D = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    deque<pair<int, int>> q;
    int ans = 0;
    for (int h = 0; h < H; h++) {
        for (int w = 0; w < W; w++) {
            if (S[h][w] == 0 && !V[h][w]) {
                bool inner = true;
                q.push_back({h, w});
                while (!q.empty()) {
                    pair<int, int> node = q.front();
                    q.pop_front();
                    int ch = node.first;
                    int cw = node.second;
                    if (!V[ch][cw]) {
                        V[ch][cw] = true;
                        if (ch == 0 || ch == H-1 || cw == 0 || cw == W-1) {
                            inner = false;
                        }
                        for (pair<int, int> d : D) {
                            int nh = ch + d.first;
                            int nw = cw + d.second;
                            if (0 <= nh && nh < H && 0 <= nw && nw < W && S[nh][nw] == 0 && !V[nh][nw]) {
                                q.push_back({nh, nw});
                            }
                        }
                    }
                }
                ans += inner ? 1 : 0;
            }
        }
    } 
    cout << ans << "\n";
    
    return 0;
}
