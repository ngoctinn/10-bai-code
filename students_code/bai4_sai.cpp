#include <iostream>

// Sai: Tham số trong lời gọi đệ quy bị sai thứ tự
int timUCLN(int a, int b) {
    if (b == 0) {
        return a;
    }
    return timUCLN(a, a % b); // Lỗi ở đây! Phải là timUCLN(b, a % b)
}

int main() {
    int a = 56, b = 98;
    std::cout << "UCLN cua " << a << " va " << b << " la: " << timUCLN(a, b) << std::endl;
    // Kết quả thực tế: Lặp vô hạn dẫn đến tràn bộ nhớ stack (stack overflow)
    return 0;
}
