import os
from pypdf import PdfReader

def extract_text(pdf_path):
    # 1. Kiểm tra xem file có tồn tại không
    if not os.path.exists(pdf_path):
        return f"Lỗi: Không tìm thấy file {pdf_path}"

    try:
        # 2. Mở file PDF
        reader = PdfReader(pdf_path)
        full_text = ""

        # 3. Duyệt qua từng trang để lấy chữ
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text = page.extract_text()
            if text:
                full_text += f"\n--- Trang {i+1} ---\n" + text
        
        return full_text

    except Exception as e:
        return f"Lỗi khi đọc file: {str(e)}"

if __name__ == "__main__":
    # Đường dẫn tới file bạn vừa chuẩn bị
    file_name = "sample.pdf" 
    
    print(f"Đang đọc file: {file_name}...")
    result = extract_text(file_name)
    
    # In kết quả ra màn hình
    print(result)

    # (Tùy chọn) Lưu kết quả ra file txt để kiểm tra
    with open("extracted_text.txt", "w", encoding="utf-8") as f:
        f.write(result)
    print("\n✅ Đã trích xuất xong! Kiểm tra file 'extracted_text.txt' nhé.")
    