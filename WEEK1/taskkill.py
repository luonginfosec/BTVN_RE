import psutil
import ctypes
import sys
def taskkill_by_pid(pid):
    PROCESS_TERMINATE = 1 # Quyền truy cập cần thiết để có thể kết thúc được tiến trình
    handle = ctypes.windll.kernel32.OpenProcess(PROCESS_TERMINATE, False, pid)
    # Sử dụng ctypes để gọi hàm OpenProcess từ kernel32 của Win , tiến hành mở chương trình
    # đã cho với quyền có thể kết thúc được tiến trình , tham số thứ 2 là False tức là không kế thừa
    # đến các chương trình con
    if handle:
        # nếu mở thành công ta tiến hành truyền handle và exit code để đóng tiến trình
        success = ctypes.windll.kernel32.TerminateProcess(handle, -1)
        # giải phóng tài nguyên
        ctypes.windll.kernel32.CloseHandle(handle)
        if success:
            print(f"Success")
        else:
            print(f"Error")
    else:
        print(f"Error")
def taskkill_by_name(name):
    found = False
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == name:
            found = True
            taskkill_by_pid(proc.info['pid'])
    if not found:
        print(f"No process found with name '{name}'")
def main():
    if len(sys.argv) != 3:
        print("Usage: python taskkill.py <method> <value>")
        return
    method = sys.argv[1]
    value = sys.argv[2]
    
    if method == "name":
        taskkill_by_name(value)
    elif method == "pid":
        try:
            pid = int(value)
            taskkill_by_pid(pid)
        except ValueError:
            print("Error")
    else:
        print("Invalid method. Use 'name' or 'pid'.")
if __name__ == "__main__":
    main()
