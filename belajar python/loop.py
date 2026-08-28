scores = [80, 65, 90, 70, 85]

for index, score in enumerate(scores, start=1):

    if score >= 75:
        print(f"{index}. {score} → Lulus")

    else:
        print(f"{index}. {score} → Tidak Lulus")