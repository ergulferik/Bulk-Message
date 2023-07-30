import pyautogui
import pywhatkit

data = open("numbers.txt", "r", encoding="utf-8")
listData = data.readlines()
number = []
for i in listData:
    tempStr = ""
    for k in range(len(i)):
        if i[k] == ' ':
            continue
        else:
            tempStr += i[k]
    number.append(tempStr)

counter = 0
for i in number:
    try:
        pywhatkit.sendwhatmsg_instantly(i, "KÜLTÜR SANAT TOPLULUĞU\n\nMerhabalar, tiyatro çalışmalarımız her hafta pazartesi saat 16.30 ve çarşamba 17.20 de olacaktır. Çalışmalara spor ayakkabı ve eşofman&tayt ile gelmek zorunludur.\n\nTiyatro odamızı Ceypark AVM'nin önünden nasıl bulabileceğinize dair video: \nhttps://www.instagram.com/p/CVKVZ1Con1z/?utm_source=ig_web_button_share_sheet", 15)

        # pyautogui.press('enter')

        pyautogui.moveTo(1797, 1020)
        pyautogui.click()
        counter += 1
        print(counter, "Tane mesaj gönderildi")
    except:
        print(i, "Numarasında hata var")


