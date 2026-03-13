import glob,keyboard,os,time,sys
def dialog_box(options_list,text):
    max_choice_num = 0
    i = 0
    choice_num = -1
    max_choice_num = len(options_list) - 1
    if max_choice_num+1== 0:
        os.system("cls")
        print(text)
        input()
        return 0
    while True:
        if i == 0:
            os.system("cls")
            print(text)
            for option in range(max_choice_num+1):
                print(options_list[option])
            i = 1
            time.sleep(0.2)
        else:
            if keyboard.is_pressed("up"):
                os.system("cls")
                print(text)
                choice_num -= 1
                if choice_num< 0:
                    choice_num = max_choice_num
                
                for j in range(len(options_list)):
                    if j== choice_num:
                        print(">" + options_list[j])
                    else:
                        print(options_list[j])
                time.sleep(0.15)
                
            elif keyboard.is_pressed("down"):
                os.system("cls")
                print(text)
                choice_num += 1
                if choice_num > max_choice_num:
                    choice_num = 0
                for j in range(max_choice_num + 1):
                    if j == choice_num:
                        print(">" + options_list[j])
                    else:
                        print(options_list[j])
                time.sleep(0.15)
            elif keyboard.is_pressed("enter"):
                if choice_num!= -1:
                    return choice_num
            time.sleep(0.05)
def main_interface():
    txt_files = glob.glob('*.txt')
    dialog_box_list = []
    dialog_box_list.append("新存档")
    for i in range(len(txt_files)):
        dialog_box_list.append("存档"+txt_files[i].split(".")[0])
    archive = dialog_box(dialog_box_list,"\n精灵宝可梦\n        绿宝石\n")
    return archive
def location_cutscenes(text):
    os.system("cls")
    for i in range(os.get_terminal_size().lines):
        if os.get_terminal_size().lines // 2== i+1:
            center = (os.get_terminal_size().columns - len(text)) // 2
            right_padding = os.get_terminal_size().columns - len(text) - center
            print(center*" "+text+right_padding*" ")
        print(" "*os.get_terminal_size().columns)
    time.sleep(0.5)
    os.system("cls")
    
