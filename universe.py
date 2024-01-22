import os
<<<<<<< HEAD
'''
=======

>>>>>>> remotes/origin/main
folder_path = "./SparkUniverse/save"
file_names = os.listdir(folder_path)

if len(file_names) == 0:
    print("创建一个新的游戏,输入新游戏的名称:")
<<<<<<< HEAD
    #print("command001")
    file_name = input()
    print("这一局游戏内你希望被称为:")
    #print("command002")
    user_name = input()
    print("这一局游戏内你希望你领导的的团体被称为:")
    #print("command003")
=======
    file_name = input()
    print("这一局游戏内你希望被称为:")
    user_name = input()
    print("这一局游戏内你希望你领导的的团体被称为:")
>>>>>>> remotes/origin/main
    company_name = input()

    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
        file.write(user_name + '\n')
        file.write(company_name + '\n')
<<<<<<< HEAD
else:
    print(file_names)
'''

#定义全局参数
file_name = ''
user_name = ''
company_name = ''
game_switch = False
folder_path = "./SparkUniverse/save"
file_names = os.listdir(folder_path)
print("echo-0000") #echo-0000:进程开始
#菜单循环
while game_switch == False :
    try:
        input_new = str(input())
        if "-" not in input_new :
            print("echo-0001") #echo-0001:非法指令
        else :
            command_list = input_new.split("-")
            command_head = command_list[0]
            if command_head == "start" :
                if file_name != '' and user_name != '' and company_name != '':
                    game_switch = True
                    if file_name not in file_names:
                        file_path = os.path.join(folder_path, file_name)
                        with open(file_path, 'w') as file:
                            file.write(user_name + '\n')
                            file.write(company_name + '\n')
                    print("echo-1001")#echo-1001:游戏开始
                else:
                    print("echo-0002") #echo-0002:不满足游戏开始的条件
            if command_head == "ls":#ls-file查询已经读入存档信息
                if command_list[1] == "file":
                    print("file_name-",file_name)
                elif command_list[1] =="user":
                    print("user_name-",user_name)
                elif command_list[1] =="company":
                    print("company_name-",company_name)
                else:
                    print("echo-0003") #echo-0003:游戏尚未开始，指令无法生效
            if command_head == "change":#change指令用于修改user_name和company_name，格式分别是change-user-newmessage，change-company-newmessage
                if command_list[1] == "user":
                    user_name = command_list[2]
                elif command_list[1] == "company":
                    company_name = command_list[2]
                else:
                    print("echo-0004") #echo-0004:你在尝试修改不可强行修改的存档内容
            if command_head == "load":#load指令用于加载存档，如果存档不存在，则会创建存档，格式是load-file-filename
                if command_list[1] == "file":
                    file_name = command_list[2]
                    if file_name not in file_names:
                        user_name = ''
                        company_name = ''
                    else:
                        print()#直接读取存档
    except:
        print("echo-0005")#echo-0005:菜单异常，正在重启菜单模块

        
print("echo-####")#echo-####:进程结束

=======
    
    
else:
    print(file_names)
>>>>>>> remotes/origin/main
