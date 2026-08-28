hobbies = ["reading", "swimming", "coding"]

search = input("Masukkan hobi yang ingin dicari: ").lower()

if search in hobbies:
    print("Hobi ditemukan!")
else:
    print("Hobi tidak ditemukan.")