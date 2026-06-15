#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int W;
    cin >> W;
    vector<int> nums;
    for (int i = 1; i < 100; i++) {
        nums.push_back(i);
        nums.push_back(i * 100);
        nums.push_back(i * 10000);
    }
    if (W == 1000000) {
        nums.push_back(1000000);
    }
    int L = nums.size();
    cout << L << "\n";
    for (int i = 0; i < L; i++) {
        cout << nums[i] << " ";
    }
    cout << "\n";

    return 0;
}
