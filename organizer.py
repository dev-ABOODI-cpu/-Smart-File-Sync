import os
import shutil
import sys
import time
import requests
from colorama import Fore, Style, init
import arabic_reshaper
from bidi.algorithm import get_display

# تفعيل مكتبة الألوان
init(autoreset=True)

# ألوان متناسقة وفخمة جداً للأدوات الاحترافية
MAGENTA = Fore.LIGHTMAGENTA_EX   # بنفسجي مضيء للإطارات والزخارف
CYAN = Fore.LIGHTCYAN_EX         # سماوي للنصوص الأساسية وحقوقك
GREEN = Fore.LIGHTGREEN_EX       # أخضر مبهج للخيارات والنجاح
YELLOW = Fore.LIGHTYELLOW_EX     # أصفر للتنبيهات
RED = Fore.LIGHTRED_EX           # أحمر للخروج
GRAY = Fore.WHITE                # رمادي فاتح للمدخلات

def clear_screen():
    os.system('clear')

def fix_arabic(text):
    # دالة لإصلاح العربي فقط بدون التأثير على أكواد الألوان
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

def print_banner():
    # تصميم صندوقي رقمي فخم ومتناسق الألوان بدون تداخل
    print(f"{MAGENTA}┌──────────────────────────────────────────────────┐")
    print(f"{MAGENTA}│ {GREEN}      FILE DOWNLOADER & ORGANIZER ULTRA v3.0     {MAGENTA}│")
    print(f"{MAGENTA}├──────────────────────────────────────────────────┤")
    print(f"{MAGENTA}│ {CYAN}  » Developer : 𝐃𝐄𝐕 𝐀𝐁𝐎𝐎𝐃𝐈 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋             {MAGENTA}│")
    print(f"{MAGENTA}│ {CYAN}  » WhatsApp  : +249112727808                    {MAGENTA}│")
    print(f"{MAGENTA}│ {CYAN}  » Telegram  : @da_62                           {MAGENTA}│")
    print(f"{MAGENTA}├──────────────────────────────────────────────────┤")
    print(f"{MAGENTA}│        {GREEN}✨ {fix_arabic('مرحباً بك في غرفتك البرمجية الخاصة')} ✨     {MAGENTA}│")
    print(f"{MAGENTA}└──────────────────────────────────────────────────┘")

def download_file(url):
    file_name = url.split("/")[-1]
    if not file_name or "?" in file_name:
        file_name = f"downloaded_file_{int(time.time())}"

    print(f"\n{CYAN}[*] {fix_arabic('جاري الاتصال السريع لتحميل:')} {file_name}...")

    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))

        with open(file_name, 'wb') as file:
            if total_size == 0:
                file.write(response.content)
            else:
                downloaded = 0
                for chunk in response.iter_content(chunk_size=65536):
                    downloaded += len(chunk)
                    file.write(chunk)

                    done = int(40 * downloaded / total_size)
                    percent = int(100 * downloaded / total_size)
                    bar = '█' * done + '░' * (40 - done)

                    sys.stdout.write(f"\r{MAGENTA}[{bar}] {YELLOW}{percent}%")
                    sys.stdout.flush()

        print(f"\n\n{GREEN}[+] {fix_arabic('اكتمل تحميل الملف بنجاح!')}")

        file_extension = file_name.split(".")[-1].lower()

        if file_extension in ["jpg", "jpeg", "png", "gif", "svg", "ico"]:
            folder_name = "Images"
        elif file_extension in ["pdf", "docx", "txt", "xlsx", "rst", "pptx", "csv"]:
            folder_name = "Documents"
        elif file_extension in ["zip", "rar", "tar", "gz", "7z", "iso", "dmg"]:
            folder_name = "Compressed"
        elif file_extension in ["mp4", "mkv", "avi", "mov", "flv"]:
            folder_name = "Videos"
        elif file_extension in ["mp3", "wav", "m4a", "flac"]:
            folder_name = "Audio"
        else:
            folder_name = "Others"

        base_path = "/sdcard/Download"
        target_folder = os.path.join(base_path, folder_name)

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
            print(f"{YELLOW}[+] {fix_arabic('تم إنشاء مجلد:')} {folder_name}")

        shutil.move(file_name, os.path.join(target_folder, file_name))
        print(f"{GREEN}[+] {fix_arabic('تم النقل والمزامنة إلى:')} Download/{folder_name}")

    except Exception as e:
        print(f"\n{RED}[-] {fix_arabic('عقبة تقنية مع هذا الرابط:')} {e}")

def main_menu():
    while True:
        clear_screen()
        print_banner()

        # قوائم منظمة وجميلة ملونة بالكامل بدون تشويه الأكواد
        print(f"\n{GREEN}  [1] 📥 {fix_arabic('تحميل وتنظيم رابط واحد سريع')}")
        print(f"{CYAN}  [2] 📂 {fix_arabic('تحميل قائمة روابط دفعة واحدة من ملف')}")
        print(f"{YELLOW}  [3] 🛠 {fix_arabic('استعراض بطاقة معلومات المطور والعبقري')}")
        print(f"{RED}  [4] ❌ {fix_arabic('مغادرة الغرفة السرية وإغلاق الأداة')}\n")

        # فصل كود اللون عن النص العربي لحل مشكلة التشويه في المدخلات
        sys.stdout.write(f"{CYAN}» {fix_arabic('ادخل رقم الأمر الذكي')}: {GRAY}")
        sys.stdout.flush()
        choice = input()

        if choice == "1":
            clear_screen()
            print_banner()
            sys.stdout.write(f"\n{CYAN}» {fix_arabic('ضع رابط الملف هنا (أو اكتب 0 للعودة)')}: {GRAY}")
            sys.stdout.flush()
            url = input()
            if url == "0":
                continue
            download_file(url)
            input(f"\n{GRAY}{fix_arabic('اضغط Enter للعودة إلى لوحة التحكم الرئيسية...')}")

        elif choice == "2":
            clear_screen()
            print_banner()
            print(f"{YELLOW}[!] {fix_arabic('نصيحة: اكتب روابطك داخل ملف نصي في ترمكس أولاً.')}")
            sys.stdout.write(f"{CYAN}» {fix_arabic('أدخل اسم ملف الروابط (مثال: links.txt) أو 0 للعودة')}: {GRAY}")
            sys.stdout.flush()
            file_path = input()
            if file_path == "0":
                continue

            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    urls = [line.strip() for line in f if line.strip()]

                print(f"\n{GREEN}[+] {fix_arabic('تم العثور على')} {len(urls)} {fix_arabic('روابط. بدء العمل...')}")
                for index, url in enumerate(urls, 1):
                    print(f"\n{MAGENTA}════════════════ [{index}/{len(urls)}] ════════════════")
                    download_file(url)
                print(f"\n{GREEN}[+++] {fix_arabic('تم الانتهاء من تحميل وتنسيق القائمة بالكامل!')}")
            else:
                print(f"{RED}[-] {fix_arabic('الملف غير موجود! تأكد من الاسم.')}")
            input(f"\n{GRAY}{fix_arabic('اضغط Enter للعودة إلى لوحة التحكم الرئيسية...')}")

        elif choice == "3":
            clear_screen()
            print_banner()
            print(f"\n{CYAN}✦ {fix_arabic('الشغف، الإبداع، وهندسة الأكواد تجتمع هنا.')}")
            print(f"{CYAN}✦ {fix_arabic('تم تطوير وصقل هذه الأداة بكامل تفاصيلها الاحترافية')}")
            print(f"  {fix_arabic('بواسطة المطور القدير والمهتم بالأمن السيبراني:')} {YELLOW}DEV ABOODI")
            print(f"{CYAN}✦ {fix_arabic('خطوة واحدة اليوم في البرمجة، هي قفزة غداً في حماية العالم الرقمي.')}")
            input(f"\n{GRAY}{fix_arabic('اضغط Enter للعودة (Back)...')}")

        elif choice == "4":
            clear_screen()
            print_banner()
            print(f"\n{GREEN}{fix_arabic('يسعدني دائماً رفقاك في رحلة التطوير يا عبودي. طاب يومك! 🍫✨')}")
            time.sleep(2)
            clear_screen()
            sys.exit()

        else:
            print(f"{RED}[!] {fix_arabic('اختيار غير صحيح، يرجى إدخال رقم صحيح.')}")
            time.sleep(1.5)

if __name__ == "__main__":
    main_menu()
