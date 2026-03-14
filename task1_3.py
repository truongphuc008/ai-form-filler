import os
import json
import time
from dotenv import load_dotenv
from google import genai

# 1. Load API Key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or "AIzaSyBD_KvARtlMph5FnOM0kykEl_h5oNTwS5w"

# 2. Khởi tạo Client
client = genai.Client(api_key=api_key)

def convert_to_json(text_content):
    prompt = f"""
    Trích xuất JSON (full_name, email, phone, university, major, skills) từ văn bản sau.
    Chỉ trả về JSON thô, không giải thích.
    Văn bản: {text_content}
    """
    
    print("🚀 Đang gọi Gemini 2.0 Flash (models/gemini-2.0-flash)...")
    
    # Sử dụng models/gemini-2.0-flash để đúng chuẩn API mới
    response = client.models.generate_content(
        model="models/gemini-2.0-flash",
        contents=prompt
    )
    
    return response.text.replace("```json", "").replace("```", "").strip()

if __name__ == "__main__":
    if os.path.exists("extracted_text.txt"):
        with open("extracted_text.txt", "r", encoding="utf-8") as f:
            raw_text = f.read()
        
        try:
            # Nếu bị lỗi 429, đoạn code này sẽ giúp bạn biết cần đợi bao lâu
            json_data = convert_to_json(raw_text)
            parsed_json = json.loads(json_data) 
            
            with open("data.json", "w", encoding="utf-8") as f:
                json.dump(parsed_json, f, ensure_ascii=False, indent=4)
            
            print("\n--- KẾT QUẢ JSON ---")
            print(json.dumps(parsed_json, ensure_ascii=False, indent=4))
            print("\n✅ Task 1.3 với Gemini 2.0 HOÀN TẤT!")
            
        except Exception as e:
            if "429" in str(e):
                print("❌ Lỗi 429: Bạn đang gọi quá nhanh. Hãy đợi 30 giây rồi chạy lại nhé!")
            else:
                print(f"❌ Lỗi: {e}")
    else:
        print("❌ Thiếu file extracted_text.txt!")