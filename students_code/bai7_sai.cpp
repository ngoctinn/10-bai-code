#include <iostream>

// Sai: Không xử lý đầu vào là số âm
int timUCLN(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int a = -56, b = 98;
    std::cout << "UCLN cua " << a << " va " << b << " la: " << timUCLN(a, b) << std::endl;
    // Kết quả thực tế: -14 (sai, UCLN luôn là số dương)
    return 0;
}
