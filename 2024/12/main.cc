/*

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
    std::vector<std::string> a;
    std::string line;
    while (std::cin >> line) a.push_back(line);
    const int n = a.size();
    const int m = a[0].size();

    kactl::UF dsu(n*m);
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        for (auto [di, dj] : dij) {
          int ni = i + di, nj = j + dj;
          if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
          if (a[i][j] == a[ni][nj]) {
            int k = i*m + j;
            int nk = ni*m + nj;
            dsu.join(k, nk);
          }
        }
      }
    }
    std::map<int, int> peri;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        int k = i*m + j;
        for (auto [di, dj] : dij) {
          int ni = i + di, nj = j + dj;
          if (ni < 0 || ni >= n || nj < 0 || nj >= m) {
            ++peri[dsu.find(k)];
            ++peri[dsu.find(k)];
          } else if (a[i][j] != a[ni][nj]) {
            int nk = ni*m + nj;
            ++peri[dsu.find(k)];
            ++peri[dsu.find(nk)];
          }
        }
      }
    }

    ll tot = 0;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        int k = i*m + j;
        if (dsu.find(k) == k) {
          peri[k] /= 2;
          tot += dsu.size(k) * peri[k];
          std::cout << a[i][j] << "; ";
          std::cout << dsu.size(k) << " * " <<  peri[k];
          std::cout << " = " << dsu.size(k) * peri[k] << "\n";
        }
      }
    }
    std::cout << tot;

    std::cout << std::endl;
  }
  return 0;
}