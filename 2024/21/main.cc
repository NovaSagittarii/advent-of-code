/*

IN

6A
836A
540A
965A
480A
789A


OUT

836A
836A: 30
540A
540A: 30
965A
965A: 28
480A
480A: 30
789A
789A: 28
104792 -- 1

836A
836A: 70
540A
540A: 72
965A
965A: 66
480A
480A: 74
789A
789A: 66
248684 -- 2

8: 57386004

30 70 170 426 1050 2618
30 72 184 446 1120 2772
28 66 160 398 982 2442
30 74 182 444 1106 2734
28 66 164 396 990 2436

err suppose you found a best sequence 
can you just extend this sequence? to get a new best sequence??

i just realize that 3**25 is just NOT happening

suppose you wanted to press 1 2 3
then the alias for this is
(move to 1) A > A > A
and the alias for this... is uh
(*move to 1)
(move to A) A   <- specifically in this section YOU HAVE NO CHOICE
(move to >) A
(move to A) A
(move to >) A
(move to A) A   <- also you start on A and end on A

this move back to A makes it somewhat easier to deal with

so all you gotta do is generate a couple of tier0 path and run them
actually here's the matrix for going doing <^>vA using <^>vA

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
             ^ > v < A
^ ~ <A>      0 1 0 1 1
> ~ vA^      1 0 1 0 1
v ~ <vA^>    1 1 1 1 1
< ~ <<vA^>>  1 2 1 2 1
A ~ A        0 0 0 0 1

^ ^ A v v A

< AA >A v< AA ^> A
  ^ no need to go back here actually...

so maybe you need all pairs, a node is now...
- [KEY] -> [KEY] 
- A presses

(looked at subreddit)
oh i overlooked the top-down recurrence the entire time...
that f([pos] -> [pos], lv) can be defined in terms of
f(..., lv-1)
*/

#include <bits/stdc++.h>

namespace kactl {}

typedef long long ll;
typedef std::vector<int> vi;
typedef std::vector<vi> v2i;
typedef std::vector<v2i> v3i;
#define setmax(a, b) a = std::max(a, b);
#define setmin(a, b) a = std::min(a, b);

const std::vector<std::array<int, 2>> dij {
  {-1, 0},
  {0, 1},
  {1, 0},
  {0, -1},
};

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

      const int howmuchpain = 1;
      // const int howmuchpain = 8;
      
      typedef std::tuple<int, std::array<int, 2>, std::string> node;
      std::queue<node> q;
      q.push({0, {3, 2}, ""});
      std::vector<std::string> candidate;
      bool done = false;
      for (int depth = 0; !q.empty() && !done; ++depth) {
        int qn = q.size();
        while (qn--) {
          auto [prog, ij, u] = q.front();
          q.pop();
          auto [i, j] = ij;
          if (i < 0 || i >= 4 || j < 0 || j >= 3 || a[i][j] == '.') continue;
          if (a[i][j] == s[prog]) {
            ++prog; // yay a match
            // could be a while but no repeated in input
          }
          if (prog == s.size()) {
            candidate.push_back(u);
            done = true;
            continue;
            // break;
          }
          // try moving a bit
          for (int d = 0; d < 4; ++d) {
            auto [di, dj] = dij[d];
            auto dirs = u;
            ++dirs[d];
            q.push({prog, {i + di, j + dj}, dirs});
          }
        }
      }
      auto u = candidate[0];
      for (auto x : u) std::cout << x << " ";
      std::cout << std::endl;
      for (int i = 0; i < howmuchpain; ++i){
        /**
         *              ^ > v < A
         * ^ ~ <A>A     0 1 0 1 2
         * > ~ vA^A     1 0 1 0 2
         * v ~ <vA^>A   1 1 1 1 2
         * < ~ <<vA^>>A 1 2 1 2 2
         * A ~ A        0 0 0 0 1
         */
        auto [w, d, s, a, A] = u;
        a5int v = {
          d + s + a,
          w + s + a*2,
          d + s + a,
          w + s + a*2,
          1*(w+s+a+d) + A,
        };
        u = v;
      }

      ll tot = 0;
      for (auto x : u) tot += x;
      std::cout << s << ": " << tot << std::endl;
      std::istringstream in(s);
      int w;
      in >> w;
      ans += tot * w;
    }
    std::cout << ans;

    std::cout << std::endl;
  }
  return 0;
}