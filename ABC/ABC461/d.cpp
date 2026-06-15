#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int H, W, K;
    cin >> H >> W >> K;
    vector<vector<int>> S(H, vector<int>(W, 0));
    vector<vector<int>> T(H, vector<int>(W, 0));
    for (int h = 0; h < H; h++) {
        string s;
        cin >> s;
        for (int w = 0; w < W; w++) {
            S[h][w] = stoi(s.substr(w, 1));
        }
        if (h > 0) {
            T[h][0] = T[h-1][0] + S[h][0];
            for (int w = 1; w < W; w++) {
                T[h][w] = T[h-1][w] + T[h][w-1] - T[h-1][w-1] +  S[h][w];
            }
        } else {
            T[0][0] = S[0][0];
            for (int w = 1; w < W; w++) {
                T[h][w] = T[h][w-1] + S[h][w];
            }
        }
    }
    int ans = 0;
    for (int hl = 0; hl < H; hl++) {
        for (int hr = hl; hr < H; hr++) {
            for (int wl = 0; wl < W; wl++) {
                for (int wr = wl; wr < W; wr++) {
                    int count = T[hr][wr];
                    if (hl > 0 && wl > 0) {
                        count -= T[hr][wl-1] + T[hl-1][wr] - T[hl-1][wl-1];
                    } else if (wl > 0) {
                        count -= T[hr][wl-1];
                    }
                    else if (hl > 0) {
                        count -= T[hl-1][wr];
                    }
                    
                    if (count == K) {
                        ans += 1;
                    }
                }
                    
            }
                
        }
            
    }
    cout << ans << "\n";
    
    return 0;
}
