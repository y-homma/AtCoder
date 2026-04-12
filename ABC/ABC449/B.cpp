#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int H, W, Q;
    cin >> H >> W >> Q;
    int c;
    int q;
    for (int i = 0; i < Q; i++){
        cin >> c;
        cin >> q;
        if (c == 1) {
            cout << q * W << endl;
            H -= q;
        } else {
            cout << q * H << endl;
            W -= q;
        }
    }

    return 0;
}
