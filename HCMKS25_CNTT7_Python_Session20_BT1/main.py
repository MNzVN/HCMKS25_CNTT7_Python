data = [
    ("Faker", "10", "2", "8"),
    ("ShowMaker", "15", "0", "10"),
    ("Chovy", "12", "ba", "5")
]

def calculate_kda(kill : int, death : int, assist : int) -> int:
    try:
        kill = int(kill)
        death = int(death)
        assist = int(assist)
        score_kda = (kill + assist ) / death
    except (TypeError,ValueError):
        return 0.0
    except ZeroDivisionError:
            return float(kill + assist)
    else:
        return score_kda


print("--- BẢNG XẾP HẠNG KDA ---")
for item in data:
    name = item[0]
    kill = item[1]
    death = item[2]
    assist = item[3]
    score_kda = calculate_kda(kill, death, assist)
    print(f"Tuyển thủ {name} có KDA: {score_kda}")