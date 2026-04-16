def numbers(lst):

    number_list=lst.split(",")
    number_set=set(number_list)
    number_list=list(number_set)
    numbers=[]
    for idex in number_list:
        try:
            num=float(idex)
            numbers.append(num)
        except:
            continue
    numbers.sort()
    n=len(numbers)
    max_number=numbers[-1]
    min_number=numbers[0]
    sum=0
    for i in range(n):
        sum+=numbers[i]
    ava_number=sum/n
    return{
        "number_list":numbers,
        "max_number":max_number,
        "min_number":min_number,
        "ava_number":ava_number
        }
number_str=input("请输入一串数字：")
result=numbers(number_str)
print(result)