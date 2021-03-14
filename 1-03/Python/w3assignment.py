# 載入模組
import urllib.request as req 
import json

# 將網址使用json模組讀取
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"

with req.urlopen(url) as response: 
    data=json.load(response)

# 將data內資料更新為只包含景點內容的資料。
data=data["result"]["results"] 

# 建立data.txt，並用寫入模式打開。
with open("data.txt","w",encoding="utf-8") as file: 

#用迴圈讀取data字典中的每個值。
    lines=0 #用lines索引data字典值的位置。迴圈最後lines+=1。
    for line in data: 
#在jpg、JPG、png後面加上","，並用split分個字串變成列表，以便稍後將第一個網址寫入data中。
        data[lines]["file"]=data[lines]["file"].replace("jpg","jpg,")  
        data[lines]["file"]=data[lines]["file"].replace("JPG","JPG,")
        data[lines]["file"]=data[lines]["file"].replace("png","png,")
        data_img=data[lines]["file"].split(",")
# 將對應的資料逐個寫入data
        file.write( 
            data[lines]["stitle"]+","+  # 景點名稱,
            data[lines]["longitude"]+","+ # 經度,
            data[lines]["latitude"]+","+ # 緯度,
            data_img[0]+"\n" # 第一個圖片網址，並換行。
        )
        lines+=1 