import threading
import os
import psutil
import time

def count_words_in_files(filename):
    start_time = time.time()
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words_count = len(content.split(' '))
            print(f"So luong tu trong file '{filename}': {words_count}")
    except Exception as e:
        print(f"Error: {e}")
    end_time = time.time()
    print(f"Thoi gian thuc thi count_words_in_files: {end_time - start_time:.2f} giay")

def count_files_in_directory():
    start_time = time.time()
    try:
        files = [f for f in os.listdir('.') if os.path.isfile(f)]
        file_count = len(files)
        print(f"So file trong thu muc hien tai: {file_count}")
    except Exception as e:
        print(f"Error: {e}")
    end_time = time.time()
    print(f"Thoi gian thuc thi count_files_in_directory: {end_time - start_time:.2f} giay")

def list_processes(name):
    start_time = time.time()
    numThread = 0
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_info = proc.info
            if process_info['name'] == name:
                numThread += 1
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print(f"So luong process '{name}': {numThread}")
    end_time = time.time()
    print(f"Thoi gian thuc thi list_processes: {end_time - start_time:.2f} giay")

def main():
    thread1 = threading.Thread(target=count_words_in_files, args=("1.txt",))  
    thread2 = threading.Thread(target=count_files_in_directory)
    thread3 = threading.Thread(target=list_processes, args=("explorer.exe",))  

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    main()
