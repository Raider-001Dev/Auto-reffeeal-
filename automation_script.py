from appium import webdriver
import time
import os
from appium.webdriver.common.touch_action import TouchAction

# Setup untuk TempMail APK
def setup_temp_mail():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",  # Sesuaikan dengan versi Android emulator
        "deviceName": "Android Emulator",
        "app": os.path.abspath('TempMail.apk'),
        "appPackage": "com.ymdx.email",
        "appActivity": "com.ymdx.email.ui.activity.MainActivity",
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(5)  # Tunggu aplikasi dimuat

    # Dapatkan email dari TempMail
    email_element = driver.find_element_by_id("com.ymdx.email:id/email")
    email = email_element.text
    print(f"Generated Email: {email}")

    driver.quit()
    return email

# Setup untuk BB Cloud Phone APK
def setup_bb_cloud_phone(email):
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",  # Sesuaikan dengan versi Android emulator
        "deviceName": "Android Emulator",
        "app": os.path.abspath('BB_Cloud_Phone.apk'),
        "appPackage": "com.bbcloud.phone",
        "appActivity": "com.bbcloud.phone.ui.activity.SignUpActivity",
    }

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    time.sleep(5)  # Tunggu aplikasi dimuat

    # Isi email di form sign-up
    email_input = driver.find_element_by_id("com.bbcloud.phone:id/emailInput")
    email_input.send_keys(email)

    # Klik kirim untuk OTP
    send_button = driver.find_element_by_id("com.bbcloud.phone:id/sendButton")
    send_button.click()

    # Tunggu OTP
    time.sleep(10)  # Waktu tunggu bisa disesuaikan

    # Masukkan OTP secara manual atau otomatis
    otp_input = driver.find_element_by_id("com.bbcloud.phone:id/otpInput")
    otp_input.send_keys("123456")  # Ganti dengan metode untuk mengambil OTP

    # Masukkan password dan konfirmasi password
    password_input = driver.find_element_by_id("com.bbcloud.phone:id/passwordInput")
    password_input.send_keys("password123")

    confirm_password_input = driver.find_element_by_id("com.bbcloud.phone:id/confirmPasswordInput")
    confirm_password_input.send_keys("password123")

    # Klik tombol daftar
    sign_up_button = driver.find_element_by_id("com.bbcloud.phone:id/signUpButton")
    sign_up_button.click()

    # Tunggu proses pendaftaran selesai
    time.sleep(5)

    # Lanjut ke halaman task dan masukkan referral code
    task_button = driver.find_element_by_id("com.bbcloud.phone:id/taskButton")
    task_button.click()

    referral_code_input = driver.find_element_by_id("com.bbcloud.phone:id/referralCodeInput")
    referral_code_input.send_keys("62c208c1")

    ok_button = driver.find_element_by_id("com.bbcloud.phone:id/okButton")
    ok_button.click()

    driver.quit()

# Main function
def main():
    email = setup_temp_mail()
    setup_bb_cloud_phone(email)

if __name__ == "__main__":
    main()
