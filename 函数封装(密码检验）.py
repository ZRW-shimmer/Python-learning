def check_passward(str):
    keys_list=list(str)
    L=len(keys_list)
    Number_keys=['1','2','3','4','5','6','7','8','9','0']
    Symble=['!','@','#','$','%','^','&','*']
    Small_keys=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    Big_keys=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    if L<8 :
        return "错误，密码长度不够！"
    number=0
    symble=0
    small=0
    big=0
    is_success=True
    for i in range(L):
        if keys_list[i] in Number_keys:
            number+=1
        elif keys_list[i] in Symble:
            symble+=1
        elif keys_list[i] in Small_keys:
            small+=1
        elif keys_list[i] in Big_keys:
            big+=1
        else:
            is_success=False
            break
    def judge(a,b,c,d):
        if a==0:
            print("缺少数字！")
        if b==0:
            print("缺少符号！")
        if c==0:
            print("缺少小写字母！")
        if d == 0:
            print("缺少大写字母！")

    if number!=0 and small!=0 and big!=0 and is_success:
        return "合格的密码！"
    else:
        judge(number,symble,small,big)
        return "密码不合格！"
keys_str=input("请输入密码（至少8位）：")
print(check_passward(keys_str))

