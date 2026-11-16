import datetime

def main():
    current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print("Xin chào! Môi trường của tôi đã sẵn sàng cho khóa học AI Agent 101!")
    print(f"Thời gian hiện tại: {current_time}")

if __name__ == "__main__":
    main()
