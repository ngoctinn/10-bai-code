#include <iostream>

// Sai: Hàm có kiểu trả về void nhưng lại cố gắng in kết quả
void timUCLN(int a, int b) {
    while (a != b) {
        if (a > b) a -= b;
        else b -= a;
    }
    // Lỗi: Không có lệnh return, nhưng kết quả tính toán bị mất
}

int main() {
    int a = 56, b = 98;
    // Lỗi biên dịch: Cố gắng in giá trị của một hàm void
    std::cout << "UCLN la: " << timUCLN(a, b) << std::endl;
    return 0;
}
