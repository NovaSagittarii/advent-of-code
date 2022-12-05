 #include <bits/stdc++.h>

int run(std::vector<int> code, int one, int two){
    code[1] = one;
    code[2] = two;
    for(int i = 0;;i+=4){
        if(code[i] == 1){
            code[code[i+3]] = code[code[i+1]] + code[code[i+2]];
        }else if(code[i] == 2){
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]];
        }else if(code[i] == 99){
            break;
        }else{
            std::cout << "help";
            return 1;
        }
        // for(auto&x:code)std::cout <<x<<" ";std::cout<<"\n";
    }
    return code[0];
}

int main() {
    std::vector<int> code;
    int x;
    char dummy;
    while(std::cin >> x){
        code.push_back(x);
        std::cin >> dummy;
    }
    
    std::cout << run(code, 12, 2) << "\n";
    
    for(int i = 0; i <= 99; i ++){
        for(int j = 0; j <= 99; j ++){
            if(run(code, i, j) == 19690720){
                std::cout << 100*i + j << "\n";
            }
        }
    }
    
    return 0;
}
