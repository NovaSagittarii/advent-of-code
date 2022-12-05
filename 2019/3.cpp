 #include <bits/stdc++.h>

int main() {
    std::vector<int> code;
    int amt;
    char dir, dummy;
    int x = 0, y = 0, wire = 1;
    int distance = 0;
    int small = 1e9;
    std::unordered_map<int, int> v;
    while(std::cin >> dir >> amt){
        int dx = 0, dy = 0;
        if(dir == 'R') dx = 1;
        if(dir == 'L') dx = -1;
        if(dir == 'U') dy = -1;
        if(dir == 'D') dy = 1;
        
        for(int i = 1; i <= amt; i ++){
            distance ++;
            x += dx;
            y += dy;
            int k = x*2e5 + (y+1e5);
            int z = dx != 0 ? 1 : 2;
            // std::cout << x << " " << y << " \n";
            
            if(v[k] > 0 && wire > 1){
                int candidate = v[k] + distance; // std::abs(x) + std::abs(y);
                std::cout << x << " " << y << " " << candidate << "\n";
                small = std::min(small, candidate);
            }
            if(wire == 1 && v[k] == 0){
                v[k] = distance;
            }
        }
        
        std::cin.get(dummy);
        // std::cout << "("<<dummy<<")";
        if(dummy == '\n'){
            x = 0;
            y = 0;
            wire ++;
            distance = 0;
        }
    }
    std::cout << small;
    
    return 0;
}
