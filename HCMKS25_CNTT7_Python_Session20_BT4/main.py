import logging
roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active"
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active"
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched"
    }
]


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] - [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='roster_app.log',
    filemode='w'
)


def is_duplicate_player_id(player_id):
    for player in roster:
        if player["player_id"] == player_id:
            return True
    return False


def find_player_by_id(roster_list, player_id):
    for player in roster_list:
        if player["player_id"] == player_id:
            return player
    return None


def calculate_actual_pay(player_dict):
    if player_dict["status"] == "Active":
        return player_dict["salary"]
    return player_dict["salary"] * 0.5


def display_roster(roster_list):
    if len(roster_list) == 0:
        print("Đội hình hiện đang trống.")
        return

    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")
    print(
        f"{'ID':<8}| {'Tên tuyển thủ':<22}| "
        f"{'Vị trí':<15}| {'Lương':<12}| Trạng thái"
    )
    print("-" * 80)

    try:
        for player in roster_list:

            status = player.get("status", "Unknown")

            player_name = player["name"]

            if status == "Benched":
                player_name += " [DỰ BỊ]"

            print(
                f"{player['player_id']:<8}| "
                f"{player_name:<22}| "
                f"{player['role']:<15}| "
                f"{player['salary']:<12,.1f}| "
                f"{status}"
            )

        logging.info(
            "Coach viewed the team roster."
        )

    except KeyError as e:
        print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
        logging.error(
            f"Missing key while displaying roster: {e}"
        )


def sign_player(roster_list):

    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    if is_duplicate_player_id(player_id):
        print(
            f"Lỗi: Mã tuyển thủ {player_id} đã tồn tại."
        )

        logging.warning(
            f"Failed to sign player - Duplicate player ID {player_id}"
        )
        return

    player_name = input(
        "Nhập tên tuyển thủ: "
    ).strip().title()

    role = input(
        "Nhập vị trí thi đấu: "
    ).strip().title()

    while True:

        try:
            salary = float(
                input("Nhập mức lương hàng tháng: ")
            )

            if salary <= 0:
                print(
                    "Lương phải là số dương. Vui lòng nhập lại."
                )
                continue

            break

        except ValueError:
            print(
                "Lương phải là số. Vui lòng nhập lại."
            )

            logging.warning(
                "Failed to sign player - Invalid salary input"
            )

    new_player = {
        "player_id": player_id,
        "name": player_name,
        "role": role,
        "salary": salary,
        "status": "Active"
    }

    roster_list.append(new_player)

    print(
        f"\nThành công: Đã chiêu mộ tuyển thủ {player_name}."
    )

    logging.info(
        f"Signed new player {player_name} with salary {salary}"
    )


def update_player_status(roster_list):

    print(
        "\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI THI ĐẤU ---"
    )

    player_id = input(
        "Nhập mã tuyển thủ cần cập nhật: "
    ).strip().upper()

    player = find_player_by_id(
        roster_list,
        player_id
    )

    if player is None:

        print(
            f"Không tìm thấy tuyển thủ mang mã {player_id}."
        )

        logging.warning(
            f"Failed to update player - Player ID {player_id} not found"
        )

        return

    print(f"\nTuyển thủ: {player['name']}")
    print(f"Vị trí: {player['role']}")
    print(f"Lương hiện tại: {player['salary']}")
    print(f"Trạng thái hiện tại: {player['status']}")

    print("""
Bạn muốn cập nhật:
1. Cập nhật lương
2. Cập nhật trạng thái thi đấu
""")

    update_choice = input(
        "Chọn chức năng cập nhật (1-2): "
    )

    if update_choice == "1":

        old_salary = player["salary"]

        while True:

            try:

                new_salary = float(
                    input("Nhập mức lương mới: ")
                )

                if new_salary <= 0:
                    print(
                        "Lương phải là số dương. Vui lòng nhập lại."
                    )
                    continue

                player["salary"] = new_salary

                print(
                    f"Thành công: Đã cập nhật lương cho tuyển thủ {player_id}."
                )

                logging.info(
                    f"Updated player {player_id} salary from {old_salary} to {new_salary}"
                )

                break

            except ValueError:
                print(
                    "Lương phải là số. Vui lòng nhập lại."
                )

    elif update_choice == "2":

        print("""
Chọn trạng thái mới:
1. Active
2. Benched
""")

        status_choice = input(
            "Nhập lựa chọn trạng thái (1-2): "
        )

        if status_choice == "1":
            player["status"] = "Active"

        elif status_choice == "2":
            player["status"] = "Benched"

        else:
            print("Lựa chọn không hợp lệ.")
            return

        print(
            f"Thành công: Đã cập nhật trạng thái cho tuyển thủ {player_id}."
        )

        logging.info(
            f"Updated player {player_id} status to {player['status']}"
        )


def generate_payroll_report(roster_list):

    print(
        "\n--- BÁO CÁO QUỸ LƯƠNG HÀNG THÁNG ---"
    )

    if len(roster_list) == 0:
        print(
            "Đội hình hiện đang trống. Tổng quỹ lương: 0.0"
        )
        return

    total_payroll = 0.0

    print(
        f"{'ID':<8}| {'Tên tuyển thủ':<15}| "
        f"{'Trạng thái':<11}| {'Lương gốc':<12}| "
        f"Lương thực nhận"
    )

    print("-" * 80)

    try:

        for player in roster_list:

            actual_pay = calculate_actual_pay(player)

            print(
                f"{player['player_id']:<8}| "
                f"{player['name']:<15}| "
                f"{player['status']:<11}| "
                f"{player['salary']:<12,.1f}| "
                f"{actual_pay:,.1f}"
            )

            total_payroll += actual_pay

        print("-" * 80)

        print(
            f"Tổng quỹ lương hàng tháng: {total_payroll:,.1f}"
        )

        logging.info(
            f"Generated monthly payroll report. Total: {total_payroll}"
        )

    except KeyError as e:

        print(
            "Lỗi: Một tuyển thủ đang bị thiếu dữ liệu."
        )

        print("-" * 80)

        print(
            "Tổng quỹ lương hàng tháng: 0.0"
        )

        logging.error(
            f"Missing key while generating payroll report: {e}"
        )


while True:

    menu_title = (
        "HỆ THỐNG QUẢN LÝ ĐỘI HÌNH RIKKEI ESPORTS"
    )

    user_choice = input(
        f"""
===== {menu_title} =====
1. Xem đội hình thi đấu hiện tại
2. Chiêu mộ tuyển thủ mới
3. Cập nhật lương & Trạng thái thi đấu
4. Báo cáo quỹ lương hàng tháng
5. Thoát hệ thống
==================================================
Chọn chức năng (1-5): """
    )

    match user_choice:

        case "1":
            display_roster(roster)

        case "2":
            sign_player(roster)

        case "3":
            update_player_status(roster)

        case "4":
            generate_payroll_report(roster)

        case "5":
            print("Đã thoát hệ thống.")

            logging.info(
                "Roster management system closed."
            )

            break

        case _:
            print(
                "Lựa chọn không hợp lệ. Vui lòng chọn từ 1-5."
            )
