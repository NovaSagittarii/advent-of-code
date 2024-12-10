/*

*/

#include <bits/stdc++.h>

namespace kactl {

}

typedef long long ll;
typedef std::vector<int> vi;
typedef std::vector<vi> v2i;
typedef std::vector<v2i> v3i;
#define setmax(a, b) a = std::max(a, b);
#define setmin(a, b) a = std::min(a, b);

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);

  int tn = 1;
  // std::cin >> tn; // std::cerr << "MULTITEST MODE\n";
  while (tn--) {
    v2i a;
    std::string line;
    while (std::cin >> line) {
      a.push_back({});
      for (auto c : line) a.back().push_back(c-'0');
    }

    const int n = a.size();
    const int m = a[0].size();
    std::vector<std::vector<std::array<int, 2>>> pos(10);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        int x = a[i][j];
        pos[x].push_back({i, j});
      }
    }
    int tot = 0;
    const static std::vector<std::array<int, 2>> dij = {
      {0, 1}, {1, 0}, {0, -1}, {-1, 0}
    };
    for (auto [i, j] : pos[0]) {
      v2i vis(n, vi(m));

      auto dfs = [&](int i, int j, auto&& dfs) -> void {
        if (vis[i][j]) return;
        vis[i][j] = 1;
        if (a[i][j] == 9) ++tot;
        for (auto [di, dj] : dij) {
          int ni = i + di, nj = j + dj;
          if (ni >= 0 && ni < n && nj >= 0 && nj < m) {
            if (a[ni][nj] == a[i][j] + 1) {
              dfs(ni, nj, dfs);
            }
          }
        }
      };

      dfs(i, j, dfs);
    }
    std::cout << tot;

    std::cout << std::endl;
  }
  return 0;
}