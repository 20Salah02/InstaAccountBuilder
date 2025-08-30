import requests
import json
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import random

# إنشاء مجلد لحفظ الصور
if not os.path.exists('profile_images'):
    os.makedirs('profile_images')

# تهيئة Faker لإنشاء بيانات وهمية
fake = Faker()

# قائمة البروكسي التي قمت بتوفيرها
proxies = [
    'http://07emg3isi9eofe4-session-0ts3b5yhsj-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-n8hg99qldc-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-s2x68ruwf7-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-b84clhy7z2-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-bekcey52cx-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-xb7n8fnrzx-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-3wcfq647ym-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-oiacfslsjx-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-lb0s1db246-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-ae7xh1zaug-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-38deffc3qu-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-r6y7h7568o-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-4rq1cfad0h-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-gv7rpylfkg-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-lq22843ily-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-svetpbj9jd-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-vxe5gfkdul-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-exvg7psysq-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-it0mvdcz2l-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-khqm1iyzcg-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-9q193e94hn-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-j68jv7ln6s-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-ioevu2efcy-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-aepm0b12s4-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-1t9p6zi8gl-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-p093z45mjb-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-z4jup46jf8-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-awu4ukkqd8-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-y7p8uq31ox-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-ynrh1qqp8e-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-3gfdz3161m-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-tinww2riy8-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-j2fta1lj2n-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-w6mt843xk0-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-tg98uf2zpc-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-eualal6zm1-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-u051quj1yr-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-jzdrvw2sqs-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-9tgig60xra-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-llt3rfumgd-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-d1o0clju6n-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-hkplls51uc-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-s2e31kdyt2-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-uzaw6oznlk-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-j62e69p778-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-yjlqqaxu13-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-f92jrqwbo7-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-s8rohv1fkq-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-5ogcivqww1-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
    'http://07emg3isi9eofe4-session-2vb17fexj8-lifetime-10:3kvh4atxod343d6@rp.scrapegw.com:6060',
]

# دالة لإنشاء بريد إلكتروني مؤقت من temp-mail.org
def get_temp_email():
    response = requests.get('https://api.internal.temp-mail.io/api/v3/email/new')
    if response.status_code == 200:
        return response.json()['email']
    return None

# دالة لتنزيل صورة ملف شخصي من thispersondoesnotexist.com
def download_profile_image(index, gender=None):
    if gender in ['male', 'female']:
        url = 'https://thispersondoesnotexist.com/image'
        response = requests.get(url)
        if response.status_code == 200:
            image_path = f'profile_images/profile_{index}.jpg'
            with open(image_path, 'wb') as file:
                file.write(response.content)
            return image_path
    else:
        # تنزيل صور الحيوانات أو الطبيعة من مصدر آخر
        animal_url = 'https://source.unsplash.com/1600x900/?nature,animal'
        response = requests.get(animal_url)
        if response.status_code == 200:
            image_path = f'profile_images/profile_{index}.jpg'
            with open(image_path, 'wb') as file:
                file.write(response.content)
            return image_path
    return None

# دالة لإنشاء أسماء مستخدمين تبدو مثل أسماء مستخدمي إنستغرام
def generate_instagram_username(gender=None):
    if gender == 'male':
        return fake.user_name() + str(random.randint(0, 999))
    elif gender == 'female':
        return fake.user_name() + str(random.randint(0, 999))
    else:
        return fake.user_name() + str(random.randint(0, 999))

# دالة لإنشاء حساب إنستغرام باستخدام بروكسي
def create_instagram_account(username, email, password, profile_image, proxy):
    # إعداد خيارات المتصفح مع البروكسي
    options = webdriver.ChromeOptions()
    options.add_argument(f'--proxy-server={proxy}')
    options.add_argument('--headless')  # تشغيل المتصفح في الخلفية
    driver = webdriver.Chrome(options=options)

    try:
        # الانتقال إلى صفحة إنشاء حساب إنستغرام
        driver.get('https://www.instagram.com/accounts/emailsignup/')
        time.sleep(2)

        # ملء النموذج الأولي
        full_name = fake.name()
        driver.find_element(By.NAME, 'emailOrPhone').send_keys(email)
        driver.find_element(By.NAME, 'fullName').send_keys(full_name)
        driver.find_element(By.NAME, 'username').send_keys(username)
        driver.find_element(By.NAME, 'password').send_keys(password)
        driver.find_element(By.NAME, 'password').send_keys(Keys.RETURN)
        time.sleep(2)  # انتظار تحميل الصفحة التالية

        # إدخال تاريخ الميلاد
        # اختيار اليوم
        day_select = Select(driver.find_element(By.XPATH, '//select[@title="Day"]'))
        day_select.select_by_value(str(random.randint(1, 28)))  # اختيار يوم عشوائي

        # اختيار الشهر
        month_select = Select(driver.find_element(By.XPATH, '//select[@title="Month"]'))
        month_select.select_by_value(str(random.randint(1, 12)))  # اختيار شهر عشوائي

        # اختيار السنة
        year_select = Select(driver.find_element(By.XPATH, '//select[@title="Year"]'))
        year_select.select_by_value(str(random.randint(1990, 2000)))  # اختيار سنة عشوائية

        # النقر على "Sign Up" مرة أخرى
        driver.find_element(By.XPATH, '//button[text()="Sign Up"]').click()
        time.sleep(5)  # انتظار إكمال التسجيل

        # كتابة بيانات الحساب في ملف ccv.txt
        with open('ccv.txt', 'a') as file:
            file.write(f"{email}:{password}:{full_name}\n")

    finally:
        driver.quit()

# دالة رئيسية لإنشاء الحسابات
def main():
    accounts = []
    num_accounts = 50  # عدد الحسابات المراد إنشاؤها

    for i in range(num_accounts):
        # تحديد النوع بناءً على النسب المطلوبة
        if i < num_accounts * 0.25:
            gender = 'male'
        elif i < num_accounts * 0.5:
            gender = 'female'
        else:
            gender = None  # صور حيوانات وطبيعة

        # إنشاء بيانات وهمية
        username = generate_instagram_username(gender)
        email = get_temp_email()
        password = fake.password()
        profile_image = download_profile_image(i, gender)

        if email and profile_image:
            # تحديد البروكسي
            proxy = proxies[i % len(proxies)]  # استخدام بروكسي مختلف لكل حساب

            # إنشاء الحساب
            create_instagram_account(username, email, password, profile_image, proxy)

            # إضافة الحساب إلى القائمة
            accounts.append({
                'username': username,
                'email': email,
                'password': password,
                'profile_image': profile_image,
                'proxy': proxy
            })

            # طباعة تفاصيل الحساب
            print(f"تم إنشاء الحساب {i+1}: {username} - {email} - Proxy: {proxy}")

    # حفظ الحسابات في ملف
    save_accounts(accounts, filename='accounts.txt', format='txt')
    save_accounts(accounts, filename='accounts.json', format='json')

# دالة لحفظ البيانات في ملف .txt أو .json
def save_accounts(accounts, filename='accounts.txt', format='txt'):
    if format == 'txt':
        with open(filename, 'w') as file:
            for account in accounts:
                file.write(f"Username: {account['username']}, Email: {account['email']}, Password: {account['password']}, Proxy: {account['proxy']}\n")
    elif format == 'json':
        with open(filename, 'w') as file:
            json.dump(accounts, file, indent=4)

if __name__ == '__main__':
    main()