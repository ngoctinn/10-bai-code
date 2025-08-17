#include <iostream>

// Sai: Dùng sai toán tử
int timUCLN(int a, int b) {
    if (b == 0) {
        return a;
    }
    return timUCLN(b, a / b); // Lỗi ở đây! Phải là a % b
}

int main() {
    int a = 56, b = 98;
    std::cout << "UCLN cua " << a << " va " << b << " la: " << timUCLN(a, b) << std::endl;
    // Kết quả thực tế: Kết quả sai (ví dụ: 1)
    return 0;
}
