import psutil
def list_processes():
    print(f"{'Image Name':<40} {'PID':<20}")
    print("=" * 50)
    # Hàm process_iter() của psutil trả về 1 iterator chứa tất cả các đối tượng tiến trình ở đây
    # ở đây em đang yêu cầu 2 thuộc tính pid và name
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_info = proc.info
            print(f"{process_info['name']:<40} {process_info['pid']:<20}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
if __name__ == "__main__":
    list_processes()
