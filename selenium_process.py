from typing import List, Tuple
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SeleniumController():
    @classmethod
    def crawling(cls) -> List[Tuple[str, str]]:
        """
        options.add_argument("headless")
        driver.quit()
        백 그라운드 설정 및 백 그라운드 크롬 종료
        """
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("detach", True)
        options.add_argument("headless")
        
        service = Service(executable_path=ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://www.youtube.com/@newskbs/videos")
        
        titles = driver.find_elements(By.CSS_SELECTOR, "#video-title")
        links = driver.find_elements(By.CSS_SELECTOR, "#video-title-link")
        
        title_list: List[Tuple[str, str]] = []
        title_end: str
        
        with open("title.txt", "r", encoding='utf-8') as f:
            title_end = f.readline()
        
        for title, link in zip(titles, links):
            if title.text == title_end:
                break
            else:
                title_list.append((title.text, link.get_attribute('href')))
        
        try:
            last_title:str = title_list[0][0]
        
            with open("title.txt", "w", encoding='utf-8') as f:
                f.write(last_title)
            
        except:
            pass
            
            
                
        driver.quit()
        
        return title_list
        
