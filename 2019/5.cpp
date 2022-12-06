#include <bits/stdc++.h>

int run(std::vector<int> code, std::deque<int> &stdin, std::vector<int> &stdout){
    // code[1] = one;
    // code[2] = two;
    for(int i = 0;;){
        int opcode = code[i]%100;
        int m1 = 1 ^ (code[i]/100%10);
        int m2 = 1 ^ (code[i]/1000%10);
        int m3 = 1 ^ (code[i]/10000%10);
        int *p1 = &code[m1 ? code[i+1] : i+1];
        int *p2 = nullptr;
        if(opcode != 3 && opcode != 4 && opcode != 99) p2 = &code[m2 ? code[i+2] : i+2];
        // std::cout << code[i] << " " << m3 << m2 << m1 << opcode << "\n";
        // for(int &x:code)std::cout<<x<<" ";std::cout <<"\n";
        switch(opcode){
            case 1:
                code[m3 ? code[i+3] : i+3] = code[m1 ? code[i+1] : i+1] + code[m2 ? code[i+2] : i+2];
                i+=4;
                break;
            case 2:
                code[m3 ? code[i+3] : i+3] = code[m1 ? code[i+1] : i+1] * code[m2 ? code[i+2] : i+2];
                i+=4;
                break;
            case 3:
                *p1 = stdin.front();
                i+=2;
                stdin.pop_front();
                break;
            case 4:
                stdout.push_back(*p1);
                i+=2;
                break;
            case 5:
                i = *p1 != 0 ? *p2 : i+3;
                break;
            case 6:
                i = *p1 == 0 ? *p2 : i+3;
                break;
            case 7:
                code[m3 ? code[i+3] : i+3] = *p1 < *p2;
                i+=4;
                break;
            case 8:
                code[m3 ? code[i+3] : i+3] = *p1 == *p2;
                i+=4;
                break;
            case 99:
                return code[0];
                break;
            default:
                std::cout << "help";
                std::exit(1);
        }
    }
    return code[0];
}

int main() {
    std::deque<int> stdin;
    std::vector<int> code, stdout;
    int x;
    char dummy;
    while(std::cin >> x){
        code.push_back(x);
        std::cin >> dummy;
    }
    
    stdin.push_back(5);
    std::cout << run(code, stdin, stdout) << "\n";
    std::cout << "Output: ";
    for(auto &x:stdout) std::cout << x << " ";
    
    /* std::cout << run(code, 12, 2) << "\n";
    
    for(int i = 0; i <= 99; i ++){
        for(int j = 0; j <= 99; j ++){
            if(run(code, i, j) == 19690720){
                std::cout << 100*i + j << "\n";
            }
        }
    }*/
    
    return 0;
}
