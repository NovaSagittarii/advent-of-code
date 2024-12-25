/*
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
typedef std::vector<ll> vll;
typedef std::vector<vll> v2ll;
typedef std::vector<v2ll> v3ll;
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
    
    v3ll dp(26, v2ll(5, vll(5, -1)));
    std::vector<std::vector<std::array<int, 2>>> dadj = {
      {{1, 4}, {3, 3}}, // 0 (^)
      {{0, 2}, {4, 3}}, // 1 (A)
      {{3, 4}}, // 2 (<)
      {{0, 0}, {2, 2}, {4, 4}}, // 3 (v)
      {{1, 0}, {3, 2}}, // 4 (>)
    };
    auto dfs = [&](int lv, int s, int t, auto&& dfs) -> ll {
      // std::cout << lv << " " << s << " " << t << std::endl;
      if (lv == 0) return 1;
      if (s == t) return 1; // smack A
      if (dp[lv][s][t] != -1) return dp[lv][s][t];
      ll tot = 1e18;
      std::priority_queue<std::array<ll, 3>> pq;
      // ll tA = dfs(lv-1, t, 1, dfs); // gotta press A at the end
      pq.push({0, s, 1}); // {cost, curr_lv, lower_level}
      while (!pq.empty()) {
        auto [c, u, ppos] = pq.top();
        pq.pop();
        c *= -1;
        // if (lv == 2) std::cout << c << " " << u << " " << ppos << std::endl;
        if (u == t) {
          if (ppos == 1) {
            tot = c;
            break;
          } else {
            ll C = c + dfs(lv-1, ppos, 1, dfs);
            pq.push({-C, u, 1});
          }
        }
        for (auto [v, pos] : dadj[u]) {
          ll C = c + dfs(lv-1, ppos, pos, dfs);
          pq.push({-C, v, pos});
        }
      }
      return dp[lv][s][t] = tot;
    };

    // std::cout << dfs(1, 1, 2, dfs) << std::endl; // 4
    // std::cout << dfs(2, 1, 2, dfs) << std::endl; // 10
    // std::cout << dfs(1, 2, 1, dfs) << std::endl; // 4
    // std::cout << dfs(2, 2, 1, dfs) << std::endl; // 8
    // std::cout << dfs(2, 3, 1, dfs) << std::endl; // 7
    // std::cout << dfs(1, 4, 1, dfs) << std::endl; // 2
    // std::cout << dfs(2, 4, 1, dfs) << std::endl; // 4
    // std::cout << dfs(2, 1, 1, dfs) << std::endl; // 1
    // std::cout << dfs(2, 2, 2, dfs) << std::endl; // 1
    // continue;

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
      std::map<char, int> dpad = {
        {'^', 0},
        {'A', 1},
        {'<', 2},
        {'v', 3},
        {'>', 4},
      };
      std::map<char, std::array<int, 2>> mdij = {
        {'^', {-1, 0}},
        {'>', {0, 1}},
        {'v', {1, 0}},
        {'<', {0, -1}},
      };

      // const int howmuchpain = 2;
      const int howmuchpain = 25;
      
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
            u.push_back('A');
            // could be a while but no repeated in input
          }
          if (prog == s.size()) {
            candidate.push_back(u);
            done = true;
            continue;
            // break;
          }
          // try moving a bit
          for (auto [c, didj] : mdij) {
            auto [di, dj] = didj;
            auto uu = u;
            uu.push_back(c);
            q.push({prog, {i + di, j + dj}, uu});
          }
        }
      }

      ll tot = 1e18;
      for (auto str : candidate) {
        ll res = 0;
        int prev = dpad['A'];
        for (auto c : str) {
          res += dfs(howmuchpain, prev, dpad[c], dfs);
          prev = dpad[c];
        }
        // std::cout << str << " " << res << "\n";
        setmin(tot, res);
      }


      // for (auto x : u) tot += x;
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