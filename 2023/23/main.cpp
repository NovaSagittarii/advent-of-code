#include <bits/stdc++.h>

int32_t main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);
    
    std::vector<std::string> grid;
    std::string line;
    while(std::cin >> line) grid.push_back(line);
    
    const int n = grid.size();
    const int m = n ? grid.front().size() : 0;
    
    std::vector<std::array<int, 2>> directions = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    
    std::vector<bool> vis(n*m);
    std::vector<std::map<int, int>> adj(n*m);
    const auto ctk = [m](const int i, const int j) -> int {
        return i*m + j;
    };
    const auto kti = [m](const int k) -> int {
        return k / m;
    };
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == '#') continue; // cannot be connected
            for (auto [di, dj] : directions) {
                int ni = i + di;
                int nj = j + dj;
                if (0 <= ni && ni < n && 0 <= nj && nj < m) {
                    if (grid[ni][nj] == '#') continue;
                    adj[ctk(i, j)][ctk(ni, nj)] = 1;
                }
            }
        }
    }
    
    // edge contraction
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            const int u = ctk(i, j);
            auto& neighbors = adj[u];
            if (neighbors.size() == 2) {
                const auto [s, su] = *(neighbors.begin());
                const auto [t, ut] = *(++neighbors.begin());
                const int st = su + ut;
                adj[s].erase(u);
                adj[s][t] = st;
                adj[t].erase(u);
                adj[t][s] = st;
            }
        }
    }
    
    int ans = 0;
    auto dfs = [&](int u, int depth, auto&& dfs) -> void {
        if (vis[u]) return;
        vis[u] = true;
        if (kti(u) == n-1) ans = std::max(ans, depth);
        for (auto [v, weight] : adj[u]) {
            dfs(v, depth + weight, dfs);
        }
        vis[u] = false;
    };
    dfs(ctk(0, 1), 0, dfs);
    
    std::cout << ans;
    std::cout << std::endl;
    return 0;
}