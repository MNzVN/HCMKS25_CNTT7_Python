# Dữ liệu API
player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


# Hàm tính thưởng
def calculate_bonus(matches, mmr):
    return (matches * 10) + (mmr * 0.5)


# Hàm xử lý chính
def process(player_records):
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    for record in player_records:
        try:
            print("Đang xử lý:", record)

            player_name = record[0]
            matches_played = record[1]
            mmr = record[2]

            matches_played = int(matches_played)
            mmr = int(mmr)

            bonus_rp = calculate_bonus(matches_played, mmr)

            print(f"{player_name}: nhận được {bonus_rp} RP")

        except IndexError:
            print(f"{record[0] if len(record) > 0 else 'Unknown'}: Lỗi - Hồ sơ bị thiếu thông tin!")

        except ValueError:
            print(f"{record[0]}: Lỗi - Dữ liệu MMR không hợp lệ!")

        continue


# Chạy chương trình
process(player_records)