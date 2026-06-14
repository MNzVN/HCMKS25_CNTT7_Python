
import logging

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

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='tournament_app.log',
    filemode='w'
)


def is_duplicate_match_id(match_id):
    for match in match_list:
        if match["match_id"] == match_id:
            return True
    return False


def display_matches(matches):
    if len(matches) == 0:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")
    print(f"{'Mã trận':<10}| {'Đội A':<15}| {'Đội B':<15}| {'Tỷ số':<8}| Trạng thái")
    print("-" * 70)

    for match in matches:
        score = f"{match['score_a']}-{match['score_b']}"
        print(
            f"{match['match_id']:<10}| "
            f"{match['team_a']:<15}| "
            f"{match['team_b']:<15}| "
            f"{score:<8}| "
            f"{match['status']}"
        )

    logging.info("User viewed the match list.")


def add_match(matches):
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")

    match_id = input("Nhập mã trận đấu: ").strip().upper()

    if match_id == "":
        print("Mã trận đấu không được để trống.")
        logging.warning(
            "User tried to add a match with empty match ID."
        )
        return

    if is_duplicate_match_id(match_id):
        print(f"Lỗi: Mã trận đấu {match_id} đã tồn tại.")
        logging.warning(
            f"Match ID {match_id} already exists."
        )
        return

    team_a = input("Nhập tên Đội A: ").strip()

    if team_a == "":
        print("Tên đội không được để trống.")
        logging.warning(
            "User tried to add a match with empty team name."
        )
        return

    team_b = input("Nhập tên Đội B: ").strip()

    if team_b == "":
        print("Tên đội không được để trống.")
        logging.warning(
            "User tried to add a match with empty team name."
        )
        return

    new_match = {
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }

    matches.append(new_match)

    print(f"\nThành công: Đã thêm trận đấu {match_id}.")
    logging.info(
        f"Match {match_id} added successfully"
    )


def input_score(team_name):
    while True:
        try:
            score = int(input(f"Nhập điểm {team_name}: "))

            if score < 0:
                print("Điểm số phải lớn hơn hoặc bằng 0.")
                logging.error(
                    f"Negative score input detected: {score}"
                )
                continue

            return score

        except ValueError as e:
            print("Điểm số phải là số nguyên. Vui lòng nhập lại.")
            logging.error(
                f"Invalid score input. Error: {e}"
            )


def update_score(matches):
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")

    match_id = input(
        "Nhập mã trận đấu cần cập nhật: "
    ).strip().upper()

    for match in matches:

        if match["match_id"] == match_id:

            print(
                f"\nTrận đấu: "
                f"{match['team_a']} vs {match['team_b']} "
                f"({match['status']})"
            )

            score_a = input_score("Đội A")
            score_b = input_score("Đội B")

            match["score_a"] = score_a
            match["score_b"] = score_b

            if score_a == 0 and score_b == 0:

                confirm = input(
                    "Tỷ số đang là 0-0. Trọng tài có xác nhận trận đã hoàn thành không? (y/n): "
                ).strip().lower()

                if confirm == "y":
                    match["status"] = "Completed"
                else:
                    match["status"] = "Pending"

            else:
                match["status"] = "Completed"

            print(
                f"\nThành công: Đã cập nhật tỷ số trận đấu {match_id}."
            )

            logging.info(
                f"Match {match_id} score updated successfully"
            )

            return

    print(f"Không tìm thấy trận đấu mang mã {match_id}.")
    logging.warning(
        f"User tried to update non-existing match {match_id}"
    )


def determine_winner(match):

    if match["status"] == "Pending":
        return "Not Started"

    if match["score_a"] > match["score_b"]:
        return match["team_a"]

    if match["score_b"] > match["score_a"]:
        return match["team_b"]

    return "Draw"


def generate_report(matches):
    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")

    completed_count = 0

    for match in matches:

        if match["status"] == "Completed":

            winner = determine_winner(match)

            print(
                f"{match['match_id']}: "
                f"{match['team_a']} "
                f"{match['score_a']}-{match['score_b']} "
                f"{match['team_b']} | "
                f"Kết quả: {winner}"
            )

            completed_count += 1

    if completed_count == 0:
        print("Chưa có trận đấu nào hoàn thành.")

    print(f"\nTổng số trận đã hoàn thành: {completed_count}")

    logging.info(
        "User generated tournament report."
    )


while True:

    menu_title = "HỆ THỐNG QUẢN LÝ GIẢI ĐẤU RIKKEI ESPORTS"

    user_choice = input(
        f"""
===== {menu_title} =====
1. Hiển thị lịch thi đấu & Kết quả
2. Thêm trận đấu mới
3. Cập nhật tỷ số trận đấu
4. Báo cáo thống kê
5. Thoát chương trình
==================================================
Chọn chức năng (1-5): """
    )

    match user_choice:

        case "1":
            display_matches(match_list)

        case "2":
            add_match(match_list)

        case "3":
            update_score(match_list)

        case "4":
            generate_report(match_list)

        case "5":
            print("Đóng chương trình...")
            logging.info(
                "Tournament management system closed."
            )
            break

        case _:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1-5.")
