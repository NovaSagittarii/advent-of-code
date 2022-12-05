#include <bits/stdc++.h>

int f(int x){
    if(x < 0) return 0;
    return std::max(0, x/3-2) + f(x/3-2);
}

int main() {
    int x;
    int sum = 0;
    while(std::cin >> x){
        int o = f(x);
        sum += o;
    }
    std::cout << sum;
    
    return 0;
}
