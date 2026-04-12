#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M;
    cin >> N >> M;
    vector<int> ty(M, 0), ny(M, 0);
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        ty[a-1] += 1;
        ny[b-1] += 1;
    }
    for (int i = 0; i < M; i++) {
        cout << ny[i] - ty[i] << "\n";
    }
    
    return 0;
}
