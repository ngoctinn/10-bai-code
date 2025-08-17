#include <iostream>

// Sai: Logic duyệt ngược để tìm ước chung
int timUCLN(int a, int b) {
    int uocChung = 1;
    int minVal = (a < b) ? a : b;
    for (int i = minVal; i >= 1; i--) {
        if (a % i == 0 && b % i == 0) {
            uocChung = i; // Lỗi: Gán giá trị nhưng không dừng lại
        }
    }
    return uocChung; // Sẽ luôn trả về 1
}

int main() {
    int a = 56, b = 98;
    std::cout << "UCLN cua " << a << " va " << b << " la: " << timUCLN(a, b) << std::endl;
    // Kết quả thực tế: 1
    return 0;
}
