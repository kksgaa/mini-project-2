from prettytable import PrettyTable

user = {
    "admin": {"password": "admin", "role": "admin"},
    "buyer": {"password": "buyer", "role": "pembeli"}
}

def tampilkan_kostum(k):
    table = PrettyTable()
    table.field_names = ["NO", "Nama Kostum", "Harga Sewa"]
    table.title = "Daftar Kostum"
    for kostum in k:
        table.add_row([kostum["no"], kostum["nama"], kostum["harga"]])
    print(table)

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in user and user[username]["password"] == password:
        print(f"Login berhasil, selamat datang {username}")
        return user[username]["role"]
    else:
        print("Username atau password salah")
        return None

def admin_menu(k):
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Tambah Kostum")
        print("2. Lihat Kostum")
        print("3. Update Kostum")
        print("4. Hapus Kostum")
        print("5. Logout")

        pilihan = input("Pilih menu nomor: ")

        if pilihan == "1":
            tambah_kostum(k)
        elif pilihan == "2":
            tampilkan_kostum(k)
        elif pilihan == "3":
            update_kostum(k)
        elif pilihan == "4":
            hapus_kostum(k)
        elif pilihan == "5":
            print("anda telah logout")
            break
        else:
            print("Tidak ada pilihan dengan angka tersebut")

def pembeli_menu(k):
    while True:
        print("\n=== MENU PEMBELI ===")
        print("1. sewa kostum")
        print("2. Logout")

        pilihan = input("Pilih menu nomor: ")

        if pilihan == "1":
            sewa_kostum(k)
        elif pilihan == "2":
            print("anda telah logout")
            break
        else:
            print("Tidak ada pilihan dengan angka tersebut")

def tambah_kostum(k):
    nama = input("Masukkan nama kostum: ")
    harga = int(input("Masukkan harga sewa: "))

    no_baru = len(k) + 1
    k.append({"no": no_baru, "nama": nama, "harga": harga})
    print("Kostum berhasil ditambahkan")

def update_kostum(k):
    tampilkan_kostum(k)
    no_kostum = int(input("Masukkan NO kostum yang ingin diupdate: "))
    for kostum in k:
        if kostum["no"] == no_kostum:
            kostum["nama"] = input(f"Masukkan nama baru untuk {kostum["nama"]}: ")
            kostum["harga"] = int(input(f"Masukkan harga baru untuk {kostum["nama"]}: "))
            print("Kostum berhasil diupdate")
            return
    print("Kostum tidak ditemukan")

def hapus_kostum(k):
    tampilkan_kostum(k)
    no_kostum = int(input("Masukkan NO kostum yang ingin dihapus: "))
    for kostum in k:
        if kostum["no"] == no_kostum:
            k.remove(kostum)
            print("Kostum berhasil dihapus")
            return
    print("Kostum tidak ditemukan")

def sewa_kostum(k):
    tampilkan_kostum(k)
    no_kostum = int(input("Masukkan NO kostum yang ingin disewa: "))
    for kostum in k:
        print(f"Anda berhasil menyewa {kostum["nama"]} ")
        return
    print("Kostum tidak ditemukan!")

def main():
    print("Selamat datang di Rental Kostum Cosplay!")

    role = None
    while role is None:
        role = login()

    if role == "admin":
        admin_menu(kostum_list)
    elif role == "pembeli":
        pembeli_menu(kostum_list)

kostum_list = []
if __name__ == "__main__":
    main()