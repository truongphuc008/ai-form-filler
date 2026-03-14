import json

mock_users = [
    {
        "full_name": "Duong Truong Phuc",
        "email": "phuc.uit@gmail.com",
        "phone": "0123456789",
        "university": "UIT",
        "major": "Information Technology",
        "skills": ["Python", "Git", "AI"]
    },
    {
        "full_name": "Nguyen Van Mau",
        "email": "mau.test@gmail.com",
        "phone": "0987654321",
        "university": "UIT",
        "major": "Computer Science",
        "skills": ["Java", "SQL", "Selenium"]
    }
]

with open("mock_data.json", "w", encoding="utf-8") as f:
    json.dump(mock_users, f, ensure_ascii=False, indent=4)

print("✅ Đã tạo file mock_data.json thành công!")