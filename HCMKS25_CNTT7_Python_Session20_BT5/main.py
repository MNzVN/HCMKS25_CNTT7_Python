import logging
players = [
    {
        "player_id": "T101",
        "player_name": "Faker",
        "market_value": 5000,
        "fan_tokens": 1500,
        "match_points": 0,
        "form_multiplier": 1.0
    },
    {
        "player_id": "GEN01",
        "player_name": "Chovy",
        "market_value": 4800,
        "fan_tokens": 800,
        "match_points": 500,
        "form_multiplier": 1.2
    },
    {
        "player_id": "DRX01",
        "player_name": "Deft",
        "market_value": 3000,
        "fan_tokens": 0,
        "match_points": 0,
        "form_multiplier": 0.8
    }
]


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="fantasy_league.log",
    filemode="w"
)


def find_player_by_id(player_id):
    for player in players:
        if player["player_id"] == player_id:
            return player
    return None


def display_market(player_list):

    if len(player_list) == 0:
        print("Sàn giao dịch hiện chưa có tuyển thủ nào.")
        return

    print("\n--- SÀN GIAO DỊCH TUYỂN THỦ ---")
    print(
        f"{'ID':<10}| {'Tên tuyển thủ':<15}| "
        f"{'Giá trị thị trường':<18}| {'Fan Token':<10}| "
        f"{'Điểm trận':<10}| {'Hệ số':<8}| Trạng thái đầu tư"
    )
    print("-" * 120)

    for player in player_list:

        fan_tokens = player.get("fan_tokens", 0)

        if fan_tokens == 0:
            investment_status = "Chưa có người đầu tư"
        elif fan_tokens <= 1000:
            investment_status = "Đang thu hút"
        else:
            investment_status = "Tuyển thủ Hot"

        print(
            f"{player.get('player_id', 'Unknown'):<10}| "
            f"{player.get('player_name', 'Unknown'):<15}| "
            f"{player.get('market_value', 0):<18}| "
            f"{fan_tokens:<10}| "
            f"{player.get('match_points', 0):<10}| "
            f"{player.get('form_multiplier', 1.0):<8}| "
            f"{investment_status}"
        )

    logging.info("User viewed the player market.")


def invest_tokens(player_list):

    print("\n--- ĐẦU TƯ FAN TOKEN ---")

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    player = find_player_by_id(player_id)

    if player is None:
        print("Không tìm thấy tuyển thủ!")

        logging.warning(
            f"Invest failed - Player {player_id} not found"
        )
        return

    while True:

        try:

            token_amount = int(
                input("Nhập số token muốn đầu tư: ")
            )

            if token_amount <= 0:
                print(
                    "Số token phải là số nguyên dương. Vui lòng nhập lại."
                )
                continue

            player["fan_tokens"] += token_amount

            print(
                f"\nThành công: Đã đầu tư {token_amount} token vào tuyển thủ {player_id}."
            )

            print(
                f"Số Fan Token hiện tại của {player['player_name']}: "
                f"{player['fan_tokens']:,}"
            )

            logging.info(
                f"Invested {token_amount} tokens into {player_id}"
            )

            break

        except ValueError:

            print(
                "Số token phải là số nguyên dương. Vui lòng nhập lại."
            )

            logging.warning(
                "Invalid token input while investing"
            )


def withdraw_tokens(player_list):

    print("\n--- RÚT VỐN FAN TOKEN ---")

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    player = find_player_by_id(player_id)

    if player is None:
        print("Không tìm thấy tuyển thủ!")
        return

    while True:

        try:

            withdraw_amount = int(
                input("Nhập số token muốn rút: ")
            )

            if withdraw_amount <= 0:
                print(
                    "Số token phải là số nguyên dương."
                )
                continue

            if withdraw_amount > player["fan_tokens"]:

                print(
                    "Không thể rút. Số token muốn rút vượt quá số Fan Token hiện có."
                )

                print(
                    f"Fan Token hiện có của {player['player_name']}: "
                    f"{player['fan_tokens']:,}"
                )

                logging.warning(
                    "Withdraw failed - Amount exceeds current fan tokens"
                )

                return

            fee = withdraw_amount * 0.1
            actual_received = withdraw_amount - fee

            player["fan_tokens"] -= withdraw_amount

            print(
                f"\nThành công: Đã rút {withdraw_amount} token khỏi tuyển thủ {player_id}."
            )

            print(
                f"Phí giao dịch 10%: {fee} token"
            )

            print(
                f"Số token thực nhận về ví: {actual_received} token"
            )

            print(
                f"Fan Token còn lại của {player['player_name']}: "
                f"{player['fan_tokens']:,}"
            )

            logging.info(
                f"Withdrawn {withdraw_amount} tokens from {player_id}. Actual received: {actual_received}"
            )

            break

        except ValueError:
            print(
                "Số token phải là số nguyên dương."
            )


def update_form(player_list):

    print("\n--- CẬP NHẬT HỆ SỐ PHONG ĐỘ ---")

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    player = find_player_by_id(player_id)

    if player is None:
        print("Không tìm thấy tuyển thủ!")
        return

    while True:

        try:

            new_multiplier = float(
                input(
                    "Nhập hệ số phong độ mới (0.5 - 2.5): "
                )
            )

            if not 0.5 <= new_multiplier <= 2.5:
                print(
                    "Hệ số phong độ chỉ được nằm trong khoảng 0.5 đến 2.5."
                )
                continue

            player["form_multiplier"] = new_multiplier

            print(
                f"\nThành công: Đã cập nhật hệ số phong độ cho {player['player_name']}."
            )

            print(
                f"Hệ số mới: x{new_multiplier}"
            )

            logging.info(
                f"Updated form multiplier for {player_id} to {new_multiplier}"
            )

            break

        except ValueError:

            print(
                "Hệ số phong độ phải là số thực. Vui lòng nhập lại."
            )


def calculate_match_points(player_list):

    print("\n--- CHẤM ĐIỂM SAU TRẬN ĐẤU ---")

    player_id = input(
        "Nhập mã tuyển thủ: "
    ).strip().upper()

    player = find_player_by_id(player_id)

    if player is None:
        print("Không tìm thấy tuyển thủ!")
        return

    while True:

        try:

            base_points = float(
                input(
                    "Nhập điểm gốc của trận đấu: "
                )
            )

            if base_points < 0:
                print(
                    "Điểm không được âm."
                )
                continue

            actual_points = (
                base_points *
                player["form_multiplier"]
            )

            player["match_points"] += actual_points

            print(
                f"\n>> Tuyển thủ {player['player_name']} nhận được "
                f"{actual_points} điểm "
                f"(Hệ số x{player['form_multiplier']})."
            )

            print(
                f"Tổng điểm: {player['match_points']}"
            )

            logging.info(
                f"Added {actual_points} match points to {player_id}"
            )

            break

        except ValueError:

            print(
                "Điểm phải là số."
            )


while True:

    menu_title = (
        "HỆ THỐNG RIKKEI ESPORTS FANTASY"
    )

    user_choice = input(
        f"""
===== {menu_title} =====
1. Xem Sàn Giao Dịch Tuyển Thủ
2. Đầu tư Fan Token
3. Rút vốn (Hoàn trả Token)
4. Biến động phong độ (Cập nhật hệ số)
5. Chấm điểm sau trận đấu
6. Thoát hệ thống
==================================================
Chọn chức năng (1-6): """
    )

    match user_choice:

        case "1":
            display_market(players)

        case "2":
            invest_tokens(players)

        case "3":
            withdraw_tokens(players)

        case "4":
            update_form(players)

        case "5":
            calculate_match_points(players)

        case "6":

            print(
                "Đóng hệ thống Rikkei Esports Fantasy."
            )

            logging.info(
                "Fantasy League system closed."
            )

            break

        case _:

            print(
                "Lựa chọn không hợp lệ. Vui lòng chọn từ 1-6."
            )

            logging.warning(
                "Invalid menu choice."
            )