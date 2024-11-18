import pytest
import os

from src.file_uasge import count_lines

# 這是setup和teardown的範例

# Fixture: 用於在測試中創建和清理臨時檔案
@pytest.fixture
def setup_and_teardown():
    # Setup: 建立臨時檔案，並寫入內容
    temp_file = "temp_file.txt"
    with open(temp_file, "w") as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
        f.write("Line 3\n")
    print("🔧 已建立臨時檔案並填入測試資料")
    yield temp_file  # 傳遞臨時檔案路徑給測試函數
    # Teardown: 刪除臨時檔案
    os.remove(temp_file)
    print("🧹 已清理臨時檔案")

# 測試函數
def test_count_lines(setup_and_teardown):
    temp_file = setup_and_teardown  # 獲取臨時檔案路徑
    result = count_lines(temp_file)
    assert result == 3  # 預期結果：檔案有 3 行
