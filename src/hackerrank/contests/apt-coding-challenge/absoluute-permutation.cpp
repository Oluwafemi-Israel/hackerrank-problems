//https://www.hackerrank.com/contests/apt-coding-challenge/challenges/absolute-permutation


#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        if (k) {
            if (n % k == 0 && (n/k) % 2 == 0) {
                for (int i = 1; i <= n; i++) {
                    printf("%d ", i + ((i - 1) / k % 2?-k: k));
                }
                cout << endl;
            } else {
                cout << -1 << endl;
            }
        } else {
            for (int i = 1; i <= n; i++) {
                printf("%d ", i);
            }
            cout << endl;
        }
    }
    return 0;
}