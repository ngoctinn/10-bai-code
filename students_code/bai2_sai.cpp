#include <iostream>

// Sai: Điều kiện dừng đệ quy sai
int timUCLN(int a, int b) {
    if (a == 0) { // Lỗi ở đây! Phải là b == 0
        return b;
    }
    return timUCLN(b, a % b);
}

int main() {
    int a = 56, b = 98;
    std::cout << "UCLN cua " << a << " va " << b << " la: " << timUCLN(a, b) << std::endl;
    // Kết quả thực tế: 0 (sai)
    return 0;
}
