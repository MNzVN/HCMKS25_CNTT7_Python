# Dữ liệu
player_stats_list = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]

# Hàm tính KDA (modular)
def calculate_kda(kills, deaths, assists):
    return (kills + assists) / deaths


# Hàm xử lý chính
def process_kda(player_stats_list):
    print("--- BẢNG XẾP HẠNG KDA ---")

    for player_data in player_stats_list:
        player_name = player_data[0]
        kills = player_data[1]
        deaths = player_data[2]
        assists = player_data[3]

        try:
            kills = int(kills)
            deaths = int(deaths)
            assists = int(assists)

            kda = calculate_kda(kills, deaths, assists)

            print(f"{player_name}: KDA = {kda}")

        except ZeroDivisionError:
            print(f"{player_name}: KDA Hoàn hảo (Perfect Game)!")

        except ValueError:
            print(f"{player_name}: Lỗi dữ liệu không hợp lệ!")

        continue


# Chạy chương trình
process_kda(player_stats_list)