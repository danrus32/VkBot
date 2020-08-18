import qrcode
import re
import time
def qrcodegenerate(randomName,peer_id,group_id,user_id,messagetext): 
    print("qr create")
    def ResubQR(messagetext):
        data= re.sub('qr ', "",messagetext)
        return data
    date= ResubQR(messagetext)
    img = qrcode.make(date)  
    img.save("qrmap/"+str(randomName)+'.png')
    time.sleep(3)
