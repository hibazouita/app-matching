
import warnings

warnings.filterwarnings('ignore')

import fitz



import sys
doc=fitz.open(sys.argv[1])

doc2=fitz.open(sys.argv[2])

text = "akwel"

   

# iterating through pages for highlighting the input phrase

for page in doc:

    match_words = page.search_for(text)

   

    for word in match_words:

        highlight = page.add_highlight_annot(word)

        highlight.update()

for page in doc2:

    match_words = page.search_for(text)

   

    for word in match_words:

        highlight = page.add_highlight_annot(word)

        highlight.update()    

# saving the pdf file as highlighted.pdf

name1=sys.argv[3]

name2=sys.argv[4]
#url1="C:/Users/Hiba Zouita/app-matching/client/server/uploads/highlited-"+str(name1)

url1="C:/Users/Hiba Zouita/app-matching/back-end/public/output/highlited-"+str(name1)
url2="C:/Users/Hiba Zouita/app-matching/back-end/public/output/highlited-"+str(name2)
doc.save(url1)
doc.save(url2)
print(url1)
print(url2)
print("hello from python",sys.argv[5])


