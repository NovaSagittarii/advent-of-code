/*

*/

#include <bits/stdc++.h>

namespace kactl {}

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
    std::vector<std::string> a;
    std::string line;
    while (std::cin >> line) a.push_back(line);
    const int n = a.size();
    const int m = a.front().size();

    int si, sj, ti, tj;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        if (a[i][j] == 'S') {
          si = i;
          sj = j;
        } else if (a[i][j] == 'E') {
          ti = i;
          tj = j;
        }
      }
    }

    const int BIG = 1e9;
    v2i ds(n, vi(m, BIG));
    v2i de = ds;

    const std::vector<std::array<int, 2>> dij {{0,-1},{-1,0},{0,1},{1,0}};

    auto Bfs = [&](int si, int sj, v2i& dp) -> void {
      std::queue<std::array<int, 2>> q;
      q.push({si, sj});
      for (int depth = 0; !q.empty(); ++depth) {
        int qn = q.size();
        while (qn--) {
          auto [i, j] = q.front();
          q.pop();
          if (a[i][j] == '#') continue; // that's a wall
          if (dp[i][j] != BIG) continue;
          dp[i][j] = depth;
          for (auto [di, dj] : dij) {
            int ni = i + di;
            int nj = j + dj;
            q.push({ni, nj});
          }
        }
      }
    };
    Bfs(si, sj, ds);
    Bfs(ti, tj, de);
    int T = ds[ti][tj];
    std::cout << "nocheat=" << T << "\n";
    std::map<int, int> cts;
    auto MinSurround = [&](int i, int j, const v2i& dp) -> int {
      int ret = BIG;
      for (auto [di, dj] : dij) {
        int ni = i + di, nj = j + dj;
        if (0 <= ni && ni < n && 0 <= nj && nj < m) setmin(ret, dp[ni][nj]);
      }
      return ret;
    };
    std::set<std::array<int, 4>> vis;
    auto Cheat = [&](int i1, int j1, int i2, int j2) -> void {
      std::array<int, 4> k = {i1, j1, i2, j2};
      if (vis.count(k)) return;
      vis.insert(k);

      int ret = T;
      if (a[i1][j1] == '#') return; // i also misread :skull:
      if (a[i2][j2] == '#') return; // ah i misread
      int res = 1 + 1 + std::abs(i1-i2) + std::abs(j1-j2) + MinSurround(i1, j1, ds) + MinSurround(i2, j2, de);
      if (i1 == si && j1 == sj) res -= 2;
      if (i2 == ti && j2 == tj) res -= 2;
      setmin(ret, res);
      if (ret != T) ++cts[T-ret];
      // if (i1 == 7 && j1 == 6) printf("save %i %i, %i %i; %i \n", i1, j1, i2, j2, T-ret);
      // if (T-ret == 64) printf("save %i %i, %i %i\n", i1, j1, i2, j2);
      // if (T-ret == 76) printf("save %i %i, %i %i\n", i1, j1, i2, j2);
    };
    for (int i = 1; i < n-1; ++i) {
      for (int j = 1; j < m-1; ++j) {
        for (int i2 = i-21; i2 <= i+21; ++i2) {
          for (int j2 = j-21; j2 <= j+21; ++j2) {
            if (i2 < 0 || i2 >= n || j2 < 0 || j2 >= m) continue;
            if (std::abs(i-i2) + std::abs(j-j2) > 20) continue;
            Cheat(i, j, i2, j2);
          }
        }
      }
    }
    for (auto [k, v] : cts) std::cout << k << ": " << v << "\n";
    int tot = 0;
    for (auto [k, v] : cts) {
      if (k >= 100) tot += v;
    }
    std::cout << tot;

    std::cout << std::endl;
  }
  return 0;
}