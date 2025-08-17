#include <iostream>

// Sai: Logic cập nhật biến trong thuật toán Euclid lặp bị sai
int timUCLN(int a, int b) {
    while (b != 0) {
        int r = a % b;
        b = a; // Lỗi: Gán sai giá trị. Phải gán a = b
        a = r; // Lỗi: Gán sai giá trị. Phải gán b = r
    }
    return a;
}

int main() {
    int a = 56, b = 98;
    std::cout << "UCLN cua " << a << " va " << b << " la: " << timUCLN(a, b) << std::endl;
    // Kết quả thực tế: 0 (sai)
    return 0;
}
