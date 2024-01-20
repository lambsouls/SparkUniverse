import os

folder_path = "./SparkUniverse/save"
file_names = os.listdir(folder_path)

if len(file_names) == 0:
    print("创建一个新的游戏,输入新游戏的名称:")
    file_name = input()
    print("这一局游戏内你希望被称为:")
    user_name = input()
    print("这一局游戏内你希望你领导的的团体被称为:")
    company_name = input()

    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
        file.write(user_name + '\n')
        file.write(company_name + '\n')
    
    
else:
    print(file_names)
