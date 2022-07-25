from random import randint

#import requests
#from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

nums=set([])
for e in range(1):
    for i in range(106):

        urls = []
        for j in range(106):
            urls.append(0)

        urls[0] = '4chan'
        urls[1] = 'anime'
        urls[2] = 'pics'
        urls[3] = 'random'
        urls[4] = 'images'
        urls[5] = 'games'
        urls[6] = 'lmao'
        urls[7] = 'programs'
        urls[8] = 'news'
        urls[9] = 'computer'
        urls[10] = 'mouse'
        urls[11] = 'white'
        urls[12] = 'black'
        urls[13] = 'power'
        urls[14] = 'gather'
        urls[15] = 'meme'
        urls[15] = 'dark'
        urls[16] = 'чёрный'
        urls[17] = 'рука'
        urls[18] = 'зомби'
        urls[19] = 'поезд'
        urls[20] = 'cute'
        urls[21] = 'фон'
        urls[22] = 'cursedimages'
        urls[23] = 'dogs'
        urls[24] = 'pepe'
        urls[25] = 'betterttv'
        urls[26] = 'betterttvemotes'
        urls[27] = 'nintendo memes'
        urls[28] = 'анекдот'
        urls[29] = 'samp'
        urls[30] = 'qr'
        urls[31] = 'red'
        urls[32] = 'red'
        urls[33] = 'classic memes'
        urls[34] = 'yellow'
        urls[35] = 'yellow'
        urls[36] = 'btsart'
        urls[37] = 'green'
        urls[38] = 'green'
        urls[39] = 'furry'
        urls[40] = 'blue'
        urls[41] = 'мемы смешарики'
        urls[42] = 'мемыизодноклассников'
        urls[43] = 'go'
        urls[44] = 'stop'
        urls[45] = 'welcome'
        urls[46] = 'determine'
        urls[47] = 'ignorant'
        urls[48] = 'year'
        urls[49] = 'major'
        urls[50] = 'slow'
        urls[51] = 'spontaneous'
        urls[52] = 'city'
        urls[53] = 'sit'
        urls[54] = 'scholar'
        urls[55] = 'aloof'
        urls[56] = 'package'
        urls[57] = 'congress'
        urls[58] = 'stress'
        urls[59] = 'scene'
        urls[60] = 'reception'
        urls[61] = 'spare'
        urls[62] = 'claim'
        urls[63] = 'terrify'
        urls[64] = 'destruction'
        urls[65] = 'swipe'
        urls[66] = 'weave'
        urls[67] = 'mixture'
        urls[68] = 'dream'
        urls[69] = 'rifle'
        urls[70] = 'left'
        urls[71] = 'incentive'
        urls[72] = 'control'
        urls[73] = 'warn'
        urls[74] = 'beer'
        urls[75] = 'established'
        urls[76] = 'deviation'
        urls[77] = 'conductor'
        urls[78] = 'calculation'
        urls[79] = 'archive'
        urls[80] = 'spy'
        urls[81] = 'style'
        urls[82] = 'fairy'
        urls[83] = 'snake'
        urls[84] = 'angel'
        urls[85] = 'angle'
        urls[86] = 'diagram'
        urls[87] = 'fireplace'
        urls[88] = 'attention'
        urls[89] = 'disgrace'
        urls[90] = 'opportunity'
        urls[91] = 'julius caesar'
        urls[92] = 'map'
        urls[93] = 'management'
        urls[94] = 'potato'
        urls[95] = 'negotiation'
        urls[96] = 'session'
        urls[97] = 'environment'
        urls[98] = 'exam'
        urls[99] = 'worker'
        urls[100] = 'signature'
        urls[101] = 'clothes'
        urls[102] = 'cell'
        urls[103] = 'message'
        urls[104] = 'engineering'
        urls[105] = 'dota'
        
        
        
        


        rand = str(randint(0, 100))
        word = urls[i]
        url = 'https://www.google.kz/search?q=' + word + '%20' + rand + '&tbm=isch&hl=ru&tbs=isz:i&authuser=0&sa=X&ved=0CAQQpwVqFwoTCKipyraR0PYCFQAAAAAdAAAAABAC&biw=1491&bih=751'
        #url = 'https://yandex.kz/images/search?text=' +  word + '%20' + rand + '&iorient=square&isize=small&from=tabbar'
        print(url)







        driver = webdriver.Chrome(
            executable_path="C:/Users/Себастиан/AppData/Local/Programs/Python/picture/pic/Scripts/main/chromedriver_win32/chromedriver.exe"
        )
        driver.maximize_window()
        #driver.set_window_size(500, 500)
        try:
            driver.get(url=url)
            time.sleep(0.5)

            SCROLL_PAUSE_TIME = 0.1

            # Get scroll height
            last_height = driver.execute_script("return document.body.scrollHeight")

            time_for_web = 0
            while True:
                # Scroll down to bottom
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # Wait to load page
                time.sleep(SCROLL_PAUSE_TIME)

                # Calculate new scroll height and compare with last scroll height
                new_height = driver.execute_script("return document.body.scrollHeight")
                time.sleep(1)


                try:
                    driver.find_element(by=By.CLASS_NAME, value='r0zKGf').click()
                except Exception as _ex:
                    pass

                try:
                    driver.find_element(by=By.CLASS_NAME, value='mye4qd').click()
                except Exception as _ex:
                    pass

                if driver.find_element(by=By.CLASS_NAME, value='OuJzKb.Bqq24e').text == "Больше ничего нет":
                    time_for_web = time_for_web + 1


                if time_for_web == 2:
                    print(driver.find_element(by=By.CLASS_NAME, value='OuJzKb.Bqq24e').text)
                    with open("C:/Users/Себастиан/AppData/Local/Programs/Python/picture/pic/Scripts/main/page_html.html", "w", encoding="utf-8" ) as file:
                        file.write(driver.page_source)
                    break
        except Exception as _ex:
                print(_ex)
        finally:
            driver.close()
            driver.quit()


        with open("C:/Users/Себастиан/AppData/Local/Programs/Python/picture/pic/Scripts/main/page_html.html", "r", encoding="utf-8") as file:
            nums_split=set([])
            for i in file:
                nums_split.add(i[:-1])

            nums_split=str(nums_split)
            html_split = nums_split.split()





        def url_search(S, sample):
            global html_split
            Res = 0

            m = len(sample)
            n = len(S)

            p = [0] * m
            j = 0
            i = 1

            while i < m:
                if sample[j] == sample[i]:
                    p[i] = j + 1
                    i += 1
                    j += 1
                else:
                    if j == 0:
                        p[i] = 0
                        i += 1
                    else:
                        j = p[j - 1]

                j = 0
                i = 0

                while i < n:
                    if S[i] == sample[j]:
                        i += 1
                        j += 1
                        if j == m:
                            Res += 1
                            if i == n:
                                print("Подстрока не найдена")
                            else:
                                j = 0
                    else:
                        if j > 0:
                            j = p[j - 1]
                        else:
                            i += 1

                return Res;




        new_array = []
        new_array2 = []
        new_array3 = []
        new_array4 = []
        new_array5 = []
        #new_array6 = []
        #new_array7 = []

        for i in range(len(html_split)):
            if url_search(html_split[i], 'https://encrypted-tbn0.gstatic.com/images?q=tbn:') == 1:
                new_array.append(html_split[i])

        for i in range(len(new_array)):
            new_array2.append(new_array[i].replace('src="', ''))

        for i in range(len(new_array)):
            new_array3.append(new_array2[i].replace('amp;s"/>', ''))

        for i in range(len(new_array)):
            new_array4.append(new_array3[i].replace('"></div><div', ''))

        for i in range(len(new_array)):
            new_array5.append(new_array4[i].replace('data-', ''))

        #for i in range(len(new_array)):
         #   new_array6.append(new_array5[i].replace('&amp;usqp=CAU', ''))

        #for i in range(len(new_array)):
        #    new_array7.append(new_array6[i].replace('&amp;usqp=CA', ''))


        for i in new_array5:
            nums.add(i[:-1])

        new_array = []
        new_array2 = []
        new_array3 = []
        new_array4 = []
        new_array5 = []


#def main(word_number):
   # get_source_html(generate_url(word_number))
   # html_spliter()
   # search_filter()


#if __name__ == "__main__":
 #   for j in range(10):
  #      for i in range(74):
   #         main(i)


f = open('urls.txt', 'a')
for i in nums:
    f.write(i + '\n')
f.close()


