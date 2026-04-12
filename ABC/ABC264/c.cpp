#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

bool isSameBitCount(int N, int count) {
    int c = N;
    int bc = 0;
    while (c > 0) {
        bc += c % 2;
        c /= 2;
    }
    // cout << "Count for " << N << " is " << bc << "\n";
    return (bc == count); 
}

vector<int> calcBit(int N, int digit) {
    int c = N;
    vector<int> bit(digit, 0);
    for (int i = 0; i < digit; i++) {
        bit[i] = c % 2;
        c /= 2;
    }
    return bit;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int H, W;
    cin >> H >> W;
    vector<vector<int>> A(H, vector<int>(W, 0));
    for (int h = 0; h < H; h++) {
        for (int w = 0; w < W; w++) {
            cin >> A[h][w];
        }
    }
    int H2, W2;
    cin >> H2 >> W2;
    vector<vector<int>> B(H2, vector<int>(W2, 0));
    for (int h = 0; h < H2; h++) {
        for (int w = 0; w < W2; w++) {
            cin >> B[h][w];
        }
    }

    int hMax = 1 << H;
    int wMax = 1 << W;
    
    for (int h = 0; h < hMax; h++) {
        if (!isSameBitCount(h, H2)) {
            continue;
        }
        vector<int> hBit = calcBit(h, H);
        for (int w = 0; w < wMax; w++) {
            if (!isSameBitCount(w, W2)) {
                continue;
            }
            vector<int> wBit = calcBit(w, W);
            bool canMatch = true;
            int bhi = -1;
            for (int hi = 0; hi < H; hi++) {
                if (hBit[hi] == 0) {
                    continue;
                }
                bhi++;
                int bwi = -1;
                for (int wi = 0; wi < W; wi++) {
                    if (wBit[wi] == 0) {
                        continue;
                    }
                    bwi++;
                    if (A[hi][wi] != B[bhi][bwi]) {
                        canMatch = false;
                    }
                }
            }
            if (canMatch) {
                cout << "Yes\n";
                return 0;
            }
        }
    }
    cout << "No\n";

    return 0;
}
