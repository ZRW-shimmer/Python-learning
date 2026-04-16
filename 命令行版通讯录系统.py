from asyncio.windows_events import NULL

contact_list = []
key=NULL

def save_data(contact_list):
    with open(r"C:\Users\86156\Desktop\命令行版通讯录.txt","w",encoding="utf-8") as e:
        for i in range(len(contact_list)):
            e.write(f"{contact_list[i][0]},{contact_list[i][1]},{contact_list[i][2]}\n")

def add_contact(name,phone,remark):
    contact_list.append([name,phone,remark])
    return

def search_contact(key):
    for i in range(len(contact_list)):
        if key in contact_list[i][0] or key in contact_list[i][1] or key in contact_list[i][2]:
            print(f"{contact_list[i][0]},{contact_list[i][1]},{contact_list[i][2]}")
        else:
            print("未找到联系人")
    return

def updata_contact(name,phone,remark):
    for i in range(len(contact_list)):
        if contact_list[i][0]==name:
            contact_list[i][1]=phone
            contact_list[i][2]=remark
    return

def delete_contact(name):
    for i in range(len(contact_list)):
        if contact_list[i][0]==name:
            del contact_list[i]
            print("删除成功!")
            return
        else:
            print("未找到联系人！")
def show_nume():
    print("\n"+"="*30)
    print("         命令行版通讯录")
    print("\n"+"="*30)
    print("1.新增联系人")
    print("2.查找联系人")
    print("3.修改联系人")
    print("4.删除联系人")
    print("5.退出系统")
    print("\n"+"="*30)


def main():

    global contact_list
    global key

    try:
        with open(r"C:\Users\86156\Desktop\命令行版通讯录.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, phone, remark = line.strip().split(",")
                contact_list.append([name, phone, remark])

    except FileNotFoundError:
        print("未找到通讯录！")
    while True:
        show_nume()
        choice = int(input("请输入你要选择的功能："))
        if choice == 1:
            name = input("请输入姓名：")
            phone = input("请输入手机号：")
            remark = input("请输入关系：")
            add_contact(name, phone, remark)
            print("新增联系人成功！")
            continue
        elif choice == 2:
            key = input("请输入要查找联系人的关键词：")
            search_contact(key)
        elif choice == 3:
            name = input("请输入要修改的联系人姓名：")
            phone = input("请输入修改后的手机号：")
            remark = input("请输入修改后的关系：")
            updata_contact(name, phone, remark)
            print("修改成功！")
        elif choice == 4:
            name = input("请输入要删除的联系人的姓名：")
            delete_contact(name)
            print("删除成功！")
        elif choice == 5:
            print("正在保存通讯录")
            save_data(contact_list)
            break
        else:
            print("请输入1-5的数字！")
if __name__=="__main__":
    main()


