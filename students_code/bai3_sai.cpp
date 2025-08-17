#include <iostream>

// Sai: Logic sai trong vòng lặp while
int timUCLN(int a, int b) {
    while (a = b) { // Lỗi ở đây! Đây là phép gán, không phải so sánh
        if (a > b) {
            a = a - b;
        } else {
            b = b - a;
        }
    }
    return a;
}

int main() {
    int a = 56, b = 98;
    std::cout << "UCLN cua " << a << " va " << b << " la: " << timUCLN(a, b) << std::endl;
    // Kết quả thực tế: Chạy vô tận hoặc kết quả không đoán trước được
    return 0;
}
