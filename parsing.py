from bs4 import BeautifulSoup as BS

with open("freq.html") as file:
    src = file.read()


#print (src)

soup = BS(src, "lxml")

f = open("names.txt", "w")

all_words = soup.find_all("td")
for word in all_words:
    temp_str = word.text
    if (len(temp_str) > 0 and str.find(' ') == -1):
        if ((word.text[0] <= 'Я' and word.text[0] >= 'А')
                or (word.text[0] <= 'я' and word.text[0] >= 'а')):
            f.write(word.text + '\n')
