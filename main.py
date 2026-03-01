import functions,os,keyboard,time,glob,datetime
os.system("cls")
functions.main_interface(True,0)
txt_files = glob.glob('*.txt')
max_choices = len(txt_files)  
choice_num = 0
name = ""
center = 0
while True:
    if keyboard.is_pressed("up"):
        os.system("cls")
        choice_num -= 1
        if choice_num < 0:
            choice_num = max_choices  
        functions.main_interface(False,choice_num)
        time.sleep(0.15)
    elif keyboard.is_pressed("down"):
        os.system("cls")
        choice_num += 1
        if choice_num > max_choices:
            choice_num = 0 
        functions.main_interface(False,choice_num)
        time.sleep(0.15)
    elif keyboard.is_pressed("enter"):  
        break
    time.sleep(0.05)
os.system("cls")
if choice_num == 0:
    functions.dialog_box(["",0],["",1],["",2],["",3],"你好！让你久等了！（按回车键继续）")
    functions.dialog_box(["",0],["",1],["",2],["",3],"欢迎来到精灵宝可梦的世界！")
    functions.dialog_box(["",0],["",1],["",2],["",3],"我是小田卷。")
    functions.dialog_box(["",0],["",1],["",2],["",3],"人们都称我为\n宝可梦博士。")
    functions.dialog_box(["",0],["",1],["",2],["",3],"这就是被我们称为\n“宝可梦”的生物（掏出精灵球）")
    functions.dialog_box(["",0],["",1],["",2],["",3],"这个世界广泛存在着精灵宝可梦，\n人们也管它们叫宝可梦。")
    functions.dialog_box(["",0],["",1],["",2],["",3],"人们和宝可梦一起玩耍，\n互相帮助，并且成为了好伙伴。")
    functions.dialog_box(["",0],["",1],["",2],["",3],"有时候，我们与它们\n宝可梦一起战斗。")
    functions.dialog_box(["",0],["",1],["",2],["",3],"遗憾的是，我们对它们\n并不是很了解。")
    functions.dialog_box(["",0],["",1],["",2],["",3],"事实上，宝可梦身上\n还有很多很多秘密。")
    functions.dialog_box(["",0],["",1],["",2],["",3],"为了揭开宝可梦的秘密，\n我倾注了毕生心血研究它们。\n来实现我一生中最大的愿望")
    functions.dialog_box(["",0],["",1],["",2],["",3],"那么请问？")
    gender = functions.dialog_box(["男",0],["女",1],["",2],["",3],"你是男孩？还是女孩？")
    while name== "":
        os.system("cls")
        print("那么，请告诉我你的名字吧！")
        name = input()
    functions.dialog_box(["",0],["",1],["",2],["",3],"啊，没错！")
    functions.dialog_box(["",0],["",1],["",2],["",3],"你就是刚搬到\n未白镇来的%s啊。我知道了！"%(name))
    functions.dialog_box(["",0],["",1],["",2],["",3],"好的，准备好了吗？")
    functions.dialog_box(["",0],["",1],["",2],["",3],"振奋人心的冒险即将展开。")
    functions.dialog_box(["",0],["",1],["",2],["",3],"鼓起勇气，迈向宝可梦的世界吧！\n那里孕育着梦想，\n充满着刺激，还会遇到新的朋友！")
    functions.dialog_box(["",0],["",1],["",2],["",3],"当然，我对你充满了期待。\n到我的宝可梦研究所来见我吧。")
    functions.location_cutscenes("未白镇")
    functions.dialog_box(["",0],["",1],["",2],["",3],"妈妈：%s，我们到了，宝贝！"%(name))
    functions.dialog_box(["",0],["",1],["",2],["",3],"跟我们的行李一起挤在车厢里\n很累吧？")
    functions.dialog_box(["",0],["",1],["",2],["",3],"喜欢吗？\n这是我们的新家！")
    functions.dialog_box(["",0],["",1],["",2],["",3],"虽然房子看上去有点老旧，\n但你不觉得住起来应该很舒适吗？")
    functions.dialog_box(["",0],["",1],["",2],["",3],"而且这次也有你自己的房间了，%s！我们先进屋吧。"%(name))
    functions.location_cutscenes("新家 一楼")
    functions.dialog_box(["",0],["",1],["",2],["",3],"妈妈：怎么样，%s？\n这儿不错吧？"%(name))
    functions.dialog_box(["",0],["",1],["",2],["",3],"搬家公司的宝可梦帮我们把东西\n都搬进来，还会帮忙打扫房间。真方便！")
    functions.dialog_box(["",0],["",1],["",2],["",3],"%s，你的房间在楼上，去看看吧，宝贝！"%(name))
    functions.dialog_box(["",0],["",1],["",2],["",3],"爸爸给你买了个钟，\n这样你就能知道时间了。别忘了调钟啊！")
    functions.dialog_box(["",0],["",1],["",2],["",3],"（过动猿在打扫房间）")
    functions.location_cutscenes("新家 二楼")
    functions.dialog_box(["",0],["",1],["",2],["",3],"钟停了，把它调好吧！")
    input("现在是%i点，请你输入当前是几点"%(datetime.now().hour))
    os.system("cls")
    functions.dialog_box(["",0],["",1],["",2],["",3],"妈妈：%s，喜欢你的\n新房间吗？"%(name))
    functions.dialog_box(["",0],["",1],["",2],["",3],"好！房间都清理干净了！")
    functions.dialog_box(["",0],["",1],["",2],["",3],"楼下也\n整理完毕了，")
    functions.dialog_box(["",0],["",1],["",2],["",3],"让宝可梦搬家真方便啊！")
    functions.dialog_box(["",0],["",1],["",2],["",3],"啊，最好是看看你桌子上的东西\n是不是都齐了。")
    functions.dialog_box(["NGC",0],["笔记",1],["",2],["",3],"你在房间里发现了：")
    if choice_num== 0:
        functions.dialog_box(["",0],["",1],["",2],["",3],"这是NGC，")
        functions.dialog_box(["",0],["",1],["",2],["",3],"上面连着个GBR\n当做手柄。")
    elif choice_num== 1:
        functions.dialog_box(["",0],["",1],["",2],["",3],"%s翻开笔记。"%(name))
        functions.dialog_box(["",0],["",1],["",2],["",3],"冒险须知第一条：QWQ")
        functions.dialog_box(["",0],["",1],["",2],["",3],"冒险须知第二条：保存选项可以记录")
        functions.dialog_box(["",0],["",1],["",2],["",3],"后面是空白")
    functions.dialog_box(["去一楼",0],["",1],["",2],["",3],"接下来你要干什么？")



