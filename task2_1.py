from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# 1. Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 2. Mở một trang web thử nghiệm (ví dụ Google Form hoặc trang bất kỳ)
driver.get("https://www.google.com")

print("✅ Đã mở trình duyệt thành công!")
time.sleep(5) # Đợi 5 giây để bạn quan sát

# 3. Đóng trình duyệt
driver.quit()