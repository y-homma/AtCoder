#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, K, A;
    cin >> N >> K >> A;
    int last = (A + K - 1) % N;
    if (last == 0) {
        last = N;
    }
    cout << last << "\n";


    return 0;
}
