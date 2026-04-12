#include <bits/stdc++.h>
using namespace std;
using ll = long long;

// Player1勝利: 0, Player2勝利1, 引き分け-1
int fight(char player1, char player2) {
    if (player1 == player2) {
        return -1;
    } else if (player1 == 'G') {
        return player2 == 'C' ? 0 : 1;
    } else if (player1 == 'C') {
        return player2 == 'P' ? 0 : 1;
    } else {
        return player2 == 'G' ? 0 : 1;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int N, M;
    cin >> N >> M;
    vector<string> A(2 * N);
    vector<int> wins(2*N, 0);
    for (int i = 0; i < 2 * N; i++) {
        cin >> A[i];
    }

    vector<vector<int>> rank(2*N, vector<int>(2));
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < 2*N; j++) {
            rank[j] = {wins[j], j};
        }
        sort(rank.begin(), rank.end(), [](const vector<int> &x, vector<int> &y) {
            if (x[0] != y[0]) {
                return x[0] > y[0];
            }
            return x[1] < y[1];
        });
        for (int j = 0; j < N; j++) {
            int fi = rank[2*j][1];
            int si = rank[2*j+1][1];
            int win = fight(A[fi].at(i), A[si].at(i));
            if (win == 0) {
                wins[fi] += 1;
            } else if (win == 1) {
                wins[si] += 1;
            }
        }
    }

    for (int j = 0; j < 2*N; j++) {
        rank[j] = {wins[j], j};
    }
    sort(rank.begin(), rank.end(), [](const vector<int> &x, vector<int> &y) {
        if (x[0] != y[0]) {
            return x[0] > y[0];
        }
        return x[1] < y[1];
    });
    
    for (auto r : rank) {
        cout << r[1] + 1 << "\n";
    }


    return 0;
}
