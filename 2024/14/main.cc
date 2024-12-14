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
    for (auto [x, y, dx, dy] : a) {
      x += dx*100;
      y += dy*100;
      x %= w;
      y %= h;
      x += w;
      y += h;
      x %= w;
      y %= h;
      if (x == w/2 || y == h/2) continue;
      int q = (x < w/2)*2 + (y < h/2);
      ++ans[q];
    }

    ll tot = 1;
    for (auto x : ans) {
      std::cout << x << " ";
      tot *= x;
    }
    std::cout << tot;

    std::cout << std::endl;
  }
  return 0;
}