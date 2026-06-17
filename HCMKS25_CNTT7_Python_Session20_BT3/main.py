import logging

# ================= LOGGING CONFIG =================
logging.basicConfig(
    filename="tournament_app.log",
    level=logging.INFO,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s'
)

# ================= DATA =================
match_list = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]


# ================= HELPERS =================
def find_match(match_id):
    for match in match_list:
        if match.get("match_id") == match_id:
            return match
    return None


def determine_winner(match):
    """
    Trả về đội thắng hoặc trạng thái trận đấu.

    Args:
        match (dict): thông tin trận đấu

    Returns:
        str: tên đội thắng / Draw / Pending
    """
    if match.get("status") == "Pending":
        return "Not Started"

    score_a = match.get("score_a", 0)
    score_b = match.get("score_b", 0)

    if score_a > score_b:
        return match["team_a"]
    elif score_b > score_a:
        return match["team_b"]
    else:
        return "Draw"


# ================= FUNCTION 1 =================
def display_matches(matches):
    """Hiển thị danh sách trận đấu"""
    if not matches:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print("Mã trận | Đội A | Đội B | Tỷ số | Trạng thái")
    print("-" * 60)

    for match in matches:
        print(
            f"{match['match_id']} | "
            f"{match['team_a']} | "
            f"{match['team_b']} | "
            f"{match['score_a']}-{match['score_b']} | "
            f"{match['status']}"
        )

    logging.info("User viewed the match list.")


# ================= FUNCTION 2 =================
def add_match():
    """Thêm trận đấu mới"""
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")

    match_id = input("Nhập mã trận đấu: ").strip()
    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()

    if not match_id:
        print("Mã trận đấu không được để trống.")
        logging.warning("User tried to add empty match ID.")
        return

    if not team_a or not team_b:
        print("Tên đội không được để trống.")
        logging.warning("User tried to add empty team name.")
        return

    if find_match(match_id):
        print(f"Lỗi: Mã trận đấu {match_id} đã tồn tại.")
        logging.warning(f"Match ID {match_id} already exists.")
        return

    match_list.append({
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    })

    print(f"Thành công: Đã thêm trận đấu {match_id}.")
    logging.info(f"Match {match_id} added successfully")


# ================= FUNCTION 3 =================
def update_score():
    """Cập nhật tỷ số trận đấu"""
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")

    match_id = input("Nhập mã trận đấu cần cập nhật: ").strip()
    match = find_match(match_id)

    if not match:
        print("Không tìm thấy trận đấu.")
        logging.warning(f"User tried to update non-existing match {match_id}")
        return

    print(f"{match['team_a']} vs {match['team_b']} ({match['status']})")

    # ===== INPUT SCORE A =====
    while True:
        try:
            score_a = int(input("Nhập điểm Đội A: "))
            if score_a < 0:
                raise ValueError("Negative score")
            break
        except ValueError as e:
            print("Điểm số phải là số nguyên >= 0.")
            logging.error(f"Invalid score input: {e}")

    # ===== INPUT SCORE B =====
    while True:
        try:
            score_b = int(input("Nhập điểm Đội B: "))
            if score_b < 0:
                raise ValueError("Negative score")
            break
        except ValueError as e:
            print("Điểm số phải là số nguyên >= 0.")
            logging.error(f"Invalid score input: {e}")

    # ===== LOGIC EDGE CASE 0-0 =====
    if score_a == 0 and score_b == 0:
        confirm = input("0-0. Xác nhận hoàn thành? (y/n): ").lower()
        if confirm != "y":
            match["score_a"] = score_a
            match["score_b"] = score_b
            logging.info(f"Match {match_id} updated but not completed")
            return

    match["score_a"] = score_a
    match["score_b"] = score_b
    match["status"] = "Completed"

    logging.info(f"Match {match_id} score updated successfully")
    print("Cập nhật thành công.")


# ================= FUNCTION 4 =================
def generate_report():
    """Báo cáo thống kê giải đấu"""
    print("\n--- BÁO CÁO THỐNG KÊ ---")

    completed = 0

    for match in match_list:
        try:
            if match["status"] != "Completed":
                continue

            winner = determine_winner(match)

            print(
                f"{match['match_id']}: "
                f"{match['team_a']} {match['score_a']}-"
                f"{match['score_b']} {match['team_b']} | "
                f"Kết quả: {winner}"
            )

            completed += 1

        except KeyError as e:
            logging.error(f"Missing key: {e}")

    print(f"\nTổng số trận đã hoàn thành: {completed}")
    logging.info("User generated tournament report.")


# ================= MENU =================
def main():
    while True:
        print("\n===== RIKKEI ESPORTS =====")
        print("1. Hiển thị trận đấu")
        print("2. Thêm trận đấu")
        print("3. Cập nhật tỷ số")
        print("4. Báo cáo")
        print("5. Thoát")

        choice = input("Chọn (1-5): ").strip()

        if choice == "1":
            display_matches(match_list)
        elif choice == "2":
            add_match()
        elif choice == "3":
            update_score()
        elif choice == "4":
            generate_report()
        elif choice == "5":
            logging.info("System shutdown")
            print("Thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ.")
            logging.warning("Invalid menu choice selected")


if __name__ == "__main__":
    main()