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
    std::string line;
    std::vector<std::string> a;
    while (std::cin >> line) {
      if (line == "newline") break;
      a.push_back("");
      for (auto c : line) {
        if (c == '#') a.back() += "##";
        else if (c == 'O') a.back() += "[]";
        else if (c == '@') a.back() += "@.";
        else if (c == '.') a.back() += "..";
      }
    }
    
    std::string b;
    while (std::cin >> line) b += line;
    
    const int n = a.size();
    const int m = a[0].size();
    const int qn = b.size();
    int pi = -1, pj = -1;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        if (a[i][j] == '@') {
          pi = i;
          pj = j;
          // a[i][j] = '@';
        }
      }
    }
    
    auto OkMove = [&](int i, int j, int di, int dj, auto&& dfs) -> bool {
      if (a[i][j] == '#') return false;
      if (a[i][j] == '@') return dfs(i + di, j + dj, di, dj, dfs);
      if (a[i][j] == '[') {
        if (di) {
          return dfs(i + di, j + dj, di, dj, dfs) && dfs(i + di, j + 1 + dj, di, dj, dfs);
        } else {
          return dfs(i + di, j + dj, di, dj, dfs);
        }
      }
      if (a[i][j] == ']') {
        if (di) {
          return dfs(i + di, j + dj, di, dj, dfs) && dfs(i + di, j - 1 + dj, di, dj, dfs);
        } else {
          return dfs(i + di, j + dj, di, dj, dfs);
        }
      }
      return true; // O @
    };
    auto Push = [&](int i, int j, int di, int dj, auto&& dfs) -> void {
      // assume OKMove passed
      // if (a[i][j] == '#') return;
      if (a[i][j] == '@') {
        dfs(i + di, j + dj, di, dj, dfs);
        a[i + di][j + dj] = a[i][j];
      } else {
        if (a[i][j] == '[') {
          if (di) {
            dfs(i + di, j + dj, di, dj, dfs);
            dfs(i + di, j + 1 + dj, di, dj, dfs);
            a[i + di][j + dj] = a[i][j];
            a[i + di][j+1 + dj] = a[i][j+1];
            a[i][j+1] = a[i][j] = '.';
          } else {
            dfs(i + di, j + dj, di, dj, dfs);
            a[i + di][j + dj] = a[i][j];
          }
        }
        if (a[i][j] == ']') {
          if (di) {
            dfs(i + di, j + dj, di, dj, dfs);
            dfs(i + di, j - 1 + dj, di, dj, dfs);
            a[i + di][j + dj] = a[i][j];
            a[i + di][j-1 + dj] = a[i][j-1];
            a[i][j-1] = a[i][j] = '.';
          } else {
            dfs(i + di, j + dj, di, dj, dfs);
            a[i + di][j + dj] = a[i][j];
          }
        }
      }
      a[i][j] = '.';
    };
    
    for (auto c : b) {
      int di = 0, dj = 0;
      if (c == '<') dj = -1;
      if (c == '>') dj = 1;
      if (c == '^') di = -1;
      if (c == 'v') di = 1;
      int ni = pi + di, nj = pj + dj;
      if (a[ni][nj] == '#') continue;
      if (OkMove(ni, nj, di, dj, OkMove)) {
        Push(pi, pj, di, dj, Push);
        pi = ni;
        pj = nj;
      }
      
      // for (auto &r : a) std::cout << r << "\n";
      // std::cout << std::endl;
    }

    ll tot = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        if (a[i][j] == '[') {
          tot += i*100 + j;
        }
      }
    }
    std::cout << tot;

    std::cout << std::endl;
  }
  return 0;
}