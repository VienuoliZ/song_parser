# https://www.upwork.com/job/Python-Scraping_~0153d46377d3863aa0/
# https://www.amalgama-lab.com/songs/t/tones_and_i/dance_monkey.html

# Hi! I need a scraper for a website www.amalgama-lab.com, where I will put a link of lyrics with translation. And after I will get the result in the namesong.csv file.
# for example, I put link https://www.amalgama-lab.com/songs/t/tones_and_i/dance_monkey.html
# and I will get result namesong.csv file which contains
# "They say, "Oh my god, I see the way you shine
# Люди говорят: "Боже мой, я вижу, как ты сияешь!
# Take your hands, my dear, and place them both in mine
# Возьми меня за руки, дорогая."

import requests
from lxml import etree
import lxml.html
import csv


def parse(url):
    try:
        api = requests.get(url)
    except:
        return
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    with open("namesong.csv", "w", newline='') as csv_file:
        write = csv.writer(csv_file)
        for i in range(len(text_original)):
            # print(text_original[i], text_translate[i])
            write.writerow(text_original[i])
            write.writerow(text_translate[i])

def main():
    parse("https://www.amalgama-lab.com/songs/t/tones_and_i/dance_monkey.html")

if __name__ == "__main__":
    main()
