#Gerekli kütüphanelerin ve UI dosyasının import edilmesi:
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import sys
from interface import *

#Kullanıcı isimlerinin eklenmesi için gereken global empty list:
emptyList = []

#Scraper ve çekilen verilerin UI üzerine yansıtılması:
def startProcess():
    try:
        #webdriver ayarları ve login işlemleri:
        options = webdriver.ChromeOptions()
        options.add_argument(r'--user-data-dir=C:\Users\kaan_\OneDrive\Masaüstü\windows_workspace\python\projeler\long\acmApp\userdata')
        PATH = r"C:\Users\kaan_\OneDrive\Masaüstü\windows_workspace\python\projeler\long\acmApp\chromedriver"
        driver = webdriver.Chrome(PATH, options=options)

        #driver üzerinden UI'daki linkin açılması:
        driver.get(ui.linePost.text())
        time.sleep(5)
        print('Login Basarili')

        #yorum path'i:
        firstComment = ['/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/ul[%s]/div/li/div/div/div[2]/h3/div/div/div/a']
        #daha fazla yorum görüntülemek için gerekeli button path'i:
        moreButton = '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/div[1]/ul/li/div/button'


        #gönderideki bütün yorumları görüntüleyebilmek için gereken döngü:
        k = True
        while k == True:
            try:
                driver.find_element(By.XPATH, moreButton).click()
                print('Tuş Bulundu')
                time.sleep(3)

            except:
                print('Tuş Kalmadı')
                k = False


        #gönderideki yorumları çekebilmek ve UI üzerinde görüntüleyebilmek için gereken döngü:
        ui.textAll.clear()
        j = 0
        while j != 1000:
            for a in firstComment:
                val = a % j
                elements = driver.find_elements(By.XPATH, val)
                for b in elements:
                    print(j, '-', b.text)
                    ui.textAll.append(b.text)
                    emptyList.append(b.text)

            j = j + 1


        print('İşlem Tamamlandı.')
        time.sleep(1)
        ui.linePost.clear()
        driver.quit()


    except:
        print("Link geçersiz veya eksik.")
        ui.textAll.setText("Link geçersiz veya eksik.")


#Gelen bütün kullanıcı isimlerinin shuffle edilme ve rastgele şekilde seçilme işlemi:
def drawProcess():
    try:
        random.shuffle(emptyList)
        winner = random.choice(emptyList)
        print(winner)
        ui.textWinners.append(winner)
        emptyList.remove(winner)
    except:
        print('Çekiliş Tamamlandı')
        ui.textWinners.append('Çekiliş Tamamlandı.')


#UI üzerindeki bütün göstergelerin sıfırlanması:
def clearAll():
    try:
        ui.textWinners.clear()
        ui.textAll.clear()
        ui.linePost.clear()
    except:
        print("Silinecek bir değer yok.")


#Uygulamanın kapatılması:
def endofProcess():
    sys.exit(app.exec())


#Kullanıcı arayüzünün kurulumu ve çalıştırılması:
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    ui.btnScraper.clicked.connect(startProcess)
    ui.btnRandom.clicked.connect(drawProcess)
    ui.btnClear.clicked.connect(clearAll)
    ui.btnQuit.clicked.connect(endofProcess)

    sys.exit(app.exec())


