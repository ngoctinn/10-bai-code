# 10-bai-code Tool

## Mục đích

Tool này được sử dụng để tự động kiểm tra, chấm điểm và tổng hợp kết quả các bài code của sinh viên. Hệ thống hỗ trợ kiểm tra nhiều bài tập lập trình (ví dụ: C++, Python, ...) và xuất kết quả tổng hợp ra file Excel.

## Cấu trúc thư mục

- `check.py`: Script chính để kiểm tra và chấm điểm các bài code.
- `requirements.txt`: Danh sách các thư viện Python cần cài đặt.
- `students_code/`: Thư mục chứa các file code của sinh viên (ví dụ: `bai1_dung.cpp`, `bai2_sai.cpp`, ...).
- `grading_results/`: Thư mục chứa kết quả chấm điểm, bao gồm file tổng hợp `tong_hop_ket_qua.xlsx`.

## Hướng dẫn sử dụng

1. **Dán danh sách bài tập vào `students_code`**

2. **Cài đặt thư viện**

   ```bash
   pip install -r requirements.txt
   ```

3. **Chạy tool kiểm tra**

   ```bash
   python check.py
   ```

4. **Kết quả**
   - Kết quả chấm điểm sẽ được lưu trong thư mục `grading_results/` dưới dạng file Excel.

## Ghi chú

- Đảm bảo các file code của sinh viên được đặt đúng tên và đúng thư mục `students_code/`.
- Có thể cần chỉnh sửa `check.py` để phù hợp với yêu cầu cụ thể của từng bài tập hoặc tiêu chí chấm điểm.

## Liên hệ

- Tác giả: ngoctinn
- Ngày cập nhật: 17/08/2025
