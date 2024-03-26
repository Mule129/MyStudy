#include <iostream>

// #include "sum2.cpp"
// #include "sub2.cpp"
// #include "mul2.cpp"
// #include "div2.cpp"

int sum2(int, int);
int sub2(int, int);
int mul2(int, int);
int div2(int, int);


int main() {
    int a, b;
    std::cout << "A: ";
    std::cin >> a;
    std::cout << "B: ";
    std::cin >> b;

    std::cout << "50 + 20 = " << sum2(a, b) << std::endl;
    std::cout << "50 - 20 = " << sub2(a, b) << std::endl;
    std::cout << "50 * 20 = " << mul2(a, b) << std::endl;
    std::cout << "50 / 20 = " << div2(a, b) << std::endl;
    
    return 0;
}