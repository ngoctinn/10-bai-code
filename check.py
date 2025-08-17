# -*- coding: utf-8 -*-
import google.generativeai as genai
import os
import time
import pandas as pd  # Thêm thư viện pandas

# ==================== PHẦN CẤU HÌNH ====================
# 1. Dán API Key của thầy/cô vào giữa hai dấu nháy đơn.
#    Ví dụ: GOOGLE_API_KEY = 'AbCdEfGhIjKlMnOpQrStUvWxYz'
GOOGLE_API_KEY = 'AIzaSyC6_UlF2oCCEbGgRrHChZ3TWMURxuRpc8Q' # Thay YOUR_API_KEY bằng key của bạn

# 2. Tên các thư mục đã tạo ở Bước 1.
#    Thầy/cô có thể đổi tên nếu muốn.
SUBMISSIONS_DIR = 'students_code'
RESULTS_DIR = 'grading_results'

# =======================================================

# --- Bắt đầu phần logic của chương trình ---

# Hàm chính để phân tích code bằng AI
def analyze_code_with_ai(student_code_content):
    """
    Hàm này gửi code của sinh viên đến AI và nhận lại phân tích.
    """
    # Khởi tạo mô hình AI của Google
    # 'gemini-1.5-flash' là model mới, nhanh và hiệu quả về chi phí.
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # === PROMPT ĐÃ ĐƯỢC CẬP NHẬT ===
    # Thêm yêu cầu để AI trả về "Đúng" hoặc "Sai" ở dòng đầu tiên.
    prompt_template = f"""
    Bạn là một trợ giảng chấm bài lập trình C++ giàu kinh nghiệm và rất tận tâm.
    Nhiệm vụ của bạn là xem xét đoạn code tìm Ước chung lớn nhất (UCLN) của sinh viên.

    **YÊU CẦU QUAN TRỌNG:**
    Bắt đầu câu trả lời của bạn với MỘT TRONG HAI dòng sau, và chỉ một trong hai:
    - Nếu code đúng hoàn toàn về mặt logic, bắt đầu bằng: `Kết quả: Đúng`
    - Nếu code có lỗi logic, bắt đầu bằng: `Kết quả: Sai`

    Sau dòng kết quả đó, hãy đưa ra phản hồi chi tiết theo cấu trúc bên dưới.

    ---
    **Đoạn code của sinh viên:**
    ```cpp
    {student_code_content}
    ```

    **Hãy thực hiện chính xác các yêu cầu sau (nếu code sai):**

    1.  **Phân Tích Lỗi Logic (Quan trọng nhất):**
        - Chỉ ra cụ thể lỗi sai nằm ở đâu trong thuật toán.
        - Giải thích một cách rõ ràng và dễ hiểu tại sao logic đó lại sai. Hãy giải thích từng bước giá trị của các biến (a, b, r) thay đổi như thế nào qua vòng lặp để sinh viên thấy được vấn đề.

    2.  **Đề Xuất Sửa Lỗi:**
        - Cung cấp đoạn code C++ đã được sửa lại cho đúng hoàn toàn.
        - Đặt code đã sửa trong khối markdown C++.

    3.  **Đánh Giá Chung:**
        - Đưa ra một nhận xét ngắn gọn về bài làm (ví dụ: "Lỗi logic cơ bản trong việc cập nhật biến", "Sai thuật toán nghiêm trọng", "Cần xem lại cách hoạt động của thuật toán Euclid").

    Nếu code đúng, chỉ cần đưa ra một lời nhận xét ngắn gọn.
    """
    
    # Gửi yêu cầu đến AI
    response = model.generate_content(prompt_template)
    return response.text

# --- Chương trình chính ---
def main():
    """
    Hàm này sẽ lặp qua tất cả các file bài làm, gọi AI để chấm,
    và cuối cùng xuất kết quả ra một file Excel duy nhất.
    """
    print("--- CHƯƠNG TRÌNH CHẤM BÀI TỰ ĐỘNG BẰNG AI ---")

    # Cấu hình API key cho thư viện
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
    except Exception as e:
        print(f"LỖI: Cấu hình API Key thất bại. Hãy kiểm tra lại API Key của bạn.")
        print(f"Chi tiết lỗi: {e}")
        return

    # Tạo thư mục lưu kết quả nếu chưa có
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Lấy danh sách tất cả các file .cpp trong thư mục bài làm
    try:
        student_files = [f for f in os.listdir(SUBMISSIONS_DIR) if f.endswith('.cpp')]
        if not student_files:
            print(f"CẢNH BÁO: Không tìm thấy file .cpp nào trong thư mục '{SUBMISSIONS_DIR}'.")
            return
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy thư mục '{SUBMISSIONS_DIR}'. Vui lòng tạo thư mục và bỏ bài của sinh viên vào.")
        return

    print(f"Tìm thấy {len(student_files)} bài làm. Bắt đầu chấm...")

    # Tạo một danh sách rỗng để lưu trữ kết quả của tất cả sinh viên
    all_results_data = []

    # Lặp qua từng file để chấm
    for filename in student_files:
        student_id = os.path.splitext(filename)[0] # Lấy tên file (không có .cpp) làm mã sinh viên
        file_path = os.path.join(SUBMISSIONS_DIR, filename)
        
        print(f"   -> Đang chấm bài của: {student_id}...")

        try:
            # 1. Đọc nội dung file code của sinh viên
            with open(file_path, 'r', encoding='utf-8') as f:
                code_content = f.read()
            
            if not code_content.strip():
                print(f"     [CẢNH BÁO] File của {student_id} trống. Bỏ qua.")
                # Ghi nhận file trống vào kết quả
                all_results_data.append({
                    'Mã Sinh Viên': student_id,
                    'Kết quả': 'Lỗi',
                    'Lý do sai / Nhận xét': 'File code trống, không có nội dung để chấm.'
                })
                continue

            # 2. Gọi AI để phân tích
            feedback = analyze_code_with_ai(code_content)
            
            # 3. Xử lý phản hồi từ AI để tách kết quả và lý do
            lines = feedback.strip().split('\n')
            result_status = "Chưa xác định"
            reason = feedback # Mặc định lấy toàn bộ phản hồi làm lý do

            if lines:
                first_line = lines[0].strip()
                if 'Kết quả: Đúng' in first_line:
                    result_status = 'Đúng'
                    # Lấy phần còn lại làm nhận xét
                    reason = '\n'.join(lines[1:]).strip() if len(lines) > 1 else "Thuật toán chính xác."
                elif 'Kết quả: Sai' in first_line:
                    result_status = 'Sai'
                    # Lấy phần còn lại làm lý do sai
                    reason = '\n'.join(lines[1:]).strip()

            # 4. Thêm kết quả đã xử lý vào danh sách chung
            all_results_data.append({
                'Mã Sinh Viên': student_id,
                'Kết quả': result_status,
                'Lý do sai / Nhận xét': reason
            })
            
            print(f"     [HOÀN TẤT] Đã phân tích xong bài của {student_id}.")

            # Tạm dừng một chút để tránh gửi yêu cầu quá nhanh đến API
            time.sleep(1) 

        except Exception as e:
            print(f"     [LỖI] Đã có lỗi xảy ra khi xử lý file của {student_id}: {e}")
            all_results_data.append({
                'Mã Sinh Viên': student_id,
                'Kết quả': 'Lỗi hệ thống',
                'Lý do sai / Nhận xét': f"Lỗi trong quá trình chấm: {e}"
            })

    # --- SAU KHI CHẤM XONG TẤT CẢ ---
    # 5. Tạo DataFrame từ danh sách kết quả và xuất ra file Excel
    if not all_results_data:
        print("\nKhông có bài làm nào được xử lý. Kết thúc chương trình.")
        return

    try:
        print("\nĐang tổng hợp và xuất kết quả ra file Excel...")
        df = pd.DataFrame(all_results_data)
        excel_output_path = os.path.join(RESULTS_DIR, 'tong_hop_ket_qua.xlsx')
        
        # Ghi ra file Excel, index=False để không có cột số thứ tự của pandas
        df.to_excel(excel_output_path, index=False)
        
        print("\n--- ĐÃ CHẤM XONG TOÀN BỘ BÀI LÀM! ---")
        print(f"Thầy/cô vui lòng kiểm tra file Excel kết quả tại: {excel_output_path}")

    except Exception as e:
        print(f"\n[LỖI] Không thể xuất file Excel. Chi tiết lỗi: {e}")

# Lệnh này để chạy hàm main() khi file được thực thi
if __name__ == "__main__":
    main()