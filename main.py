from quanlisv import Sms
from students import Student



def main():
    lb = Sms()

    while True:
        print("\n===== MENU =====")
        print("1. Them sinh vien")
        print("2. Xem tat ca sinh vien")
        print("3. Tim kiem thong tin sinh vien")
        print("4. Cap nhat thong tin sinh vien")
        print("5. Xoa thong tin sinh vien")
        print("6. Thoat!")
        choice = input("Chọn: ")

        if choice == "1":
            # Nhập thông tin sinh vien
            title = input("Nhap ten sinh vien: ")
            age = input("Nhap tuoi sinh vien: ")
            id = input("Nhap cccd: ")


        elif choice == "2":

        elif choice == "3":
            
        elif choice == "4":

        elif choice == "4":
            print("Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ.")
