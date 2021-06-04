import os.path


def show_menu():
    result = 1
    try:
        result = int(input("1. 학생목록, 2. 학생 추가, 3. 학생 수정, 4. 학생 삭제, 5. 종료 [1-5]번호를 입력하세요."))
    except ValueError as e:
        print("숫자 [1-5]값만 가능")
    finally:
        return result


def std_list_read_file():
    if os.path.isfile(file_name):
        with open("student_list.txt", "r", encoding="utf-8") as student_list:
            for std in student_list:
                std = std.strip().split(", ")
                std_list.append(std)


def std_list_write_file():
    with open("student_list.txt", "w", encoding="utf-8") as f:
        for std in std_list:
            format_str = "{}, {}, {}, {}, {}\n".format(std[0], std[1], std[2], std[3], std[4])
            f.write(format_str)


def show_std_list():
    print("{:3} {:4} {:3} {:3} {:3} {:4} {:>4}".format('번호', '성명', '국어', '영어', '수학', '총점', '평균'))
    for std in std_list:
        total = int(std[2]) + int(std[3]) + int(std[4])
        avg = total / 3
        std_info = "{:3d} {:4} {:3d} {:3d} {:3d} {:4d} {:7.2f}".format(int(std[0]), std[1], int(std[2]), int(std[3]), int(std[4]), total, avg)
        print(std_info)


def add_std_info():
    std = get_std_info("성명 국어 영어 수학을 입력하세요.")
    idx = len(std_list)
    std.insert(0, str(idx+1))
    std_list.append(std)


def get_std_info(msg):
    result = input(msg)
    std_info = result.split()
    return std_info


def update_std_info():
    show_std_list()
    num = input("수정할 학생번호를 입력하세요. >> ")
    std_info = input("수정할 국어 영어 수학을 입력하세요. >> ")
    for std in std_list:
        if std[0] == num:
            std[2], std[3], std[4] = std_info.split()[0], std_info.split()[1], std_info.split()[2]


def delete_std_info():
    show_std_list()
    num = input("삭제할 학생번호를 입력하세요.")
    for std in std_list:
        if std[0] == num:
            std_list.remove(std)


if __name__ == "__main__":
    std_list = []
    file_name = "student_list.txt"

    std_list_read_file()
    while True:
        res = show_menu()
        if res == 1:
            show_std_list()
        elif res == 2:
            add_std_info()
        elif res == 3:
            update_std_info()
        elif res == 4:
            print("학생 삭제")
            delete_std_info()
        else:
            std_list_write_file()
            break
    print("프로그램 종료")

