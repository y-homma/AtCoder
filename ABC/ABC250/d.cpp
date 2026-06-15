#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll N;
    cin >> N;
    vector<int> primes;
    vector<bool> isPrime(1000001, true);
    for (ll i = 2; i < 1000001; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
            int ci = i * 2;
            while (ci < 1000001) {
                isPrime[ci] = false;
                ci += i;
            }
        }
    }

    int ans = 0;
    int L = primes.size();
    for (int i = 0; i < L; i++) {
        int q = i + 1;
        ll p = primes[i];
        bool isSmall = true;
        while (q < L && isSmall) {
            // cout << "P: " << p << " Q: " << primes[q] << "\n";
            double est = 1;
            ll pq = primes[q];
            est = (pq * pq * pq);
            est *= p;
            if (est > 4e18) {
                isSmall = false;
            } else {
                if (pq * pq * pq * p <= N) {
                    ans += 1;
                    q += 1;
                } else {
                    isSmall = false;
                }
            }
        }
    }
    cout << ans << "\n";

    return 0;
}
