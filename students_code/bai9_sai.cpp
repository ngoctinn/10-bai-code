// Sai: Thiếu thư viện cần thiết

int timUCLN(int a, int b) {
    if (b == 0) return a;
    return timUCLN(b, a % b);
}

int main() {
    int a = 56, b = 98;
    // Lỗi biên dịch: 'std' và 'cout' không được định nghĩa
    std::cout << "UCLN la: " << timUCLN(a, b) << std::endl;
    return 0;
}
