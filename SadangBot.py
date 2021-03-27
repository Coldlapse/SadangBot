from selenium import webdriver
import time
import random

randomwaittime = random.randrange(1, 300)
print("Random Wait Time : " + str(randomwaittime), flush=True)
time.sleep(randomwaittime)
print("Starting Job", flush=True)

with Display():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.implicitly_wait(3)

        login=1

        id='' # 자신의 디씨 ID 입력
        pw='' # 자신의 디씨 PW 입력

        if login==1 :

            # 로그인
            driver.get('https://gall.dcinside.com/')
            time.sleep(1)

            driver.find_element_by_xpath("//a[contains(text(),'로그인')]").click()
            time.sleep(1)

            driver.find_element_by_id('id').send_keys(id)
            time.sleep(1)

            driver.find_element_by_id('pw').send_keys(pw)
            time.sleep(1)

            driver.find_element_by_xpath("//button[@class='btn_blue small btn_wfull']").click()
            time.sleep(1)

            print("Log-in Successful", flush=True)

            # 관리 페이지 이동
            driver.get(f'https://gall.dcinside.com/mgallery/management?id=electronicmoney')
            time.sleep(1)
            nonmember = driver.find_elements_by_xpath("//button[@class='font_lightblue set_modify']")
            time.sleep(1)
            nonmember[5].click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='right_cont_wrap']/div/fieldset/div[9]/div/div[3]/div[1]/div[1]/div[2]/div/div").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='right_cont_wrap']/div/fieldset/div[9]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[4]").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='right_cont_wrap']/div/fieldset/div[9]/div/div[3]/div[1]/div[1]/div[1]/div/div").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='right_cont_wrap']/div/fieldset/div[9]/div/div[3]/div[1]/div[1]/div[1]/div/ul/li[4]").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='right_cont_wrap']/div/fieldset/div[9]/div/div[3]/div[1]/div[1]/div[1]/button").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='right_cont_wrap']/div/fieldset/div[9]/div/div[3]/div[1]/div[1]/div[2]/button").click()
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='right_cont_wrap']/div/fieldset/div[9]/div/div[3]/div[2]/button[1]").click()
            time.sleep(1)

            print("Job Finished", flush=True)

    finally:
        driver.quit()