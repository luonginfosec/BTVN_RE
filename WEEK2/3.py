from pathlib import Path

def list_files_in_directory(directory):
    try:
        path = Path(directory)
        for item in path.iterdir():
            if item.is_file():
                print(f"File: {item.name}")
            elif item.is_dir():
                print(f"Directory: {item.name}")
    except Exception as e:
        print(f"Error: {e}")

directory_path = input("Nhập vào đường dẫn thư mục bạn muốn liệt kê: ")
list_files_in_directory(directory_path)
