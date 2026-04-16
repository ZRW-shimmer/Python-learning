import operator
passage=""
try:
    with open(r"C:\Users\86156\Desktop\英语短文.txt","r",encoding="utf-8") as passage_file:
        passage=passage_file.read()
except FileNotFoundError:
    print("文件不存在！")
except OSError:
    print("路径非法！")

sentences_list=passage.split(".")
word_list=[]
for sentence in sentences_list:
    sentence_list=sentence.split(",")
    for element in sentence_list:
        element_list=element.split(" ")
        for word in element_list:
            if word.strip():
                word_list.append(word.lower())

word_dict={}
for word in word_list:
    word_dict[word]=word_list.count(word)

result_list=sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)


with open(r"C:\Users\86156\Desktop\text.txt","w",encoding="utf-8") as result_file:
    for word,count in result_list:
        result_file.write(f"单词：{word},次数：{count}\n")




