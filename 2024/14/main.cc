/*
FIND [pv=,]
REPLACE 
*/

#include <bits/stdc++.h>

namespace kactl {

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

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

  const std::vector<std::array<int, 2>> dij = {
    {0, 1}, {1, 0}, {0, -1}, {-1, 0}
  };

  int tn = 1;
  // std::cin >> tn; // std::cerr << "MULTITEST MODE\n";
  while (tn--) {
    std::vector<std::array<int, 4>> a;
    int x, y, dx, dy;
    while (std::cin >> x >> y >> dx >> dy) a.push_back({x, y, dx, dy});
    std::vector<int> ans(4, 0);

    const int w = 101, h = 103;
    int best = 0;
    v2i b(h, vi(w, -1));
    for (int T = 0; T < 1000000; ++T) {
      if ((T&2047) == 2047) {
        std::cerr << T << " ";
        std::cerr << best << std::endl;
      }
      // do 500*500 check
      int near = 0;
      for (auto [x, y, dx, dy] : a) {
        x += dx*T;
        y += dy*T;
        x %= w;
        y %= h;
        x += w;
        y += h;
        x %= w;
        y %= h;
        b[y][x] = T;
        if (x-1 >= 0 && b[y][x-1] == T && x+1 < w && b[y][x+1] == T) ++near;
        // if (x+1 < w && b[y][x+1] == T) ++near;
        // if (y-1 >= 0 && b[y-1][x] == T) ++near;
        // if (y+1 < h && b[y+1][x] == T) ++near;
      }
      setmax(best, near);
      if (near < 60) continue;
      std::cout << "ok=" << near << "\n";

      std::cout << T << "\n";
      for (int i = 0; i < h; ++i) {
        for (int j = 0; j < w; ++j) {
          char c = ' ';
          if (b[i][j] == T) c = '#';
          std::cout << c;
        }
        std::cout << "\n";
      }
      std::cout << std::endl;
    }

    std::cout << std::endl;
  }
  return 0;
}