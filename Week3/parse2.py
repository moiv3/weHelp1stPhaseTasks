from bs4 import BeautifulSoup

#online version WIP

import requests,time,csv

start_time = time.time()
url = 'https://www.ptt.cc/bbs/Lottery/index.html'
page_headers = {
    "cookie":"over18=1",
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
list_of_posts=[]

#configuration
pages_to_scrape = 3
publish_time_position = 3

#print('Status code: ', response.status_code)
#print('Text: ', response.text[:50])

for page in range(pages_to_scrape):
    print(url)
    #print("Parsing page",page+1,"...")
    response = requests.get(url,headers=page_headers)
    
    website = BeautifulSoup(response.text, "html.parser")
    #print(website)
    entries_in_page = website.find_all("div",class_="r-ent")

    for entry in entries_in_page:
        entry_dict={}
        #print(entry)
        #標題
        title = entry.find("div",class_="title")
        anchor = title.find("a")
        if anchor:
            #print(anchor.text)
            entry_dict["title"] = anchor.text
            #print("https://www.ptt.cc" + anchor['href'])
            inner_page = "https://www.ptt.cc" + anchor['href']
            inner_response = requests.get(inner_page,headers=page_headers)
            inner_website = BeautifulSoup(inner_response.text, "html.parser")
            art_meta_values = inner_website.find_all("span", class_="article-meta-value")
            try:
                #print(art_meta_values[publish_time_position].text)
                entry_dict["time"] = art_meta_values[publish_time_position].text
            except:
                #print("No publish time available")
                entry_dict["time"] = ""
            #also need to do online version!
            #inner_website = anchor["href"]
            #第4個值...在這邊先寫死，可以改成在外層就定義好?

        #推噓文數。先只處理html上的數字(正值，無值，爆文=100)
        #所有人都有nrec, 但沒顯示的不會有text
            score = entry.find("div",class_="nrec")
            if score.text:
                #print(int(score.text))
                entry_dict["score"]=int(score.text)
            else:
                #print("0")
                entry_dict["score"]=0

            list_of_posts.append(entry_dict)

        #else:
            #print("沒找到!")
        
    print(len(list_of_posts))

    last_page = website.find("a",string="‹ 上頁")
    url = "https://www.ptt.cc" + last_page['href']
    #print(url)

#for post in list_of_posts:
    #print(post["title"]+","+str(post["score"])+","+post["time"])

with open('article.csv', 'a', newline="", encoding='utf-8') as article_file:
    article_writer_object = csv.writer(article_file,delimiter=',')

    for post in list_of_posts:
        article_writer_object.writerow((post["title"],str(post["score"]),post["time"]))
        print(post["title"]+","+str(post["score"])+","+post["time"])

article_file.close()

end_time = time.time()
print(end_time - start_time,"s")

"""
#local version backup
        with open("LotteryP2080.html", encoding="utf8") as fp:
    print("Parsing page...")
    list_of_posts=[]
    website = BeautifulSoup(fp, "html.parser")
    entries_in_page = website.find_all("div",class_="r-ent")
    for entry in entries_in_page:
        entry_dict={}
        #print(entry)
        #標題
        title = entry.find("div",class_="title")
        anchor = title.find("a")
        if anchor:
            print(anchor.text)
            entry_dict["title"] = anchor.text
            with open("innerTest.html", encoding="utf8") as inner_fp:
                inner_website = BeautifulSoup(inner_fp, "html.parser")
                art_meta_values = inner_website.find_all("span", class_="article-meta-value")
                print(art_meta_values[3].text)
                entry_dict["time"] = art_meta_values[3].text
            #also need to do online version!
            #inner_website = anchor["href"]
            #第4個值...在這邊先寫死，可以改成在外層就定義好?

        #推噓文數。先只處理html上的數字(正值，無值，爆文=100)
        #所有人都有nrec, 但沒顯示的不會有text
            score = entry.find("div",class_="nrec")
            if score.text:
                print(int(score.text))
                entry_dict["score"]=int(score.text)
            else:
                print("0")
                entry_dict["score"]=0

            list_of_posts.append(entry_dict)

        else:
            print("沒找到!")

        """