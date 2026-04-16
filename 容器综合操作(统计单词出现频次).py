import operator

passage=input("请输入英文文章：")
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
if len(result_list)==0:
    print("输入的文本为空！")
elif len(result_list)<3:
    for i in range(len(result_list)):
        print(result_list[i])
else:
    print(f"top1:{result_list[0]}")
    print(f"top2:{result_list[1]}")
    print(f"top3:{result_list[2]}")

