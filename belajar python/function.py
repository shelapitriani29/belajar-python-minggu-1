def hitung_lulus(scores):

    jumlah_lulus = 0

    for score in scores:

        if score >= 75:
            jumlah_lulus = jumlah_lulus + 1

    return jumlah_lulus

scores = [80, 65, 90, 70, 85]

hasil = hitung_lulus(scores)

print(f"Jumlah siswa lulus: {hasil}")