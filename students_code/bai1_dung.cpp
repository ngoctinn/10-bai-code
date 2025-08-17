#include <iostream>

// Lời giải đúng sử dụng thuật toán Euclid (đệ quy)
int timUCLN(int a, int b) {
    if (b == 0) {
        return a;
    }
    return timUCLN(b, a % b);
}

int main() {
    int a = 56, b = 98;
    std::cout << "UCLN cua " << a << " va " << b << " la: " << timUCLN(a, b) << std::endl;
    // Kết quả mong đợi: 14
    return 0;
}
