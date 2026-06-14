data = [
    ("Levi", 120, 2500),      # Dữ liệu chuẩn
    ("SofM", 150),            # Lỗi API: Bị thiếu mất trường MMR (Tuple chỉ có 2 phần tử)
    ("Optimus", 100, "N/A")   # Lỗi dữ liệu: Điểm MMR bị ghi chữ "N/A"
]

# Hàm xử lý dồn cục, không có cơ chế bẫy lỗi
def process(ds):
    print("--- BẢNG TÍNH THƯỞNG RP ---")
    for p in ds:
        t = p[0]
        m = p[1]
        r = p[2]  # Lấy điểm MMR
        
        # Tính toán tiền thưởng
        b = (m * 10) + (int(r) * 0.5)
        print("Tuyển thủ", t, "nhận được", b, "RP")

# Chạy hệ thống
process(data)