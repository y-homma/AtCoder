#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using ull = unsigned long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    set<string> S;
    const char* delim = ",";
    for (int i = 0; i < N; i++) {
        int L;
        cin >> L;
        vector<string> s(L);
        for (int j = 0; j < L; j++) {
            cin >> s[j];
        }
        ostringstream os;
        copy(s.begin(), s.end(), ostream_iterator<string>(os, delim));
        string combined = os.str();
        S.insert(combined);
    }
    cout << S.size() << "\n";


    return 0;
}
