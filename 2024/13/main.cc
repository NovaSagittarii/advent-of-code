/*
Run regex on input

FIND: (Button [AB]: )|([XY][+=])|(Prize: )|,
REPLACE: 

ax + by = c
ax = c (mod b)
x = a^-1 c (mod b)

actually... im solving for...
adx x + ady y = X
bdx x + bdy y = Y

[adx ady][x] = [X]
[bdx bdy][y] = [Y]

nvm it sorta still doesnt work

https://math.stackexchange.com/questions/19528/integer-matrices-with-integer-inverses

ah i wrote the matrix wrong...
[adx bdx][a] = [X]
[ady bdy][b] = [Y]
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
    ll tot = 0;
    
    ll adx, ady, bdx, bdy, X, Y;
    while (std::cin >> adx >> ady >> bdx >> bdy >> X >> Y) {
      X += 10000000000000;
      Y += 10000000000000;
      
      ll a = adx, b = ady, c = bdx, d = bdy;
      std::swap(b, c); // oops
      ll det = a*d - b*c;
      ll ai = d, bi = -b, ci = -c, di = a;
      if (det == 0) {
        std::cout << "fail\n"; continue;
      }
      ll x = (ai * X + bi * Y);// / det;
      ll y = (ci * X + di * Y);// / det;
      // std::cout << std::fixed << std::setprecision(2);
      // std::cout << x << " " << y << "\n";
      if (x % det == 0 && y % det == 0) {
        x/=det; y/=det;
        std::cout << x << " " << y << "\n";
        tot += 3*x + y;
      } else std::cout<<"no\n";
    }
    std::cout << tot;
    

    std::cout << std::endl;
  }
  return 0;
}