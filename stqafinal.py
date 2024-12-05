from appium import webdriver
from appium.options.android import UiAutomator2Options
from time import sleep

# Fungsi untuk menjalankan pengujian pada emulator tertentu
def run_test_on_emulator(emulator_udid):
    # Konfigurasi Appium
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = f"Device_{emulator_udid}"
    options.udid = emulator_udid
    options.automation_name = "uiautomator2"
    options.app_package = "com.code2lead.kwad"
    options.app_activity = "com.code2lead.kwad.MainActivity"
    # Inisialisasi driver
    try:
        driver = webdriver.Remote("http://localhost:4723", options=options)
        print(f"Koneksi berhasil dengan {emulator_udid}!")
        # Menunggu aplikasi untuk dimuat
        sleep(5)
        # Klik tombol dengan ID 'Login'
        login_button = driver.find_element("id", "com.code2lead.kwad:id/Login")
        login_button.click()
        # Menunggu halaman login terbuka
        sleep(2)
        # Masukkan email di field 'Et4'
        email_field = driver.find_element("id", "com.code2lead.kwad:id/Et4")
        email_field.send_keys("admin@gmail.com")
        # Masukkan password di field 'Et5'
        password_field = driver.find_element("id", "com.code2lead.kwad:id/Et5")
        password_field.send_keys("admin123")
        # Klik tombol login dengan ID 'Btn3'
        login_submit_button = driver.find_element("id", "com.code2lead.kwad:id/Btn3")
        login_submit_button.click()
        # Tunggu proses login selesai
        sleep(2)
        # Masukkan teks ke ID 'Edt_admin'
        admin_text_field = driver.find_element("id", "com.code2lead.kwad:id/Edt_admin")
        admin_text_field.send_keys("Aku sekarang Admin")
        # Klik tombol dengan ID 'Btn_admin_sub'
        admin_submit_button = driver.find_element("id", "com.code2lead.kwad:id/Btn_admin_sub")
        admin_submit_button.click()
        # Tunggu proses selesai dan kembali ke halaman sebelumnya
        sleep(3)
        driver.back()  # Kembali pertama
        sleep(1)
        driver.back()  # Kembali kedua
        sleep(2)
        # Klik tombol dengan ID 'EnterValue'
        enter_value_button = driver.find_element("id", "com.code2lead.kwad:id/EnterValue")
        enter_value_button.click()
        # Menunggu halaman input terbuka
        sleep(2)
        # Mengisi input teks dengan ID 'Et1'
        input_field = driver.find_element("id", "com.code2lead.kwad:id/Et1")
        input_field.send_keys("Ini User")
        # Klik tombol dengan ID 'Btn1'
        submit_button = driver.find_element("id", "com.code2lead.kwad:id/Btn1")
        submit_button.click()
        # Tunggu proses selesai dan verifikasi apakah halaman berikutnya terbuka
        sleep(2)
        print(f"Tes berhasil dijalankan pada {emulator_udid}!")
    except Exception as e:
        print(f"Terjadi kesalahan pada {emulator_udid}: {e}")
    finally:
        # Tutup driver setelah pengujian selesai
        driver.quit()
# Daftar emulator yang akan diuji
emulator_list = ["emulator-5554", "emulator-5556"]
# Jalankan pengujian untuk setiap emulator
for emulator in emulator_list:
    print(f"Memulai pengujian untuk {emulator}...")
    run_test_on_emulator(emulator)
    print(f"Pengujian selesai untuk {emulator}.\n")
