ticket_db = [
    {"ticket_id": "T01", "buyer_name": "Nguyen Van A", "price": 500.0, "status": "Booked", "seat": ("A", 1)},
    {"ticket_id": "T02", "buyer_name": "Tran Thi B", "price": 300.0, "status": "Cancelled", "seat": ("B", 5)},
    {"ticket_id": "T03", "buyer_name": "Le Van C", "price": 500.0, "status": "Booked", "seat": ("C", 5)}
]

import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
    filename = 'app.logaa',
    filemode = 'w'

)

def display_ticket(ticket):
    if len(ticket) == 0:
        print("Dữ liệu hiện đang trống!")
        return
    else:
        print("--- DANH SÁCH VÉ ---")
        print("Mã vé | Tên khách hàng  | Giá vé | Chỗ ngồi  | Trạng thái  ")
        print("-" * 50 )
        try: 
            for tick in ticket:
                print(f"{tick['ticket_id']:<6}| {tick['buyer_name']:<15} | {tick['price']:<5}| {tick['seat'][0]}-{tick['seat'][1]} | {tick['status']} {'[Đã Hủy]' if tick['status'] == "Cancelled" else ""}")
        except(KeyError):
            print("Lỗi: Một vé đang bị thiếu dữ liệu, vui lòng kiểm tra lại.")
            logging.error("Missing key while displaying ticket: 'seat'")
        print("-" * 50 )
        logging.info("User viewed ticket list")

def is_duplicateID(id):
    for item in ticket_db:
        if item['ticket_id'] == id:
            return True
    return None

def validate_data_input(promt : str , type = "str"):
    if promt == "":
        print("Dữ liệu không được để trống!Vui lòng nhập lại!")
        return 
    if type == "int":
        try:
            promt = int(promt)
        except (ValueError,TypeError):
            print("Giá vé và số ghế phải là số vui lòng nhập lại!")
            return
    return True
    

def book_ticket():
    is_valid = False
    while True:
        id_input = input("Nhập vào ID vé: ").strip().upper()
        is_valid = validate_data_input(id_input)
        is_duplicate = is_duplicateID(id_input)
        if is_valid:
            if is_duplicate:
                print("Lỗi mã vé đã tồn tại!")
                logging.warning("Mã vé đã tồn tại")
                continue
            break
    while True:
        name_input = input("Nhập vào tên người mua: ").strip().title()
        is_valid = validate_data_input(name_input)
        if is_valid:
            break
    while True:
        price_input = input("Nhập vào giá vé: ")
        is_valid = validate_data_input(price_input,"int")
        if is_valid:
            break
    while True:
        area_input = input("Nhập vào khu vực(chữ cái): ").strip().upper()
        is_valid = validate_data_input(area_input)
        if is_valid:
            break
    while True:
        number_seat =  input("Nhập vào số ghế: ")
        is_valid = validate_data_input(number_seat,"int")
        if is_valid:
            break
    tick_new_book = {"ticket_id": id_input, "buyer_name": name_input, "price": price_input, "status": "Booked", "seat": (area_input, number_seat)}
    ticket_db.append(tick_new_book)
    logging.info(f"Book Newticket {id_input} for {name_input}")

def change_seat(tickets):
    is_valid = False
    
    while True:
        change_id = input("Nhập vào id cần đổi chỗ: ").strip().upper()
        is_valid = validate_data_input(change_id)
        is_search_id = is_duplicateID(change_id)
        if is_valid:
            break
    if is_search_id:
        while True:
            change_area = input("Nhập vào khu vực(chữ cái): ").strip().upper()
            is_valid = validate_data_input(change_area)
            if is_valid:
                break
        while True:
            change_number_seat =  input("Nhập vào số ghế: ")
            is_valid = validate_data_input(change_number_seat,"int")
            if is_valid:
                break
        for item in tickets:
            if item['ticket_id'] == change_id:
                item['seat'] = (change_area,change_number_seat)
                print(f"Thành công đã đổi vé {change_id} sang {change_area}-{change_number_seat}")
                logging.info(f"Seat changed for ticket {change_id} to {change_area}-{change_number_seat}")
    else:
        print("không tìm thấy mã vé!")
        
def cancel_ticket(tickets):
    print("\n--- HỦY VÉ ---")
    cancel_id = input("Nhập mã vé cần hủy: ").strip().upper()

    for item in tickets:
        if item['ticket_id'] == cancel_id:
            if item['status'] == "Cancelled":
                print(f"Vé {cancel_id} đã ở trạng thái Cancelled trước đó.")
                return

            item['status'] = "Cancelled"
            print(f"Thành công: Vé {cancel_id} đã được hủy.")
            logging.warning(f"Ticket {cancel_id} has been cancelled.")
            return

    print(f"Không tìm thấy vé mang mã {cancel_id}.")
    logging.warning(f"Cancel ticket failed - Ticket {cancel_id} not found")


def calculate_revenue(tickets):
    print("\n--- BÁO CÁO DOANH THU ---")

    total_revenue = 0.0
    total_booked = 0
    total_cancelled = 0

    try:
        for item in tickets:
            if item['status'] == "Booked":
                total_booked += 1
                total_revenue += float(item['price'])

            elif item['status'] == "Cancelled":
                total_cancelled += 1

        print(f"Tổng số vé đã đặt: {total_booked}")
        print(f"Tổng số vé đã hủy: {total_cancelled}")
        print(f"Tổng doanh thu hợp lệ: {total_revenue}")

        logging.info(
            f"Revenue report generated. Total: {total_revenue}"
        )

    except KeyError as e:
        print("Lỗi: Một vé đang bị thiếu dữ liệu doanh thu.")
        print("Tổng doanh thu hợp lệ: 0.0")
        logging.error(f"Missing key while calculating revenue: {e}")



while True:
    menu_title = "HỆ THỐNG QUẢN LÝ VÉ RIKKEI ESPORTS".center(50,"=")
    user_choice = input(f"""
{menu_title}
1. Xem danh sách vé đã bán
2. Đặt vé mới
3. Đổi chỗ ngồi (Cập nhật vé)
4. Hủy vé
5. Báo cáo doanh thu
6. Thoát chương trình
{"=" * len(menu_title)}
Chọn chức năng (1-6): """)
    match user_choice:
        case "1":
            display_ticket(ticket_db)
        case "2":
            book_ticket()
        case "3":
            change_seat(ticket_db)
        case "4":
            cancel_ticket(ticket_db)
        case "5":
            calculate_revenue(ticket_db)
        case "6":
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            logging.info("User exited the program.")
            break # Thoát vòng lặp để đóng chương trình và ghi log vào file
        case _:
            if user_choice in ["2", "3", "4", "5"]:
                print(f"\nChức năng {user_choice} đang được phát triển.")
            else:
                print("\nLựa chọn không hợp lệ, vui lòng nhập từ 1-6!")
                logging.warning("Lỗi lựa chọn không hợp lệ vui lòng chọn lại!")