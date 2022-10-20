import urllib.request  # the lib that handles the url stuff
import re
data = urllib.request.urlopen('https://raw.githubusercontent.com/dwyl/english-words/master/words_dictionary.json')
wordsHangman=[]

for line in data:
    word=re.findall(r'"(.*?)"', str(line))
    
    if len(word)>0:
        if len(word[0])>5:
            wordsHangman+=word
            
with open("englishHangman.py","a") as f:
    print("words="+str(wordsHangman),file=f)
    

