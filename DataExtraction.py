from bs4 import BeautifulSoup
from seleniumbase import Driver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import csv
from sys import exit
def bypass_cloudflare(driver):
    print("Cloudflare Bypass ediliyor...")
    WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Cloudflare güvenlik görevi içeren pencere öğeleri']")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@class='ctp-checkbox-label']"))).click()
    print("Cloudflare Bypass edildi.")    
    return True
driver = Driver(uc=True,)
driver.get("https://www.sahibinden.com/satilik-daire/malatya")
print("Cloudflare Bypass ediliyor...")
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Cloudflare güvenlik görevi içeren pencere öğeleri']")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@class='ctp-checkbox-label']"))).click()
print("Cloudflare Bypass edildi.")
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
titles_raw = soup.find_all(class_="classifiedTitle")
specs_raw = soup.find_all(class_="searchResultsAttributeValue")
price_raw = soup.find_all(class_="classified-price-container")
dates_raw = soup.find_all(class_="searchResultsDateValue")
districts_raw = soup.find_all(class_="searchResultsLocationValue")
titles = []
h_refs = []
for tt in titles_raw:
    titles.append(tt.getText().strip())
    h_refs.append("https://www.sahibinden.com" + tt.get("href"))
specs = [sp.getText().strip() for sp in specs_raw]
rooms = specs[1::2]
square_meters = specs[0::2]
prices = [pr.getText().strip() for pr in price_raw]
dates = [dt.getText().strip().replace("\n\n", " ") for dt in dates_raw]
districts = [ds.getText().strip() for ds in districts_raw]
time.sleep(random.uniform(1, 2))
'''pages = 3 # Toplam sayfa sayısı
for page in range(1, pages + 1): # 2. sayfadan son sayfaya kadar döngü
    offset = (page - 1) * 20 # Her sayfanın URL'indeki pagingOffset değeri
    driver.get("https://www.sahibinden.com/satilik-daire/malatya?pagingOffset=" + str(offset)) # Sayfaya geçmek için
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    titles_raw = soup.find_all(class_="classifiedTitle")
    specs_raw = soup.find_all(class_="searchResultsAttributeValue")
    price_raw = soup.find_all(class_="classified-price-container")
    dates_raw = soup.find_all(class_="searchResultsDateValue")
    districts_raw = soup.find_all(class_="searchResultsLocationValue")
    titles = []
    h_refs = []
    for tt in titles_raw:
        titles.append(tt.getText().strip())
        h_refs.append("https://www.sahibinden.com" + tt.get("href"))
    specs = [sp.getText().strip() for sp in specs_raw]
    rooms = specs[1::2]
    square_meters = specs[0::2]
    prices = [pr.getText().strip() for pr in price_raw]
    dates = [dt.getText().strip().replace("\n\n", " ") for dt in dates_raw]
    districts = [ds.getText().strip() for ds in districts_raw]
    time.sleep(random.uniform(1, 2))
    for i in range(len(titles)):
        inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
        print("Title: " + titles[i])
        print("Link: " + h_refs[i])
        print("Square Meters: " + square_meters[i])
        print("Rooms: " + rooms[i])
        print("Price: " + prices[i])
        print("Date: " + dates[i])
        print("District: " + districts[i])
        print("--------------------------------------------------" + "\n")'''              
def save_to_csv(data):
    with open("ilan.csv", "a", encoding="utf-8", newline="") as f:  # "a" modunda ve newline="" parametresi ile aç
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)
            
data = []
data.append(["title","link","square_meters","rooms","price","date","district"]) # Sütun başlıklarını listeye ekle

pages = 49 # Toplam sayfa sayısı
for page in range(1, pages + 1): # 2. sayfadan son sayfaya kadar döngü
    offset = (page - 1) * 20 # Her sayfanın URL'indeki pagingOffset değeri
    driver.get("https://www.sahibinden.com/satilik-daire/malatya?pagingOffset=" + str(offset)) # Sayfaya geçmek için
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    titles_raw = soup.find_all(class_="classifiedTitle")
    specs_raw = soup.find_all(class_="searchResultsAttributeValue")
    price_raw = soup.find_all(class_="classified-price-container")
    dates_raw = soup.find_all(class_="searchResultsDateValue")
    districts_raw = soup.find_all(class_="searchResultsLocationValue")
    titles = []
    h_refs = []
    for tt in titles_raw:
        titles.append(tt.getText().strip())
        h_refs.append("https://www.sahibinden.com" + tt.get("href"))
    specs = [sp.getText().strip() for sp in specs_raw]
    rooms = specs[1::2]
    square_meters = specs[0::2]
    prices = [pr.getText().strip() for pr in price_raw]
    dates = [dt.getText().strip().replace("\n\n", " ") for dt in dates_raw]
    districts = [ds.getText().strip() for ds in districts_raw]
    time.sleep(random.uniform(1, 2))
    for i in range(len(titles)):
        data.append([titles[i], h_refs[i], square_meters[i], rooms[i], prices[i], dates[i], districts[i]])
save_to_csv(data) # Her sayfadaki verileri csv dosyasına kaydet
#data = [] # Listeyi sıfırla
     