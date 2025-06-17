import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--headless=new") 

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def aceitar_cookies(driver, timeout=10):
    try:
        wait = WebDriverWait(driver, timeout)
        aceitar_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cookie-consent-accept"))
        )
        aceitar_btn.click()
        print("Cookies aceites.")
        time.sleep(1)
    except Exception:
        print("Botão de cookies não encontrado ou já foi aceite.")

def scroll_to_bottom(driver, pause_time=3, max_scrolls=30):
    scrolls = 0
    last_count = 0

    while scrolls < max_scrolls:
        eventos = driver.find_elements(By.CSS_SELECTOR, "li.viral-event")
        current_count = len(eventos)

        if current_count == last_count:
            break  
        last_count = current_count

        try:
            ultimo_evento = eventos[-1]
            ActionChains(driver).move_to_element(ultimo_evento).perform()
        except Exception as e:
            print(f"Erro ao fazer scroll: {e}")
            break

        time.sleep(pause_time)
        print(f"[Scroll {scrolls + 1}] Eventos carregados: {current_count}")
        scrolls += 1

def extract_events(driver, base_url):
    eventos = []
    event_elements = driver.find_elements(By.CSS_SELECTOR, "li.viral-event")

    print(f"\nEventos encontrados: {len(event_elements)}")

    for idx, event_el in enumerate(event_elements):
        try:
            try:
                title_el = event_el.find_element(By.CSS_SELECTOR, "div.viral-event-title a")
                titulo = title_el.text.strip()
                link = title_el.get_attribute("href")
            except NoSuchElementException:
                titulo = ""
                link = ""

            if not link and titulo:
                try:
                    link = event_el.find_element(By.TAG_NAME, "a").get_attribute("href")
                except NoSuchElementException:
                    link = ""

            if not titulo and link:
                titulo = link.strip("/").split("/")[-1].replace("-", " ").capitalize()

            if link and not link.startswith("http"):
                link = base_url + link

            try:
                start_time = event_el.find_element(By.CSS_SELECTOR, "time[itemprop='startDate']").get_attribute("datetime")
            except NoSuchElementException:
                start_time = ""

            try:
                hora = event_el.find_element(By.CSS_SELECTOR, "div.viral-event-hour").text.strip()
            except NoSuchElementException:
                hora = ""

            try:
                local = event_el.find_element(By.CSS_SELECTOR, "a.viral-event-place span[itemprop='name']").text.strip()
            except NoSuchElementException:
                try:
                    local = event_el.find_element(By.CSS_SELECTOR, "a.node-name span.node-name").text.strip()
                except NoSuchElementException:
                    local = ""

            eventos.append({
                "titulo": titulo,
                "data_hora": start_time,
                "hora": hora,
                "local": local,
                "link": link
            })

        except Exception as e:
            print(f"[{idx}] Erro ao processar evento: {e}")

    return eventos

def main():
    base_url = "https://www.viralagenda.com"
    url = f"{base_url}/pt/viana-do-castelo"

    driver = setup_driver()
    driver.get(url)

    aceitar_cookies(driver)
    scroll_to_bottom(driver)

    eventos = extract_events(driver, base_url)

    driver.quit()

    for evento in eventos:
        print(evento)

if __name__ == "__main__":
    main()
