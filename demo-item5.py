# Khai báo tài khoản đúng
username_correct = "admin"
password_correct = "admin@2025"

# Kiểm tra điều kiện
def check_inf(username_input, password_input):
    if username_input == "" or password_input == "":
        print("Không được để trống username hoặc password.")
    elif username_input != username_correct and password_input != password_correct:
        print("Sai cả username và password.")
    elif username_input != username_correct:
        print("Sai username.")
    elif password_input != password_correct:
        print("Sai password.")
    else:
        print("Đăng nhập thành công!")

# Nhập thông tin từ người dùng
username_input = input("Nhập username: ")
password_input = input("Nhập password: ")

check_inf(username_input, password_input)
