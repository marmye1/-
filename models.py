import pyautogui
import cv2
import time
import os
import numpy as np

pyautogui.FAILSAFE = True

#获取屏幕截图，方便匹配
def take_screen_pic():
    pyautogui.screenshot().save("screen_screenshot/屏幕截图.png")
    screen_pic = cv2.imdecode(np.fromfile("screen_screenshot/屏幕截图.png", dtype=np.uint8), -1)
    return screen_pic

#获取目标截图
def take_target_pic(target_pic_path):
    target_pic=cv2.imdecode(np.fromfile(target_pic_path, dtype=np.uint8), -1)[:,:,:3]
    return target_pic

#截图匹配，确定坐标
def pic_match(target_pic):
    n=0
    while True:
        # 进行目标截图和屏幕截图的匹配
        screen_pic = take_screen_pic()
        result = cv2.matchTemplate(screen_pic, target_pic, cv2.TM_SQDIFF_NORMED)
        #设置阈值
        if cv2.minMaxLoc(result)[0]>0.05:#大于0.01说明匹配失败
            n+=1
            if n>=20:
                print('图片匹配失败')
                return None
        else:
            # 返回匹配区域的左上角坐标
            upper_left = cv2.minMaxLoc(result)[2]
            # 返回匹配区域的右下角坐标
            height, width, tube = target_pic.shape
            lower_right = (upper_left[0] + width, upper_left[1] + height)
            # 计算中心位置坐标
            avg = (int((upper_left[0] + lower_right[0]) / 2), int((upper_left[1] + lower_right[1]) / 2))
            break
    return avg



#获取目标截图顺序列表
def get_target_pic_name_list(true_path):

    target_pic_name_list = [os.path.join(true_path,i) for i in os.listdir(true_path)]
    return target_pic_name_list

#自动点击左键
def auto_click(avg):
    try:
        pyautogui.click(avg[0],avg[1],button='left')
    except :
        raise ValueError("手动停止")



#定义单次单击后的待机时间
def time_sleep(s):
    time.sleep(s)


#单个神经元，即一次匹配、点击、待机
def model_add(target_pic,s=0.8):
    avg = pic_match(target_pic)
    if avg != None:
        auto_click(avg)
        time_sleep(s)
    else:
        raise ValueError("没匹配到")

def model_0(target_pic_name_list):#初始化
    target_pic = take_target_pic(target_pic_name_list[0])
    model_add(target_pic, 1)
    target_pic = take_target_pic(target_pic_name_list[1])
    model_add(target_pic, 0.1)

def model_1(target_pic_name_list):
    print(f'开始匹配{target_pic_name_list[0][54:-4]}')


    target_pic = take_target_pic(target_pic_name_list[2])
    model_add(target_pic, 2)

    target_pic = take_target_pic(target_pic_name_list[3])#开始十连
    model_add(target_pic, 2)
    pyautogui.click(button='left', clicks=50)  # 需要clickshow

    target_pic = take_target_pic(target_pic_name_list[4])#继续十连
    while True:
        try:
            model_add(target_pic, 2)
            pyautogui.click(button='left', clicks=50) # 需要clickshow
        except:
            print('结束')
            target_pic = take_target_pic(target_pic_name_list[5])
            model_add(target_pic, 1)
            model_add(target_pic, 1)
            break



def open_1():
    model_0(get_target_pic_name_list(f"target_screenshot/宝箱"))

    target_pic_name_list=get_target_pic_name_list(f"target_screenshot/宝箱")#目标路径
    model_1(target_pic_name_list)



def model_expore_new():
    target_pic_name_list = get_target_pic_name_list(r"target_screenshot/探索新/")
    target_pic = take_target_pic(target_pic_name_list[0])#新探索，可能要写循环
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[1])#补给
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[2])#快选
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[3])#补充
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[4])#返回
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[5])#出发，可以等一下或者点击跳过
    model_add(target_pic)
    print('等待图标')
    time.sleep(2)
    print('结束等待')

    target_pic = take_target_pic(target_pic_name_list[6])  # 点击加速图标
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[7])  # 全加速
    model_add(target_pic)
    print('等待加速ing')
    time_sleep(12)
    print('结束等待')

    target_pic = take_target_pic(target_pic_name_list[8])  # 跳过加速
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[9])  # 领取
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[10])  # 返回
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[11])  # 确认
    model_add(target_pic)
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[12])  # 强制结束
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[13])  # 确认
    model_add(target_pic)

    target_pic = take_target_pic(target_pic_name_list[14])  # 返回，这之前有个统计结算，可以点击跳过
    time.sleep(1)
    pyautogui.click(button='left', clicks=40)  # 需要clickshow
    model_add(target_pic)

def auto_expore():
    while True:
        model_expore_new()#新探索,#最后需要手动暂停

