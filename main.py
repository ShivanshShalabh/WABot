msg = "Hi! I am Shivansh, the Kaveri House Captain. Thanks for filling out the interest form for the Teachers' Day Programme. We have added a question to the from to know whether you are interested in being a part of the music or the dance segement of the programme. We thus request you to kindly answer the form again. Thank you for your cooperation. Form link: https://forms.gle/YCw96JPyr8ysv3MNA"

from selenium import webdriver
import time

def clickBtn(web,i=None):
    try:
        time.sleep(5)
        web.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
        if i:
            print("Successfully clicked button {}".format(i))
    except:
        print("Failed to click button {}".format(i))
        clickBtn(web)
    

web = webdriver.Chrome()
web.get("https://web.whatsapp.com/")
check = input("Done logging in? (y/n): ")
for i in lst:
    try:
        web.get(f"https://web.whatsapp.com/send?phone={i}&text={msg}")
        clickBtn(web,i)
        check = input("Done sending message to {}? (y/n): ".format(i))
    except Exception as e:
        print(e)
        print("Failed to send message to {}".format(i))
        continue
