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
      std::map<char, std::array<int, 2>> dij = {
        {'^', {-1, 0}},
        {'>', {0, 1}},
        {'v', {1, 0}},
        {'<', {0, -1}},
      };

      typedef std::array<int, 7> node;
      std::queue<node> q;
      std::set<node> vis;
      q.push({0, 3, 2, 0, 2, 0, 2});
      auto InsertIfValid = [&](const node& u) -> void {
        auto [p, i1, j1, i2, j2, i3, j3] = u;
        // for (auto x : u) std::cerr << x << " ";
        // std::cerr << std::endl;

        if (i1 < 0 || i2 < 0 || i3 < 0) return;
        if (i1 >= 4 || i2 >= 2 || i3 >= 2) return;
        if (j1 < 0 || j2 < 0 || j3 < 0) return;
        if (j1 >= 3 || j2 >= 3 || j3 >= 3) return;
        if (a[i1][j1] == '.') return;
        if (b[i2][j2] == '.') return;
        if (b[i3][j3] == '.') return;
        q.push(std::move(u));
      };
      for (int depth = 0; !q.empty(); ++depth) {
        int qn = q.size();
        while (qn--) {
          auto k = q.front();
          q.pop();
          if (vis.count(k)) continue;
          vis.insert(k);
          auto [p, i1, j1, i2, j2, i3, j3] = k;
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
          InsertIfValid({p, i1, j1, i2, j2, i3, j3-1});
          InsertIfValid({p, i1, j1, i2, j2, i3, j3+1});
          InsertIfValid({p, i1, j1, i2, j2, i3-1, j3});
          InsertIfValid({p, i1, j1, i2, j2, i3+1, j3});

          // press A
          char c = b[i3][j3];
          if (c == 'A') {
            c = b[i2][j2];
            if (c == 'A') {
              if (s[p] == a[i1][j1]) {
                InsertIfValid({p+1, i1, j1, i2, j2, i3, j3});
              }
            } else {
              auto [di, dj] = dij[c];
              InsertIfValid({p, i1+di, j1+dj, i2, j2, i3, j3});
            }
          } else {
            auto [di, dj] = dij[c];
            InsertIfValid({p, i1, j1, i2+di, j2+dj, i3, j3});
          }
        }
      }
    }
    std::cout << ans;

    std::cout << std::endl;
  }
  return 0;
}