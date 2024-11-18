# file_usage.py

def count_lines(file_path):
    """計算檔案中的行數"""
    with open(file_path, "r") as file:
        return len(file.readlines())