/*
err suppose you found the best sequence 
*/

#include <bits/stdc++.h>

namespace kactl {}

typedef long long ll;
typedef std::vector<int> vi;
typedef std::vector<vi> v2i;
typedef std::vector<v2i> v3i;
#define setmax(a, b) a = std::max(a, b);
#define setmin(a, b) a = std::min(a, b);

const std::vector<std::array<int, 2>> dij {{0,-1}, {-1,0}, {0,1}, {1,0}};

int main() {
  std::ios_base::sync_with_stdio(false);
  std::cin.tie(0);

  int tn = 1;
  // std::cin >> tn; // std::cerr << "MULTITEST MODE\n";
  while (tn--) {
    // int n;
    // std::cin >> n;
    
    std::string s;
    ll ans = 0;
    while (std::cin >> s) {
      std::cout << s << std::endl;
      const std::vector<std::string> a = {
        "789",
        "456",
        "123",
        ".0A",
      };
      const std::vector<std::string> b = {
        ".^A",
        "<v>",
      };
      std::map<char, std::array<int, 2>> mdij = {
        {'^', {-1, 0}},
        {'>', {0, 1}},
        {'v', {1, 0}},
        {'<', {0, -1}},
      };

      // const int howmuchpain = 2;
      const int howmuchpain = 8; // 1 minute for 5 tests
      const int nodeSize = 1+(1+howmuchpain)*2;
      typedef std::array<int, nodeSize> node;
      std::queue<node> q;
      std::set<node> vis;
      node init;
      init[0] = 0;
      init[1] = 3;
      init[2] = 2;
      for (int i = 3; i < nodeSize; i += 2) {
        init[i] = 0;
        init[i+1] = 2;
      }
      q.push(init);
      auto InsertIfValid = [&](const node& u) -> void {
        for (int k = nodeSize-2; k > 2; k -= 2) {
          // go from the back since those change more frequently
          int i = u[k];
          int j = u[k+1];
          if (i < 0 || i >= 2) return;
          if (j < 0 || j >= 3) return;
          if (b[i][j] == '.') return;
        }
        int i1 = u[1];
        int j1 = u[2];
        if (i1 < 0 || i1 >= 4) return;
        if (j1 < 0 || j1 >= 3) return;
        if (a[i1][j1] == '.') return;
        q.push(std::move(u));
      };

      int best = 0;
      for (int depth = 0; !q.empty(); ++depth) {
        int qn = q.size();
        while (qn--) {
          auto k = q.front();
          q.pop();
          const int p = k[0];
          if (p < best) continue;
          else best = p;
          if (vis.count(k)) continue;
          vis.insert(k);
          // auto [p, i1, j1, i2, j2, i3, j3] = k;
          // std::cerr << p << "; " << i3 << " " << j3 << std::endl;
          if (p == s.size()) {
            std::cout << s << ": " << depth << std::endl;
            std::istringstream in(s);
            int w;
            in >> w;
            ans += depth * w;
            break;
          }

          // press directional
          for (auto [di, dj] : dij) {
            auto v = k;
            v[nodeSize-2] += di;
            v[nodeSize-1] += dj;
            InsertIfValid(v);
          }

          // press A
          auto dfs = [&](int lv, auto&& dfs) -> void {
            int i = k[lv];
            int j = k[lv+1];
            if (lv == 1) { // BASE CASE WOOHOO
              char c = a[i][j];
              if (s[p] == c) {
                ++k[0];
                InsertIfValid(k);
              }
            } else {
              char c = b[i][j];
              if (c == 'A') {
                dfs(lv-2, dfs);
              } else {
                auto [di, dj] = mdij[c];
                auto v = k;
                v[lv-2] += di;
                v[lv-2+1] += dj;
                InsertIfValid(v);
              }
            } 
          };
          dfs(nodeSize-2, dfs);
          // char c = b[i3][j3];
          // if (c == 'A') {
          //   c = b[i2][j2];
          //   if (c == 'A') {
          //     if (s[p] == a[i1][j1]) {
          //       InsertIfValid({p+1, i1, j1, i2, j2, i3, j3});
          //     }
          //   } else {
          //     auto [di, dj] = mdij[c];
          //     InsertIfValid({p, i1+di, j1+dj, i2, j2, i3, j3});
          //   }
          // } else {
          //   auto [di, dj] = mdij[c];
          //   InsertIfValid({p, i1, j1, i2+di, j2+dj, i3, j3});
          // }
        }
      }
    }
    std::cout << ans;

    std::cout << std::endl;
  }
  return 0;
}