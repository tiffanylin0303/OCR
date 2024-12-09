import torch
print(torch.cuda.is_available())  # True 表示 GPU 可用
print(torch.cuda.get_device_name(1))  # 獲取第一張 GPU 的名稱
print(torch.cuda.device_count())  # 返回 GPU 數量


from PIL import Image
import pytesseract

img1 = Image.open('image-ocr-english.jpg')
text = pytesseract.image_to_string(img1, lang='eng') #English detection
print(text)

img2 = Image.open('image-ocr.jpg')
text1 = pytesseract.image_to_string(img2, lang='chi_tra') # English and Chinese detection
print(text1)