/*
Run regex on input

FIND: (Button [AB]: )|([XY][+=])|(Prize: )|,
REPLACE: 
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

struct UF {
	vi e;
	UF(int n) : e(n, -1) {}
	bool sameSet(int a, int b) { return find(a) == find(b); }
	int size(int x) { return -e[find(x)]; }
	int find(int x) { return e[x] < 0 ? x : e[x] = find(e[x]); }
	bool join(int a, int b) {
		a = find(a), b = find(b);
		if (a == b) return false;
		if (e[a] > e[b]) swap(a, b);
		e[a] += e[b]; e[b] = a;
		return true;
	}
};

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
    ll tot = 0;
    
    int adx, ady, bdx, bdy, X, Y;
    while (std::cin >> adx >> ady >> bdx >> bdy >> X >> Y) {
      int MAX = X+Y+5;
      int best = MAX;
      for (int a = 0; a*adx <= X; ++a) {
        if (a > 100) continue;
        int ax = a*adx;
        for (int b = 0; ax+b*bdx <= X; ++b) {
          if (b > 100) continue;
          int x = ax + b*bdx;
          int y = a*ady + b*bdy;
          if (x == X && y == Y) {
            setmin(best, 3*a+b);
          }
        }
      }
      std::cout << best << "\n";
      if (best != MAX) tot += best;
    }
    std::cout << tot;
    

    std::cout << std::endl;
  }
  return 0;
}