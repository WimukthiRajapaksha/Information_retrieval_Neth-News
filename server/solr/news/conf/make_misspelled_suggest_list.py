# -*- coding: utf-8 -*-
import codecs

# inputs
bag_of_words = "bag_of_words.txt"


phonetic_macthing_letters={'ශ':'ස','ෂ':'ස','ණ':'න','ළ':'ල','ඝ':'ග','ඛ':'ක','ඵ':'ප','භ':'බ','ඹ':'බ','ඡ':'ච','්ඨ':'ට','ථ':'ත','ධ':'ද'}

# read all bag_of_words
bag_of_words = [str(l.strip()) for l in open(bag_of_words)]
# remove duplicates and sort accesnding order
bag_of_words = sorted(set(bag_of_words))


# open file to save output
suggest_dict = codecs.open('misspelled_suggestion_dictionary.txt',"w+", encoding='utf-8')

for w in bag_of_words:
    for l in w:
        if(l in phonetic_macthing_letters.keys()):
             word=w
             word=word.replace(l,phonetic_macthing_letters[l])
             suggest_dict.write(word+ " => "+w+"\n")
                        



# close file
suggest_dict.close()

