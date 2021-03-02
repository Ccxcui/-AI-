
# coding: utf-8

# In[26]:


import keyboard
from PIL import ImageGrab
import time
from aip import AipOcr


# In[27]:


# 1 截图
keyboard.wait(hotkey='ctrl+c')
time.sleep(0.1)


# In[28]:


# 2 图片保存起来 
image=ImageGrab.grabclipboard()  # 能够从剪切板当中获取图片，并且生成出来
image.save('01.jpg')


# In[29]:


# 3. 识别文字

""" 你的 APPID AK SK """
APP_ID = '23726236'
API_KEY = 'iiW1YVjzqVltDf859AEXh4Dt'
SECRET_KEY = '6GgMFqoBbOOHGCHDDeONHNbrf9zWazGM'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
print(client)


# In[37]:


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('01.jpg')

""" 调用通用文字识别, 图片参数为本地图片 """
text=client.basicGeneral(image)
results=text['words_result']
for i in results:
    print(i['words'])

