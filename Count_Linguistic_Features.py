# 在terminal里输入： 
# streamlit run "/Users/qinxu/Visual_Studio_Code/Py_files/Count_Linguistic_Features.py"

#   Local URL: http://localhost:8501
#   Network URL: http://192.168.10.3:8501

import pandas as pd
from glob import glob
from collections import Counter
import re
import math
import natsort
from re import findall
import streamlit as st
from st_aggrid import AgGrid
import base64



st.set_page_config(layout="wide")

######  设置Sidebar的宽度
st.markdown(
     """
     <style>
     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
         width: 250px;
       }
       [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
           width: 200px;
           margin-left: -100px;
        }
        </style>
        """,
        unsafe_allow_html=True)

# 取消警告：You are calling st.pyplot() without any arguments. After December 1st, 2020, we will remove the ability to do this as it requires the use of Matplotlib's global figure object, which is not thread-safe.
st.set_option('deprecation.showPyplotGlobalUse', False)
#st.title("Online Chinese Composition Corpus")
st.title("Frequency Count of 92 Linguistic Features")
st.write("----------------")

### 导入文本
#Path = "/Users/qinxu/Jupyter_work/2022博士论文语料/20220501 高三学和日本学生语料1366/*.txt"
#Path = "/Users/qinxu/Jupyter_work/2022博士论文语料/20220530 高三学生日本学生语料1450重命名/*.txt"
# Path = "/Users/qinxu/Desktop/20220823freq_test/*.txt"
# Filenames = glob(Path)
# Filenames= natsort.natsorted(Filenames)#文件名如果乱序，则需要用到这一行
# len(Filenames)



#获取词单

C01高频名词 = [line.strip() for line in open('词单20220311修改整理版/01.高频名词.txt', 'r', encoding='utf-8').readlines()]
C02中频名词 = [line.strip() for line in open('词单20220311修改整理版/02.中频名词.txt', 'r', encoding='utf-8').readlines()]
C03低频名词 = [line.strip() for line in open('词单20220311修改整理版/03.低频名词.txt', 'r', encoding='utf-8').readlines()]

C12高频动词 = [line.strip() for line in open('词单20220311修改整理版/12.高频动词.txt', 'r', encoding='utf-8').readlines()]
C13中频动词 = [line.strip() for line in open('词单20220311修改整理版/13.中频动词.txt', 'r', encoding='utf-8').readlines()]
C14低频动词 = [line.strip() for line in open('词单20220311修改整理版/14.低频动词.txt', 'r', encoding='utf-8').readlines()]

C25高频形容词 = [line.strip() for line in open('词单20220311修改整理版/25.高频形容词.txt', 'r', encoding='utf-8').readlines()]
C26中频形容词 = [line.strip() for line in open('词单20220311修改整理版/26.中频形容词.txt', 'r', encoding='utf-8').readlines()]
C27低频形容词 = [line.strip() for line in open('词单20220311修改整理版/27.低频形容词.txt', 'r', encoding='utf-8').readlines()]

C42高频副词 = [line.strip() for line in open('词单20220311修改整理版/42.高频副词.txt', 'r', encoding='utf-8').readlines()]
C43中频副词 = [line.strip() for line in open('词单20220311修改整理版/43.中频副词.txt', 'r', encoding='utf-8').readlines()]
C44低频副词 = [line.strip() for line in open('词单20220311修改整理版/44.低频副词.txt', 'r', encoding='utf-8').readlines()]

C04抽象名词 = [line.strip() for line in open('词单20220311修改整理版/04.抽象名词.txt', 'r', encoding='utf-8').readlines()]
C05立场性名词 = [line.strip() for line in open('词单20220311修改整理版/05.立场性名词.txt', 'r', encoding='utf-8').readlines()]
C06心理名词 = [line.strip() for line in open('词单20220311修改整理版/06.心理名词.txt', 'r', encoding='utf-8').readlines()]
C10具象名词 = [line.strip() for line in open('词单20220311修改整理版/10.具象名词.txt', 'r', encoding='utf-8').readlines()]
C11度量衡名词 = [line.strip() for line in open('词单20220311修改整理版/11.度量衡名词.txt', 'r', encoding='utf-8').readlines()]

C15动作行为动词 = [line.strip() for line in open('词单20220311修改整理版/15.动作行为动词.txt', 'r', encoding='utf-8').readlines()]
C16使役动词 = [line.strip() for line in open('词单20220311修改整理版/16.使役动词.txt', 'r', encoding='utf-8').readlines()]
C17存现动词 = [line.strip() for line in open('词单20220311修改整理版/17.存现动词.txt', 'r', encoding='utf-8').readlines()]
C18心理动词 = [line.strip() for line in open('词单20220311修改整理版/18.心理动词.txt', 'r', encoding='utf-8').readlines()]
C20交际动词 = [line.strip() for line in open('词单20220311修改整理版/20.交际动词.txt', 'r', encoding='utf-8').readlines()]
C21推测性动词 = [line.strip() for line in open('词单20220311修改整理版/21.推测性动词.txt', 'r', encoding='utf-8').readlines()]

C28样态形容词 = [line.strip() for line in open('词单20220311修改整理版/28.样态形容词.txt', 'r', encoding='utf-8').readlines()]
C35其他第一人称代词 = [line.strip() for line in open('词单20220311修改整理版/35.其他第一人称代词.txt', 'r', encoding='utf-8').readlines()]

C45必然性副词 = [line.strip() for line in open('词单20220311修改整理版/45.必然性副词.txt', 'r', encoding='utf-8').readlines()]
C46可能性副词 = [line.strip() for line in open('词单20220311修改整理版/46.可能性副词.txt', 'r', encoding='utf-8').readlines()]
C47态度性副词 = [line.strip() for line in open('词单20220311修改整理版/47.态度性副词.txt', 'r', encoding='utf-8').readlines()]

C59嵌偶单音词 = [line.strip() for line in open('词单20220311修改整理版/59.嵌偶单音词.txt', 'r', encoding='utf-8').readlines()]
C60合偶双音词 = [line.strip() for line in open('词单20220311修改整理版/60.合偶双音词.txt', 'r', encoding='utf-8').readlines()]

C08指人名词 = [line.strip() for line in open('词单20220311修改整理版/08.指人名词.txt', 'r', encoding='utf-8').readlines()]

C09集体名词 = [line.strip() for line in open('词单20220311修改整理版/09.集体名词.txt', 'r', encoding='utf-8').readlines()]
C75方位处所词 = [line.strip() for line in open('词单20220311修改整理版/75.方位处所词.txt', 'r', encoding='utf-8').readlines()]
C74时间副词 = [line.strip() for line in open('词单20220311修改整理版/74.时间副词.txt', 'r', encoding='utf-8').readlines()]
C74时间副词 = [line.strip() for line in open('词单20220311修改整理版/74.时间副词.txt', 'r', encoding='utf-8').readlines()]

C07大学学科专业分类词 = [line.strip() for line in open('词单20220311修改整理版/07.大学学科专业分类词.txt', 'r', encoding='utf-8').readlines()]
C19肯定性动词 = [line.strip() for line in open('词单20220311修改整理版/19.肯定性动词.txt', 'r', encoding='utf-8').readlines()]
C61古语词 = [line.strip() for line in open('词单20220311修改整理版/61.古语词.txt', 'r', encoding='utf-8').readlines()]
C76缩略语 = [line.strip() for line in open('词单20220311修改整理版/76.缩略语.txt', 'r', encoding='utf-8').readlines()]
C57口语词词单 = [line.strip() for line in open('词单20220311修改整理版/57.口语词词单.txt', 'r', encoding='utf-8').readlines()]
C80插入语词单 = [line.strip() for line in open('词单20220311修改整理版/80.插入语词单.txt', 'r', encoding='utf-8').readlines()]
C63模糊限制语 = [line.strip() for line in open('词单20220311修改整理版/63.模糊限制语.txt', 'r', encoding='utf-8').readlines()]
C41不定代词 = [line.strip() for line in open('词单20220311修改整理版/41.不定代词.txt', 'r', encoding='utf-8').readlines()]
C77否定词 = [line.strip() for line in open('词单20220311修改整理版/77.否定词.txt', 'r', encoding='utf-8').readlines()]
C62程度副词 = [line.strip() for line in open('词单20220311修改整理版/62.程度副词.txt', 'r', encoding='utf-8').readlines()]

低难度词汇 = [line.strip() for line in open('词单20220311修改整理版/HSK1-2.txt', 'r', encoding='utf-8').readlines()]
中难度词汇 = [line.strip() for line in open('词单20220311修改整理版/HSK3-4.txt', 'r', encoding='utf-8').readlines()]
高难度词汇 = [line.strip() for line in open('词单20220311修改整理版/HSK5-6.txt', 'r', encoding='utf-8').readlines()]
HSK词汇 = [line.strip() for line in open('词单20220311修改整理版/HSK.txt', 'r', encoding='utf-8').readlines()]


st.write('### Upload text file')
st.write('###### The text file should be in UTF-8 format and has been annotated by the NLPIR system. (请上传由NLPIR汉语分词系统进行分词后的TXT文本,TXT格式需为UTF-8。)')
uploaded_file = st.file_uploader("Choose txt files",accept_multiple_files = True,type=['txt'])

# st.markdown("""
# **Note: **Please refer to[**TXT text example**](https://github.com/qinx0606/Count_Linguistic_Features/blob/main/Text_example.txt)，.**
#     """)

with open('Text_example.txt',"r") as f:    #设置对象
    str_example = f.read()
    doc_example = str_example.strip().replace("\ufeff","").replace("\n","\n\n\n").replace("  "," ")
with st.expander('Note: Before uploading, please click here for a text example. The text to be uploaded should be in "UTF-8" format (上传前请点击此处参考TXT分词文本示例。将分词文本保存为编码格式为“UTF-8”的txt文件。)'):
    st.write(doc_example)

# Filenames = uploaded_file
# st.write(Filenames)

### 读取上传的txt文件
if uploaded_file is not None:
    Filename_Contents=[]
    for File_name in uploaded_file:
        Contents = File_name.read().decode("utf-8")
        Filename=str(File_name)
        Filename=Filename.split("name='")[-1]
        Filename=Filename.split("', type=")[0]
        Filename_Contents.append([Filename,Contents])

### 统计语言特征的元素，形成表格  
    dic = {}
    for i in range(0,len(Filename_Contents)):
        text = Filename_Contents[i][[1][0]] ## 第1个列表的第2个元素，内容
        Filename = Filename_Contents[i][[0][0]]## 第i个列表的第1个元素，文本名
        doc = text.strip().replace("\ufeff","").replace("\n","").replace("  "," ") #将文本开头的"\ufeff"替换掉；将换行符\n替换掉 （有时将"/"替换为_,不然"/"会被识别为空格）   
        
        #2.将文本单词以空格进行切分
        Wordlst = doc.split()  #doc.split(" ")
        
        wordlst = [token.split("/")[0] for token in Wordlst]  # 将上一步读取的含标点的文本，去掉标注。
        
        #3在上一步的基础上，去掉标点符号
        Wordlist = [token for token in Wordlst if token.split("/")[-1] not in ["w", "wkz", "wky" , "wyz" , "wyy", "wj", "ww",  "wt",  "wd", "wf", "wn", "wm", "ws",  "wp",  "wb", "wh","x"]]
        wordlist = [token.split("/")[0] for token in Wordlist]  #将上一步读取的不含标点的文本，去掉标注。
        
        # 去除人名
    #         Wordlist_去除人名 = [token for token in Wordlst if token.split("/")[-1] not in ["w", "wkz", "wky" , "wyz" , "wyy", "wj", "ww",  "wt",  "wd", "wf", "wn", "wm", "ws",  "wp",  "wb", "wh","x","nr","nr1","nr2","nrj","nrf"]]
    #         wordlist_去除人名 = [token.split("/")[0] for token in Wordlist_去除人名]  #将上一步读取的不含标点的文本，去掉标注。        
        
        #4.统计文本中的字数
        file = "".join(wordlst).replace("\n","")           #将去掉标注的文本，去掉回车符和空格，变为有标点的纯本文;  
        file_no标点 = "".join(wordlist).replace("\n","")    #去掉标注的文本，去掉回车符和空格和标点，变为无标点的纯本文。
        #file_no标点和人名 = "".join(wordlist_去除人名).replace("\n","")
        
        字数含标点 = len(file)                               #文本长度含标点
        字数不含标点 = len(file_no标点)                       #文本长度不含标点

        #5.统计每个文本中的 形符"总词数Tokens"和 类符 "異なり語数Types"
        形符_Tokens= len(wordlist)  # 统计某文本的Tokens，不含标点
        类符_Types= len(set(wordlist)) # 统计某文本的Types，不含标点


        
        #6.统计每个文本中的总句数和所有标点符号数
        总句数= [token for token in Wordlst if re.search("/wj|/ww|/wt|/ws",token)]
        总句数=len(总句数)
        所有标点 = [token for token in Wordlst if token.split("/")[-1] in ["w", "wkz", "wky" , "wyz" , "wyy", "wj", "ww",  "wt",  "wd", "wf", "wn", "wm", "ws",  "wp",  "wb", "wh"]]
        w所有标点=len(所有标点)
        
        C89_词汇多样性 = 类符_Types/math.sqrt(形符_Tokens)     
        C91_平均词长 = 字数不含标点/形符_Tokens     
        C92_平均句长_字数 = 字数不含标点/总句数      
        C92_平均句长_词数 = 形符_Tokens/总句数 
        
        实词tokens数 = len([token for token in Wordlist if re.search("/n|/t|/s|/f|/v|/a|/z|/b|/m|/q|/d|/r|/o|/e|/k|/h",token)])
        虚词tokens数 = len([token for token in Wordlist if re.search("/p|/c|/u|/y",token)])
        C90_词汇密度 = 实词tokens数/形符_Tokens
        
        
        
        C70_低难度词汇 = len([token for token in wordlist if token in 低难度词汇])
        C71_中难度词汇 = len([token for token in wordlist if token in 中难度词汇])
        C72_高难度词汇 = len([token for token in wordlist if token in 高难度词汇])  
        C73_非HSK词汇 = len([token for token in wordlist if token not in HSK词汇]) 
        #C73_非HSK词汇_去除人名 = len([token for token in wordlist_去除人名 if token not in HSK词汇]) 
        
    ########1.名词类    
        名词tokens = [token for token in Wordlist if re.search("/n|/t|/s|/f|/vn|/an",token)]#"/n|t|vn|an|s|f"
        名词token = [token.split("/")[0] for token in 名词tokens]
        C01_高频名词 = len([token for token in 名词token if token in C01高频名词])
        C02_中频名词 = len([token for token in 名词token if token in C02中频名词])
        C03_低频名词 = len([token for token in 名词token if token in C03低频名词])
        C04_抽象名词 = len([token for token in 名词token if token in C04抽象名词])
        C05_具象名词 = len([token for token in 名词token if token in C10具象名词])
        C06_心理名词 = len([token for token in 名词token if token in C06心理名词])        
        
        
    #统计指人名词名词："家|师|人|者|员|长|生|姐|兄|弟|妹|亲|客|夫|孩|童" 和 "C08指人名词"词单，有一部分重合            
        指人名词tokens = [token for token in Wordlist if re.search("/n",token)]
        指人名词tokens = [token for token in 指人名词tokens if token.split("/")[-1] not in ['nt','ntz','ntqg','nttqg','ntsc']]
        指人名词tokens = [token.split("/")[0] for token in 指人名词tokens]
        指人名词11 = [token for token in 指人名词tokens if re.search("家|师|人|者|员|长|生|姐|兄|弟|妹|亲|客|夫|孩|童",token)] #检索某种词性中含有某个字的词语，模糊检索，只要词中含有这个词就行
        指人名词2 = [token for token in 名词token if token not in 指人名词11]
        指人名词22 = [token for token in 指人名词2 if token in C08指人名词]
        C07_指人名词 = len(指人名词11+指人名词22)        
        
    #统计集体名词：nt和词单，有一部分重合
        集体名词1 = [token for token in Wordlist if re.search("/nt",token)]
        集体名词11 = [token.split("/")[0] for token in 集体名词1]        
        集体名词2 = [token for token in 名词token if token not in 集体名词11]
        集体名词22 = [token for token in 集体名词2 if token in C09集体名词]
        C08_集体名词 = len(集体名词11+集体名词22)
        
        #普通名词复数型       
        普通名词复数型 = [token for token in Wordlst if token.split("/")[-1] not in ["rr"]]
        非人称代词tokens = [token.split("/")[0] for token in 普通名词复数型]                   
        C09_普通名词复数型 =len([token for token in 非人称代词tokens if re.search("们",token)])    #名词+们的统计：直接在去掉人称代词（如，我们）后统计“们”的个数即可。        
        C10_名词化功能词 = len([token for token in Wordlist if token.split("/")[-1] in ["vn", "an"]])

    ########2.动词类       
        动词tokens = [token for token in Wordlist if re.search("/v",token)]
        动词token1 = [token for token in 动词tokens if token.split("/")[-1] not in ['vd','vn']]
        动词token = [token.split("/")[0] for token in 动词token1]
        C11_高频动词 = len([token for token in 动词token if token in C12高频动词])
        C12_中频动词 = len([token for token in 动词token if token in C13中频动词])
        C13_低频动词 = len([token for token in 动词token if token in C14低频动词]) 
        C14_动作行为动词 = len([token for token in 动词token if token in C15动作行为动词])
        C15_心理动词 = len([token for token in 动词token if token in C18心理动词])
        
        C17_交际动词 = len([token for token in 动词token if token in C20交际动词]) 
        C18_推测性动词 = len([token for token in 动词token if token in C21推测性动词])
        
        C19趋向动词 = len([token for token in Wordlist if token.split("/")[-1] in ["vf"]])
        C20副动词 = len([token for token in Wordlist if token.split("/")[-1] in ["vd"]])
        C21形式动词 = len([token for token in Wordlist if token.split("/")[-1] in ["vx"]])
        C22系词 = len([token for token in Wordlist if token.split("/")[-1] in ["vshi"]])
        #肯定性动词检索：“C19肯定性动词” 词单 + “辨认出|意思是”
        C16_肯定性动词1 = [token for token in 动词token if token in C19肯定性动词]
        肯定性动词='辨认出|意思是'
        肯定性动词2=[]
        for i in re.finditer(肯定性动词,file):
            #print(i.group()+str(i.span()))
            n=i.group()
            肯定性动词2.append(n)
        C16_肯定性动词=len(C16_肯定性动词1+肯定性动词2)
        C16_肯定性动词1=C16_肯定性动词1+肯定性动词2
        
    ########3.形容词类       
        形容词tokens = [token for token in Wordlist if re.search("/a|/z|/b",token)]
        形容词token1 = [token for token in 形容词tokens if token.split("/")[-1] not in ['ad','an']]
        形容词token = [token.split("/")[0] for token in 形容词token1]
        C23_高频形容词 = len([token for token in 形容词token if token in C25高频形容词])
        C24_中频形容词 = len([token for token in 形容词token if token in C26中频形容词])
        C25_低频形容词 = len([token for token in 形容词token if token in C27低频形容词])  
        C26_性质形容词 = len([token for token in Wordlist if re.search("/a",token)])
        C27_状态形容词 = len([token for token in Wordlist if token.split("/")[-1] in ["z"]])
        C28_区别词 = len([token for token in Wordlist if token.split("/")[-1] in ["b"]])
        
        
    ########4.副词类      
        副词tokens = [token for token in Wordlist if re.search("/d|/ad|/vd",token)]
        副词token = [token.split("/")[0] for token in 副词tokens]
        C29_高频副词 = len([token for token in 副词token if token in C42高频副词])
        C30_中频副词 = len([token for token in 副词token if token in C43中频副词])
        C31_低频副词 = len([token for token in 副词token if token in C44低频副词])       
        C32_必然性副词 = len([token for token in 副词token if token in C45必然性副词]) 
        C33_可能性副词 = len([token for token in 副词token if token in C46可能性副词]) 
        C34_态度性副词 = len([token for token in 副词token if token in C47态度性副词])     
        C35_否定词 = len([token for token in 副词token if token in C77否定词])
        C36_时间副词 = len([token for token in 副词token if token in C74时间副词])
        
        
        ##C36_程度副词 检索，“C62程度副词” 词单+“深深|极力|更甚|至为|透顶|绝顶|大大|全然|极大”
        C37_程度副词1 = [token for token in 副词token if token in C62程度副词]     
        程度副词="深深|极力|更甚|至为|透顶|绝顶|大大|全然|极大"
        程度副词2=[]
        for i in re.finditer(程度副词,file):
            #print(i.group()+str(i.span()))
            n=i.group()
            程度副词2.append(n)
        C37_程度副词=len(C37_程度副词1+程度副词2)
        #C37_程度副词11=C37_程度副词1+程度副词2
        
            
    ########5.代词类
        人称代词tokens = [token for token in Wordlist if re.search("/r",token)]
        人称代词token = [token.split("/")[0] for token in 人称代词tokens]
        
        我_freq= [token for token in wordlist if token in ["我"]]#精确匹配
        C38第一人称单数代词我=len(我_freq)
        我们_freq= [token for token in wordlist if token in ["我们"]]#精确匹配      
        C39第一人称复数代词我们=len(我们_freq)        
        第二人称代词_freq= [token for token in wordlist if token in ["你",'您',"你们","您们"]]#精确匹配      
        C41第二人称代词=len(第二人称代词_freq)        
        第三人称代词_freq= [token for token in wordlist if token in ["他",'她',"他们","她们"]]#精确匹配      
        C42第三人称代词=len(第三人称代词_freq)
        
        无生性代词_freq= [token for token in wordlist if token in ["它",'它们']]#精确匹配      
        C43无生性代词=len(无生性代词_freq) 
        
        C44指示代词 = len([token for token in Wordlist if token.split("/")[-1] in ["rz"]])        
        C46疑问代词 = len([token for token in Wordlist if token.split("/")[-1] in ["ry","rys","ryv","ryt"]]) #或[token for token in Wordlist if re.search("/ry",token)]
        
        #其他第一人称代词
        人称代词tokens1 = [token for token in Wordlist if re.search("/rr",token)]
        人称代词tokens = [token.split("/")[0] for token in 人称代词tokens1]
        C40_其他第一人称代词 = len([token for token in 人称代词tokens if token in C35其他第一人称代词])

    ##C44不定代词,在含标点的纯文本file中检索
        不定代词词单="|".join(C41不定代词) #.replace("\n","")
        不定代词=[]
        for i in re.finditer(不定代词词单,file):
            #print(i.group()+str(i.span()))
            t=i.group()
            不定代词.append(t)  
        C45_不定代词=len(不定代词) 

    ########6.数量词  
        C47数词 = len([token for token in Wordlist if token.split("/")[-1] in ["m","mq"]])
        C48量词 = len([token for token in Wordlist if token.split("/")[-1] in ["q","qv","qt"]]) #或[token for token in Wordlist if re.search("/q",token)]


    #统计方位处所词：处所词s，方位词f，加 “C75方位处所词”词单（副词：如，到处、处处、随处、四处、遍地）
        方位处所词sf = [token for token in Wordlist if token.split("/")[-1] in ["s","f"]]
        方位处所词sf = [token.split("/")[0] for token in 方位处所词sf]
        副词性方位处所词 = [token for token in 副词token if token in C75方位处所词]
        C49_方位处所词 = len(方位处所词sf+副词性方位处所词)     
        
        C50叹词 = len([token for token in Wordlist if token.split("/")[-1] in ["e"]])
        C51拟声词 = len([token for token in Wordlist if token.split("/")[-1] in ["o"]])
        
        
    ########8.统计助词 
        C52词缀领属_的 = len([token for token in Wordlist if token in ["的/ude1"]])
        C53副词化功能词_地 = len([token for token in Wordlist if token in ["地/ude2"]])
        C54结果补语词_得 = len([token for token in Wordlist if token in ["得/ude3"]])
        C55模拟语助词_等_等等 = len([token for token in Wordlist if token in ["等/udeng", "等等/udeng"]])

        #时态助词
        C56进行式时貌词_着 = len([token for token in Wordlist if token in ["着/uzhe"]])
        C57过去式时貌词_了 = len([token for token in Wordlist if token in ["了/ule"]])
        C58过去完成式时貌词_过 = len([token for token in Wordlist if token in ["过/uguo"]])
        C59比况助词 = len([token for token in Wordlist if token.split("/")[-1] in ["uyy"]])

    ########9.其他词类 
        ##.统计介词
        C60介词 = len([token for token in Wordlist if token.split("/")[-1] in ["p"]]) 
        C61连词 = len([token for token in Wordlist if token.split("/")[-1] in ["cc","c"]])
        #C57句内并列连词 = len([token for token in Wordlist if token.split("/")[-1] in ["cc"]])        
        C62语气词 = len([token for token in Wordlist if token.split("/")[-1] in ["y"]])      

        
    ########“嵌偶单音词”和“合偶双音词”
    # 检索“嵌偶单音词”和“合偶双音词”时，应去掉 /nt,/nz,/nr,ns相关的词，否则，如中国、外语系、大阪大学、英语、日语。人名等词汇也会进入嵌偶单音词检索结果
        Wordlist_嵌偶合偶词 = [token for token in Wordlist if token.split("/")[-1] not in ["nr","nr1","nr2","nrj","nrf","nt","ns","nsf","nz"]]
        wordlist_嵌偶合偶词 = [token.split("/")[0] for token in Wordlist_嵌偶合偶词]  #将上一步读取的不含标点的文本，去掉标注。                
        C67_嵌偶单音词 = len([token for token in wordlist_嵌偶合偶词 if re.search(str(C59嵌偶单音词),token)]) #检索“嵌偶单音词”，把词单作为字符串，进行模糊检索，只要词汇中含有字符串的字就行           
        C68_合偶双音词 = len([token for token in wordlist_嵌偶合偶词 if token in C60合偶双音词])  #检索“合偶双音词”
        #C67_合偶双音词1 = [token for token in wordlist if token in C60合偶双音词]  #检索“合偶双音词”

    ##C62口语词词单,在含标点的纯文本file中检索
        口语词词单="|".join(C57口语词词单) #.replace("\n","")
        口语词=[]
        for i in re.finditer(口语词词单,file):
            #print(i.group()+str(i.span()))
            t=i.group()
            口语词.append(t)  
        C63_口语词词单=len(口语词)  

    ##C80插入语词单,在含标点的纯文本file中检索
        插入语词单="|".join(C80插入语词单) #.replace("\n","")
        插入语=[]
        for i in re.finditer(插入语词单,file):
            #print(i.group()+str(i.span()))
            t=i.group()
            插入语.append(t)  
        C64_插入语词单=len(插入语)         

    ##C76缩略语,在含标点的纯文本file中检索
        缩略语词单="|".join(C76缩略语) #.replace("\n","")
        缩略语=[]
        for i in re.finditer(缩略语词单,file):
            #print(i.group()+str(i.span()))
            t=i.group()
            缩略语.append(t)  
        C65_缩略语=len(缩略语)           

    ##C65模糊限制语,在含标点的纯文本file中检索
        模糊限制语词单="|".join(C63模糊限制语) #.replace("\n","")
        模糊限制语=[]
        for i in re.finditer(模糊限制语词单,file):
            #print(i.group()+str(i.span()))
            t=i.group()
            模糊限制语.append(t)  
        C66_模糊限制语=len(模糊限制语)

        
        ##C61古语词,在含标点的纯文本file中检索
        古语词词单="|".join(C61古语词) #.replace("\n","")
        古语词=[]
        for i in re.finditer(古语词词单,file):
            #print(i.group()+str(i.span()))
            t=i.group()
            古语词.append(t)  
        C69_古语词=len(古语词)          

    ########10.句式       
        C74介词_把 = len([token for token in Wordlist if token.split("/")[-1] in ["pba"]])    


    ##### 形成表格

        dic[Filename] = C89_词汇多样性,C90_词汇密度,C91_平均词长,C92_平均句长_字数,C92_平均句长_词数,字数含标点,字数不含标点, 形符_Tokens,类符_Types,总句数,w所有标点,C01_高频名词,C02_中频名词,C03_低频名词,C04_抽象名词,C05_具象名词,C06_心理名词,C07_指人名词,C08_集体名词,C09_普通名词复数型,C10_名词化功能词,C11_高频动词,C12_中频动词,C13_低频动词,C14_动作行为动词,C15_心理动词,C16_肯定性动词,C17_交际动词,C18_推测性动词,C19趋向动词,C20副动词, C21形式动词,C22系词,C23_高频形容词,C24_中频形容词,C25_低频形容词,C26_性质形容词,C27_状态形容词,C28_区别词,C29_高频副词,C30_中频副词,C31_低频副词,C32_必然性副词,C33_可能性副词,C34_态度性副词,C35_否定词,C36_时间副词,C37_程度副词,C38第一人称单数代词我,C39第一人称复数代词我们,C40_其他第一人称代词,C41第二人称代词,C42第三人称代词,C43无生性代词,C44指示代词,C45_不定代词,C46疑问代词,C47数词,C48量词,C49_方位处所词,C50叹词,C51拟声词,C52词缀领属_的,C53副词化功能词_地,C54结果补语词_得,C55模拟语助词_等_等等,C56进行式时貌词_着,C57过去式时貌词_了,C58过去完成式时貌词_过,C59比况助词,C60介词,C61连词,C62语气词,C63_口语词词单, C64_插入语词单,C65_缩略语,C66_模糊限制语, C67_嵌偶单音词,C68_合偶双音词, C69_古语词,C70_低难度词汇,C71_中难度词汇,C72_高难度词汇,C73_非HSK词汇,C74介词_把
    #df = pd.DataFrame(dic,index=["字数"])
    df = pd.DataFrame(dic,['89.词汇多样性','90.词汇密度','91.平均词长',"92.平均句长_字数","92.平均句长_词数","字数含标点","字数无标点","形符_Tokens","类符_Types", '总句数','所有标点数','01.高频名词','02.中频名词','03.低频名词','04.抽象名词','05.具象名词','06.心理名词','07.指人名词','08.集体名词','09.普通名词复数型','10.名词化功能词','11.高频动词','12.中频动词','13.低频动词','14.动作行为动词','15.心理动词','16.肯定性动词','17.交际动词','18.推测性动词','19.趋向动词','20.副动词','21.形式动词','22.系词','23.高频形容词','24.中频形容词','25.低频形容词','26.性质形容词','27.状态形容词','28.区别词','29.高频副词','30.中频副词','31.低频副词','32.必然性副词','33.可能性副词','34.态度性副词','35.否定词','36.时间副词','37.程度副词','38.第一人称单数代词我','39.第一人称复数代词我们','40.其他第一人称代词','41.第二人称代词','42.第三人称代词','43.无生性代词','44.指示代词','45.不定代词','46.疑问代词','47.数词','48.量词','49.方位处所词','50.叹词','51.拟声词','52.词缀领属_的','53.副词化功能词_地','54.结果补语词_得','55.模拟语助词_等_等等','56.进行式时貌词_着','57.过去式时貌词_了','58.过去完成式时貌词_过', '59.比况助词','60.介词','61.连词', '62.语气词','63.口语词','64.插入语','65.缩略语','66.模糊限制语','67.嵌偶单音词','68.合偶双音词', '69.古语词','70.低难度词汇','71.中难度词汇','72.高难度词汇','73.非HSK词汇','74.把字句'])

    df.columns = [columns.split("/")[-1] for columns in df.columns]

    # 统计每种检索式的总频度sum
    freq_sum = df.apply(lambda x : x.sum(), axis=1) #axis=0,按列相加；axis=1，按行相加 
    df["sum_s"]=freq_sum 

    df = df.T
    #df




#   ##### 统计重叠式
#     dic = {}
#     for i in range(0,len(Filename_Contents)):
#         text = Filename_Contents[i][[1][0]]
#         Filename = Filename_Contents[i][[0][0]]
#         doc = text.strip().replace("\ufeff","").replace("\n","").replace("  "," ")

#         #2.将文本单词以空格进行切分
#         Wordlst = doc.split()  #doc.split(" ")
        
#         wordlst = [token.split("/")[0] for token in Wordlst]  # 将上一步读取的含标点的文本，去掉标注。
        
#         #3在上一步的基础上，去掉标点符号
#         Wordlist = [token for token in Wordlst if token.split("/")[-1] not in ["w", "wkz", "wky" , "wyz" , "wyy", "wj", "ww",  "wt",  "wd", "wf", "wn", "wm", "ws",  "wp",  "wb", "wh"]]
#         wordlist = [token.split("/")[0] for token in Wordlist]  #将上一步读取的不含标点的文本，去掉标注。
        
#         #4.统计文本中的字数
#         file = "".join(wordlst).replace("\n","")           #将去掉标注的文本，去掉回车符和空格，变为有标点的纯本文;  
#         file_no标点 = "".join(wordlist).replace("\n","")    #去掉标注的文本，去掉回车符和空格和标点，变为无标点的纯本文。
#         字数含标点 = len(file)                               #文本长度含标点
#         字数不含标点 = len(file_no标点)                       #文本长度不含标点    
        
#         wordlist重叠式= [token for token in Wordlist if token.split("/")[-1] not in ["nt","nms", "t","m","mq","c","nz","x","nr","nrj","nrf","nr1","nr2","ns","nsf"]]
#         wordlist重叠式= [token.split("/")[0] for token in wordlist重叠式]

#     ## ## ## 特殊形式的四字成语：在不含标点、去掉标注的分词列表中检索
#     ## 1.AABB式（高高兴兴、慌慌张张、祖祖辈辈）: pattern = r'((.)\2(.)\3)'
#         patternAABB式 = r'((.)\2(.)\3)'
#         AABB式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternAABB式,x):
#                 t=i.group()
#                 AABB式.append(t)  
#         AABB式频度=len(AABB式) 

#     ## 2.AABC式（念念不忘、多多益善、惴惴不安）: pattern = r'((.)\2..)'
#         patternAABC式 = r'((.)\2..)'
#         AABC式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternAABC式,x):
#                 n = i.group()
#                 AABC式.append(n)
#         AABC式 = [x for x in AABC式 if x not in AABB式] #去掉ABCC词语中的AABB类词语
#         AABC式频度 = len(AABC式)

#     ## 3.ABAB式（彼此彼此、意思意思、恭喜恭喜）: pattern = r'((.)(.)\2\3)'
#         patternABAB式 = r'((.)(.)\2\3)'
#         ABAB式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABAB式,x):
#                 n = i.group()
#                 ABAB式.append(n)
#         ABAB式频度 = len(ABAB式)


#     ## 4.ABAC式（百发百中、自由自在、十全十美、一生一世）: pattern = r'((.).\2.)'
#         patternABAC式 = r'((.).\2.)'
#         ABAC式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABAC式,x):
#                 n = i.group()
#                 ABAC式.append(n)
#         ABAC式频度 = len(ABAC式)

#     ## 5.ABBA式（一二二一）: pattern = r'((.)(.)\3\2)'
#         patternABBA式 = r'((.)(.)\3\2)'
#         ABBA式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABBA式,x):
#                 n = i.group()
#                 ABBA式.append(n)
#         ABBA式频度 = len(ABBA式)

#     ##  6.ABCA式（天外有天、数不胜数、话里有话）: pattern = r'((.)..\2)'
#         patternABCA式 = r'((.)..\2)'
#         ABCA式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABCA式,x):
#                 n = i.group()
#                 ABCA式.append(n)
#         ABCA式频度 = len(ABCA式)

#     ##  7.ABBC式（不了了之、自欺欺人、以风风人）: pattern = r'(.(.)\2.)'
#         patternABBC式 = r'(.(.)\2.)'
#         ABBC式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABBC式,x):
#                 n = i.group()
#                 ABBC式.append(n)
#         ABBC式频度 = len(ABBC式)

#     # 8.ABCB式（将心比心、出尔反尔、人云亦云）: pattern = r'(.(.).\2)'
#         patternABCB式 = r'(.(.).\2)'
#         ABCB式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABCB式,x):
#                 n = i.group()
#                 ABCB式.append(n)
#         ABCB式频度 = len(ABCB式)

#     # 9.ABCC式（议论纷纷、人才济济、小心翼翼）: pattern = r'(..(.)\2)'
#         patternABCC式 = r'(..(.)\2)'
#         ABCC式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABCC式,x):
#                 n = i.group()
#                 ABCC式.append(n)
#         ABCC式 = [x for x in ABCC式 if x not in AABB式] #去掉ABCC词语中的AABB类词语
#         ABCC式频度 = len(ABCC式)
#     # 10.ABCD式（热火朝天、五花八门、一言为定）: pattern = r'(....)'
#         patternABCD式 = r'(....)'
#         ABCD式=[]
#         for x in wordlist重叠式:
#             for i in re.finditer(patternABCD式,x):
#                 n = i.group()
#                 ABCD式.append(n)
                
#         特殊重叠式4字词语=AABB式+AABC式+ABAB式+ABAC式+ABBA式+ABCA式+ABBC式+ABCB式+ABCC式
#         ABCD式 = [x for x in ABCD式 if x not in 特殊重叠式4字词语]
#         ABCD式频度 = len(ABCD式)      
        
#         特殊重叠式4字词语_频度 = len(特殊重叠式4字词语)
#         dic[Filename] = AABB式,AABB式频度,AABC式,AABC式频度,ABAB式,ABAB式频度,ABAC式,ABAC式频度,ABBA式,ABBA式频度,ABCA式,ABCA式频度,ABBC式,ABBC式频度,ABCB式,ABCB式频度,ABCC式,ABCC式频度,ABCD式,ABCD式频度,特殊重叠式4字词语_频度
            
#     df重叠式 = pd.DataFrame(dic,["AABB式","AABB式频度","AABC式","AABC式频度",'ABAB式','ABAB式频度',"ABAC式","ABAC式频度","ABBA式",'ABBA式频度',"ABCA式","ABCA式频度",'ABBC式','ABBC式频度',"ABCB式","ABCB式频度","ABCC式","ABCC式频度","ABCD式","ABCD式频度","特殊重叠式4字词语_频度"])
                        
#     df重叠式.columns = [columns.split("/")[-1] for columns in df重叠式.columns]

#     # 统计每种检索式的总频度sum
#     freq_sum = df重叠式.apply(lambda x : x.sum(), axis=1) #axis=0,按列相加；axis=1，按行相加 
#     df重叠式["sum_s"]=freq_sum 

#     df重叠式 = df重叠式.T
#     #df重叠式.to_csv("/Users/qinxu/Jupyter_work/2022博士论文语料/运行结果/20220605_df重叠式.csv")
#     #df重叠式      


    ##### 统计把字句，被字句，复句等
    dic = {}
    for i in range(0,len(Filename_Contents)):
        text = Filename_Contents[i][[1][0]]
        Filename = Filename_Contents[i][[0][0]]
        doc = text.strip().replace("\ufeff","").replace("\n","").replace("  "," ")


    ########检索被动句、无施事者被动句、进行式句式、过去式句式
        #2.将doc文本以完整小句进行切分  "。/wj|？/ww|！/wt|……/ws|，/wd｜；/wf"
        小句= re.split('wj|ww|wt|ws|wd|wf',doc) #以句号、问号、感叹号、省略号、逗号、分号对句子进行切分
        
        小句带标注有空格=[]
        for i in 小句:
            ki = i.split()
            #qii=[token.split("/")[0] for token in qi] #去掉标注
            kiii= (" ".join(ki))
            小句带标注有空格.append(kiii) 
            
            
    ## C75_被动句式:检索
    ## C75_被动句式:检索
    #(1)pbei
        pbei=".*被/pbei.*|被/pbei.*"
        被pbei字句=[]
        for x in 小句带标注有空格:
            for i in re.finditer(pbei,x):
            #print(i.group()+str(i.span()))
                n = i.group()
                被pbei字句.append(n)
        被字句 = len(被pbei字句)        
    #      #(2)"由/p"+n|rr|s
        由nrr=".*由/p ./n.*|由/p ./n.*|.*由/p ../n.*|由/p ../n.*|.*由/p .../n.*|由/p .../n.*|.*由/p ..../n.*|由/p ..../n.*|.*由/p ./r.*|由/p ./r.*|.*由/p ../r.*|由/p ../r.*|.*由/p ../s.*|由/p ../s.*"
        由_nrr=[]
        for x in 小句带标注有空格:
            for i in re.finditer(由nrr,x):
                n = i.group()
                由_nrr.append(n)
        由 = len(由_nrr) 
        
    #      #(3)为n所v|为rr所v
        为n_r所v=".* 为/v ./n 所/.*|.* 为/v ../n 所/.*|.* 为/v ./n. 所/.*|.* 为/v ../n. 所/.*|.* 为/v ../rr 所/.*|.* 为/p ./n 所/.*|.* 为/p ../n 所/.*|.* 为/p ./n. 所/.*|.* 为/p ../n. 所/.*|.* 为/p ../rr 所/.*"
        为n_r_所v=[]
        for x in 小句带标注有空格:
            for i in re.finditer(为n_r所v,x):
                n = i.group()
                为n_r_所v.append(n)
        为_所 = len(为n_r_所v) 

    # #      #(4)教|让|叫|给+n_r+v: 容易和“教我做人”等重复，故省略
        #教让叫给_nr_v=".* 教/v .*/n.* .*/v.* .*|.* 让/.* .*/n.* .*/v.* .*|.* 叫/.* .*/n.* .*/v.* .*|.* 让/.* .*/n.* .*/v.* .*|.* 教/v .*/r.* .*/v.* .*|.* 让/.* .*/r.* .*/v.* .*|.* 叫/.* .*/r.* .*/v.* .*|.* 让/.* .*/r.* .*/v.* .*"       
    #         教让叫给nr_v=[]
    #         for x in 小句带标注有空格:
    #             for i in re.finditer(教让叫给_nr_v,x):
    #                 n = i.group()
    #                 教让叫给nr_v.append(n)
    #         教让叫给nrv = len(教让叫给nr_v)

        C75_被动句式句子= 被pbei字句+由_nrr+为n_r_所v
        C75_被动句式= 被字句+由+为_所                  

        
    ## C76_无施事者被动句:n|r+被｜挨｜遭｜受｜获|承｜蒙+v
        #无施事者被动动词=".* 被/pbei ./v.*|.* 被/pbei ../v.*|.* 被/pbei .../v.*|.* 被/pbei ..../v.*|.* 挨/v ./v.*|.* 挨/v ../v.*|.* 挨/v .../v.*|.* 遭/v ./v.*|.* 遭/v ../v.*|.* 遭/v .../v.*|.* 遭遇/v ./v.*|.* 遭遇/v ../v.*|.* 遭遇/v .../v.*|.* 遇/v ./v.*|.* 遇/v ../v.*|.* 遇/v .../v.*|.* 受/v ./v.*|.* 受/v ../v.*|.* 受/v .../v.*|.* 获/v ./v.*|.* 获/v ../v.*|.* 获/v .../v.*|.* 承/v ./v.*|.* 承/v ../v.*|.* 承/v .../v.*|.* 蒙/v ./v.*|.* 蒙/v ../v.*|.* 蒙/v .../v.*|.* 蒙受/v ./v.*|.* 蒙受/v ../v.*|.* 蒙受/v .../v.*|.* 受/v 了/ule ./v.*|.* 受/v 了/ule ../v.*|.* 受/v 了/ule .../v.*|.* 受/v 了/ule ./a.*|.* 受/v 了/ule ../a.*|.* 受/v 了/ule .../a.*|.* 被/pbei ./d ./v.*|.* 被/pbei ./d ../v.*|.* 被/pbei .../v.*|.* 被/pbei ./d ..../v.*|.* 挨/v ./d ./v.*|.* 挨/v ./d ../v.*|.* 挨/v .../v.*|.* 遭/v ./d ./v.*|.* 遭/v ./d ../v.*|.* 遭/v .../v.*|.* 遭遇/v ./d ./v.*|.* 遭遇/v ./d ../v.*|.* 遭遇/v .../v.*|.* 遇/v ./d ./v.*|.* 遇/v ./d ../v.*|.* 遇/v .../v.*|.* 受/v ./d ./v.*|.* 受/v ./d ../v.*|.* 受/v .../v.*|.* 获/v ./d ./v.*|.* 获/v ./d ../v.*|.* 获/v .../v.*|.* 承/v ./d ./v.*|.* 承/v ./d ../v.*|.* 承/v .../v.*|.* 蒙/v ./d ./v.*|.* 蒙/v ./d ../v.*|.* 蒙/v .../v.*|.* 蒙受/v ./d ./v.*|.* 蒙受/v ./d ../v.*|.* 蒙受/v .../v.*|.* 受/v 了/ule ./d ./v.*|.* 受/v 了/ule ./d ../v.*|.* 受/v 了/ule .../v.*|.* 被/pbei ../d ./v.*|.* 被/pbei ../d ../v.*|.* 被/pbei .../v.*|.* 被/pbei ../d ..../v.*|.* 挨/v ../d ./v.*|.* 挨/v ../d ../v.*|.* 挨/v .../v.*|.* 遭/v ../d ./v.*|.* 遭/v ../d ../v.*|.* 遭/v .../v.*|.* 遭遇/v ../d ./v.*|.* 遭遇/v ../d ../v.*|.* 遭遇/v .../v.*|.* 遇/v ../d ./v.*|.* 遇/v ../d ../v.*|.* 遇/v .../v.*|.* 受/v ../d ./v.*|.* 受/v ../d ../v.*|.* 受/v .../v.*|.* 获/v ../d ./v.*|.* 获/v ../d ../v.*|.* 获/v .../v.*|.* 承/v ../d ./v.*|.* 承/v ../d ../v.*|.* 承/v .../v.*|.* 蒙/v ../d ./v.*|.* 蒙/v ../d ../v.*|.* 蒙/v .../v.*|.* 蒙受/v ../d ./v.*|.* 蒙受/v ../d ../v.*|.* 蒙受/v .../v.*|.* 受/v 了/ule ../d ./v.*|.* 受/v 了/ule ../d ../v.*|.* 受/v 了/ule .../v.*|.* 被/pbei .../d ./v.*|.* 被/pbei .../d ../v.*|.* 被/pbei .../v.*|.* 被/pbei .../d ..../v.*|.* 挨/v .../d ./v.*|.* 挨/v .../d ../v.*|.* 挨/v .../v.*|.* 遭/v .../d ./v.*|.* 遭/v .../d ../v.*|.* 遭/v .../v.*|.* 遭遇/v .../d ./v.*|.* 遭遇/v .../d ../v.*|.* 遭遇/v .../v.*|.* 遇/v .../d ./v.*|.* 遇/v .../d ../v.*|.* 遇/v .../v.*|.* 受/v .../d ./v.*|.* 受/v .../d ../v.*|.* 受/v .../v.*|.* 获/v .../d ./v.*|.* 获/v .../d ../v.*|.* 获/v .../v.*|.* 承/v .../d ./v.*|.* 承/v .../d ../v.*|.* 承/v .../v.*|.* 蒙/v .../d ./v.*|.* 蒙/v .../d ../v.*|.* 蒙/v .../v.*|.* 蒙受/v .../d ./v.*|.* 蒙受/v .../d ../v.*|.* 蒙受/v .../v.*|.* 受/v 了/ule .../d ./v.*|.* 受/v 了/ule .../d ../v.*|.* 受/v 了/ule .../v.*"
        无施事者被动动词=".*被/pbei ./v.*|.*被/pbei ../v.*|.*被/pbei .../v.*|.*被/pbei ..../v.*|.*被/pbei ./d ./v.*|.*被/pbei ../d ./v.*|.*被/pbei ./d ../v.*|.*被/pbei ../d ../v.*|.*被/pbei ../d 的/ude1../v.*|.*被/pbei ../d 地/ude2../v.*|.*被/pbei .../d ./v.*|.*被/pbei .../d ../v.*|.*被/pbei ../a 地/ude2 ../v.*|.*挨/v ./v.*|.*遭/v ./v.*|.*遭/v ../v.*|.* 受/v ./v.*|.* 受/v ../v.*"
        C76_无施事者被动句句子=[]
        for x in 小句带标注有空格:
            for i in re.finditer(无施事者被动动词,x):
                n = i.group()
                C76_无施事者被动句句子.append(n)
        C76_无施事者被动句 = len(C76_无施事者被动句句子)  

            
            
        ## C78_进行式句式:V+(n)+中， V+(n)+着，V+(n)+来着，正/在/正在+V，V+时，当/正当+V+时，V+之时，V+的时候，V+（n）+呢、
        ###   ".*/v.* 中/.* .*" : V+(n)+中，正/在/正在+V+(n)+中
        ###   ".*/v.* 来着/.*|.*/v.* 着/.*" : V+(n)+着，正/在/正在+V+(n)+着，V+(n)+来着，正/在/正在+V+(n)+来着
        ###   ".*/v.* 的/ude1 时候/.*|.*/v.* 之/uzhi 时/.*|.*/v.* 时/.*" : V+(n)+时，V+(n)+之时，V+(n)+的时候    
        进行式句式组合=".*/v.* 中/.*|.*/v.* 来着/.*|.*/v.* 着/.*|.*/v.* 的/ude1 时候/.*|.*/v.* 之/uzhi 时/.*|.*/v.* 时/.*|.*/v.* 呢/.*"
        C78进行式句式句子=[]
        for x in 小句带标注有空格:
            for i in re.finditer(进行式句式组合,x):
                n = i.group()
                C78进行式句式句子.append(n)
        C78_进行式句式= len(C78进行式句式句子)    

        
        #C77过去时貌词检索："已经","曾经","已","曾","刚刚","刚才","刚","方才"+v
        过去时貌词组合=".* 已经/.* .*/v.*|.* 曾经/.* .*/v.*|.* 已/.* .*/v.*|.* 曾/.* .*/v.*|.* 刚刚/.* .*/v.*|.* 刚才/.* .*/v.*|.* 刚/.* .*/v.*|.* 才/.* .*/v.*|.* 方才/.* .*/v.*"
        C77_过去时貌词句子=[]
        for x in 小句带标注有空格:
            for i in re.finditer(过去时貌词组合,x):
                n = i.group()
                C77_过去时貌词句子.append(n)
        C77_过去时貌词= len(C77_过去时貌词句子)  
            
            
    ########检索10类副句               
    #将doc文本以完整句子进行切分  "。/wj|？/ww|！/wt|……/ws"
        完整句子= re.split('wj|ww|wt|ws',doc) #以完整句子进行切分
        句子去标注去空格=[]
        for i in 完整句子:
            wi = i.split()
            wii=[token.split("/")[0] for token in wi] #去掉标注
            wiii= ("".join(wii))
            句子去标注去空格.append(wiii) 
        
        句子去标注有空格=[]
        for i in 完整句子:
            qi = i.split()
            qii=[token.split("/")[0] for token in qi] #去掉标注
            qiii= (" ".join(qii))
            句子去标注有空格.append(qiii) 
            
        #C79并列复句_合用：《现代汉语》增订六版下册p129-p130
        #C79并列复句关联词=".* 既 .* 又 .*|.* 既 .* 也 .*|.* 又 .* 又 .*|.* 也 .* 也 .*|.* 又 .* 也 .*|.* 也 .* 又 .*|.* 有时 .* 有时 .*|.* 一方面 .* 一方面 .*|.* 一方面 .* 另一方面 .*|.* 一方面 .* 又一方面 .*|.* 一边 .* 一边 .*|.* 一会儿 .* 一会儿 .*|.* 不是 .* 而是 .*|.* 并非 .* 而是 .*|.* 是 .* 不是 .*|.* ，同时 .*|.* ，同样 .*|.* ，另外 .*|.* ，也 .*|.* ，又 .*|.* ，而是 .*|.* ，而 .*|.* ；同时 .*|.* ；同样 .*|.* ；另外 .*|.* ；也 .*|.* ；又 .*|.* ；而是 .*|.* ；而 .*|.* ， .* 同时 .*|.* ， .* 同样 .*|.* ， .* 另外 .*|.* ， .* 也 .*|.* ， .* 又 .*|.* ， .* 而是 .*|.* ， .* 而 .*|.* ； .* 同时 .*|.* ； .* 同样 .*|.* ； .* 另外 .*|.* ； .* 也 .*|.* ； .* 又 .*|.* ； .* 而是 .*|.* ； .* 而 .*"
        #在上一步基础上删去单用的: “也”、“又”、“而”
        C79并列复句关联词=".*既 .*又 .*|.*既 .* 也 .*|.*又 .*又 .*|.*也 .* 也 .*|.*又 .* 也 .*|.*也 .*又 .*|.*有时.*有时.*|.*一方面.*一方面.*|.*一边.* 一边.*|.*一会儿.* 一会儿.*|.*不是 .* 而是 .*|.*并非 .* 而是.*|.*是 .* 不是 .*|.*，.* 同时 .*|.*，.* 同样 .*|.*，.* 另外 .*|.*，.* 而是 .*|.*；.* 同时 .*|.*；.* 同样 .*|.*；.* 另外 .*|.*；.* 而是 .*|.*,.* 同时 .*|.*,.* 同样 .*|.*,.* 另外 .*|.*,.* 而是 .*|.*;.* 同时 .*|.*;.* 同样 .*|.*;.* 另外 .*|.*;.* 而是 .*"      
        C79_并列复句=[]
        for x in 句子去标注有空格:
            for i in re.finditer(C79并列复句关联词,x):
            #print(i.group()+str(i.span()))
                n=i.group()
                C79_并列复句.append(n)
        C79并列复句=len(C79_并列复句)

        #C80顺承复句_合用：《现代汉语》增订六版下册p130
        #C80顺承复句关联词=".* 首先 .* 然后 .*|.* 首先 .* 后来 .*|.* 首先 .* 随后 .*|.* 首先 .* 再 .*|.* 首先 .* 又 .*|.* 起先 .* 然后 .*|.* 起先 .* 后来 .*|.* 起先 .* 随后 .*|.* 起先 .* 再 .*|.* 起先 .* 又 .*|.* 先 .* 然后 .*|.* 先 .* 后来 .*|.* 先 .* 随后 .*|.* 先 .* 再 .*|.* 先 .* 又 .*|.* 刚 .* 就 .*|.* 一 .* 就 .*|.* ， .* 便 .*|.* ， .* 又 .*|.* ， .* 再 .*|.* ， .* 于是 .*|.* ， .* 然后 .*|.* ， .* 后来 .*|.* ， .* 接着 .*|.* ， .* 跟着 .*|.* ， .* 继而 .*|.* ， .* 终于 .*|.* ； .* 便 .*|.* ； .* 又 .*|.* ； .* 再 .*|.* ； .* 于是 .*|.* ； .* 然后 .*|.* ； .* 后来 .*|.* ； .* 接着 .*|.* ； .* 跟着 .*|.* ； .* 继而 .*|.* ； .* 终于 .*|.* ，便 .*|.* ，又 .*|.* ，再 .*|.* ，于是 .*|.* ，然后 .*|.* ，后来 .*|.* ，接着 .*|.* ，跟着 .*|.* ，继而 .*|.* ，终于 .*|.* ；便 .*|.* ；又 .*|.* ；再 .*|.* ；于是 .*|.* ；然后 .*|.* ；后来 .*|.* ；接着 .*|.* ；跟着 .*|.* ；继而 .*|.* ；终于 .*"
        #在上一步基础上删去单用的: “便”、“就”、“又”、“再”
        C80顺承复句关联词=".*首先 .* 然后 .*|.*首先 .* 后来 .*|.*首先 .* 随后 .*|.*首先 .* 再 .*|.*首先 .* 又 .*|.*起先 .* 然后 .*|.*起先 .* 后来 .*|.*起先 .* 随后 .*|.*起先 .* 再 .*|.*起先 .* 又 .*|.*先 .* 然后 .*|.*先 .* 后来 .*|.*先 .* 随后 .*|.*先 .* 再 .*|.*先 .* 又 .*|.*刚 .* 就 .*|.*一 .* 就 .*|.*，.* 于是 .*|.*，.* 然后 .*|.*，.* 后来 .*|.*，.* 接着 .*|.*，.* 跟着 .*|.*，.* 继而 .*|.*，.* 终于 .*|.*；.* 于是 .*|.*；.* 然后 .*|.*；.* 后来 .*|.*；.* 接着 .*|.*；.* 跟着 .*|.*；.* 继而 .*|.*；.* 终于 .*|.*，于是 .*|.*，然后 .*|.*，后来 .*|.*，接着 .*|.*，跟着 .*|.*，继而 .*|.*，终于 .*|.*；于是 .*|.*；然后 .*|.*；后来 .*|.*；接着 .*|.*；跟着 .*|.*；继而 .*|.*；终于 .*|.*,.* 于是 .*|.*,.* 然后 .*|.*,.* 后来 .*|.*,.* 接着 .*|.*,.* 跟着 .*|.*,.* 继而 .*|.*,.* 终于 .*|.*;.* 于是 .*|.*;.* 然后 .*|.*;.* 后来 .*|.*;.* 接着 .*|.*;.* 跟着 .*|.*;.* 继而 .*|.*;.* 终于 .*|.*,于是 .*|.*,然后 .*|.*,后来 .*|.*,接着 .*|.*,跟着 .*|.*,继而 .*|.*,终于 .*|.*;于是 .*|.*;然后 .*|.*;后来 .*|.*;接着 .*|.*;跟着 .*|.*;继而 .*|.*;终于 .*"
        C80_顺承复句=[]
        for x in 句子去标注有空格:
            for i in re.finditer(C80顺承复句关联词,x):
            #print(i.group()+str(i.span()))
                n=i.group()
                C80_顺承复句.append(n)
        C80顺承复句=len(C80_顺承复句)

        #C81解说复句：《现代汉语》增订六版下册p131，解说复句
        C81解说复句关联词=".* 即 .*|.*就是 说 .*|.* 就 是 说 .*|.*就是说.*|.*；.*；.*|.*;.*;.*"
        C81_解说复句=[]
        for x in 句子去标注有空格:
            for i in re.finditer(C81解说复句关联词,x):
            #print(i.group()+str(i.span()))
                n=i.group()
                C81_解说复句.append(n)
        C81解说复句=len(C81_解说复句)


        #C82选择复句：《现代汉语》增订六版下册p132，选择复句
        #C82选择复句关联词=".* 或者 .* 或者 .*|.* 或者 .* 或 .*|.* 或者 .* 或是 .*|.* 或 .* 或者 .*|.* 或 .* 或 .*|.* 或 .* 或是 .*|.* 或是 .* 或者 .*|.* 或是 .* 或 .*|.* 或是 .* 或是 .*|.* 是 .* 还是 .*|.* 不是 .* 就是 .*|.* 要么 .* 要么 .*|.* 要不 .* 要不 .*|.* 与其 .* 不如 .*|.* 与其 .* 毋宁 .*|.* 与其 .* 宁肯 .*|.* 与其 .* 倒不如 .*|.* 与其 .* 倒 不如 .*|.* 与其 .* 还不如 .*|.* 与其 .* 还 不如 .*|.* 宁可 .* 也不 .*|.* 宁可 .* 决不 .*|.* 宁可 .* 不 .*|.* 宁 .* 也不 .*|.* 宁 .* 决不 .*|.* 宁 .* 不 .*|.* 宁肯 .* 也不 .*|.* 宁肯 .* 决不 .*|.* 宁肯 .* 不 .*|.* 宁愿 .* 也不 .*|.* 宁愿 .* 决不 .*|.* 宁愿 .* 不 .*|.* ， 倒不如 .*|.* ， 倒 不如 .*|.* ； 倒不如 .*|.* ； 倒 不如 .*|.* ， 还不如 .*|.* ， 还 不如 .*|.* ； 还不如 .*|.* ； 还 不如 .*|.* ， 或者 .*|.* ， 或是 .*|.* ， 或 .*|.* ， 还是 .*|.* ； 或者 .*|.* ； 或是 .*|.* ； 或 .*|.* ； 还是 .*|.* ， .* 倒不如 .*|.* ， .* 倒 不如 .*|.* ； .*  倒不如 .*|.* ； .*  倒 不如 .*|.* ， .* 还不如 .*|.* ， .* 还 不如 .*|.* ； .*  还不如 .*|.* ； .*  还 不如 .*|.* ， .* 或者 .*|.* ， .* 或是 .*|.* ， .* 或 .*|.* ， .* 还是 .*|.* ； .*  或者 .*|.* ； .*  或是 .*|.* ； .*  或 .*|.* ； .*  还是 .*"
        C82选择复句关联词=".*或者 .* 或者 .*|.*或许 .* 或许 .*|.*或者 .* 或 .*|.*或者 .* 或是 .*|.*或 .* 或者 .*|.*或 .* 或 .*|.*或 .* 或是 .*|.*或是 .* 或者 .*|.*或是 .* 或 .*|.*或是 .* 或是 .*|.*是 .* 还是 .*|.*不是 .* 就是 .*|.*要么 .* 要么 .*|.*要不 .* 要不 .*|.*与其 .* 不如 .*|.*与其 .* 毋宁 .*|.*与其 .* 宁肯 .*|.*与其 .* 倒不如 .*|.*与其 .* 倒 不如 .*|.*与其 .* 还不如 .*|.*与其 .* 还 不如 .*|.*宁可 .* 也不 .*|.*宁可 .* 决不 .*|.*宁可 .* 不 .*|.*宁 .* 也不 .*|.*宁 .* 决不 .*|.*宁 .* 不 .*|.*宁肯 .* 也不 .*|.*宁肯 .* 决不 .*|.*宁肯 .* 不 .*|.*宁愿 .* 也不 .*|.*宁愿 .* 决不 .*|.*宁愿 .* 不 .*|.*，.* 倒不如 .*|.*，.* 倒 不如 .*|.*；.* 倒不如 .*|.*；.* 倒 不如 .*|.*，.* 还不如 .*|.*，.* 还 不如 .*|.*；.* 还不如 .*|.*；.* 还 不如 .*|.*，.* 或者 .*|.*，.* 或是 .*|.*，.* 或 .*|.*，.* 还是 .*|.*；.* 或者 .*|.*；.* 或是 .*|.*；.* 或 .*|.*；.* 还是 .*|.*，.* 倒不如 .*|.*，.* 倒 不如 .*|.*；.* 倒不如 .*|.*；.* 倒 不如 .*|.*，.* 还不如 .*|.*，.* 还 不如 .*|.*；.* 还不如 .*|.*；.* 还 不如 .*|.*，.* 或者 .*|.*，.* 或是 .*|.*，.* 或 .*|.*，.* 还是 .*|.*；.* 或者 .*|.*；.* 或是 .*|.*；.* 或 .*|.*；.* 还是 .*| .*,.* 倒不如 .*|.*,.* 倒 不如 .*|.*;.* 倒不如 .*|.*;.* 倒 不如 .*|.*,.* 还不如 .*|.*,.* 还 不如 .*|.*;.* 还不如 .*|.*;.* 还 不如 .*|.*,.* 或者 .*|.*,.* 或是 .*|.*,.* 或 .*|.*,.* 还是 .*|.*;.* 或者 .*|.*;.* 或是 .*|.*;.* 或 .*|.*;.* 还是 .*|.*,.* 倒不如 .*|.*,.* 倒 不如 .*|.*;.* 倒不如 .*|.*;.* 倒 不如 .*|.*,.* 还不如 .*|.*,.* 还 不如 .*|.*;.* 还不如 .*|.*;.* 还 不如 .*|.*,.* 或者 .*|.*,.* 或是 .*|.*,.* 或 .*|.*,.* 还是 .*|.*;.* 或者 .*|.*;.* 或是 .*|.*;.* 或 .*|.*;.* 还是 .*"
        
        C82_选择复句=[]
        for x in 句子去标注有空格:
            for i in re.finditer(C82选择复句关联词,x):
            #print(i.group()+str(i.span()))
                n=i.group()
                C82_选择复句.append(n)
        C82选择复句=len(C82_选择复句)

        #C83递进复句：《现代汉语》增订六版下册p133，递进复句
        #C83递进复句关联词=".* 不但 .* 而且 .*|.* 不但 .* 还 .*|.* 不但 .* 也 .*|.* 不但 .* 又 .*|.* 不但 .* 更 .*|.* 不仅 .* 而且 .*|.* 不仅 .* 还 .*|.* 不仅 .* 也 .*|.* 不仅 .* 又 .*|.* 不仅 .* 更 .*|.* 不只 .* 而且 .*|.* 不只 .* 还 .*|.* 不只 .* 也 .*|.* 不只 .* 又 .*|.* 不只 .* 更 .*|.* 不光 .* 而且 .*|.* 不光 .* 还 .*|.* 不光 .* 也 .*|.* 不光 .* 又 .*|.* 不光 .* 更 .*|.* 非但 .* 而且 .*|.* 非但 .* 还 .*|.* 非但 .* 也 .*|.* 非但 .* 又 .*|.* 非但 .* 更 .*|.* 不但不 .* 反而 .*|.* 不但 不 .* 反而 .*|.* 尚且 .* 何况 .*|.* 尚且 .* 还 .*|.* 尚且 .* 更不用说 .*|.* 尚且 .* 更 不用说 .*|.* 尚且 .* 更 不用 说 .*|.* 尚且 .* 更 不 用 说 .*|.* 尚且 .* 更不 用说 .*|.* 尚且 .* 更不 用 说 .*|.* 别说 .* 连 .* 也 .*|.* 别说 .* 连 .* 都 .*|.* 别说 .* 就是 .* 也 .*|.* 别说 .* 就是 .* 都 .*|.* 慢说 .* 连 .* 也 .*|.* 慢说 .* 连 .* 都 .*|.* 慢说 .* 就是 .* 也 .*|.* 慢说 .* 就是 .* 都 .*|.* 别 说 .* 连 .* 也 .*|.* 别 说 .* 连 .* 都 .*|.* 别 说 .* 就是 .* 也 .*|.* 别 说 .* 就是 .* 都 .*|.* 慢 说 .* 连 .* 也 .*|.* 慢 说 .* 连 .* 都 .*|.* 慢 说 .* 就是 .* 也 .*|.* 慢 说 .* 就是 .* 都 .*|.* 不要说 .* 连 .* 也 .*|.* 不要说 .* 连 .* 都 .*|.* 不要说 .* 就是 .* 也 .*|.* 不要说 .* 就是 .* 都 .*|.* 不要 说 .* 连 .* 也 .*|.* 不要 说 .* 连 .* 都 .*|.* 不要 说 .* 就是 .* 也 .*|.* 不要 说 .* 就是 .* 都 .*|.* ， 而且 .*|.* ， 并且 .*|.* ， 况且 .*|.* ， 甚至 .*|.* ， 以至 .*|.* ， 更 .*|.* ， 还 .*|.* ， 甚至于 .*|.* ， 甚至 于 .*|.* ， 尚且 .*|.* ， 何况 .*|.* ， 反而 .*|.* ； 而且 .*|.* ； 并且 .*|.* ； 况且 .*|.* ； 甚至 .*|.* ； 以至 .*|.* ； 更 .*|.* ； 还 .*|.* ； 甚至于 .*|.* ； 甚至 于 .*|.* ； 尚且 .*|.* ； 何况 .*|.* ； 反而 .*| .* ， .* 而且 .*|.* ， .* 并且 .*|.* ， .* 况且 .*|.* ， .* 甚至 .*|.* ， .* 以至 .*|.* ， .* 更 .*|.* ， .* 还 .*|.* ， .* 甚至于 .*|.* ， .* 甚至 于 .*|.* ， .* 尚且 .*|.* ， .* 何况 .*|.* ， .* 反而 .*|.* ， .* 而且 .*|.* ， .* 并且 .*|.* ， .* 况且 .*|.* ， .* 甚至 .*|.* ， .* 以至 .*|.* ， .* 更 .*|.* ， .* 还 .*|.* ， .* 甚至于 .*|.* ， .* 甚至 于 .*|.* ， .* 尚且 .*|.* ， .* 何况 .*|.* ， .* 反而 .*"
        #在上一步基础上删去单用的: “更”、“还”、“以至”
        #C83递进复句关联词=".* 不但 .* 而且 .*|.* 不但 .* 还 .*|.* 不但 .* 也 .*|.* 不但 .* 又 .*|.* 不但 .* 更 .*|.* 不仅 .* 而且 .*|.* 不仅 .* 还 .*|.* 不仅 .* 也 .*|.* 不仅 .* 又 .*|.* 不仅 .* 更 .*|.* 不只 .* 而且 .*|.* 不只 .* 还 .*|.* 不只 .* 也 .*|.* 不只 .* 又 .*|.* 不只 .* 更 .*|.* 不光 .* 而且 .*|.* 不光 .* 还 .*|.* 不光 .* 也 .*|.* 不光 .* 又 .*|.* 不光 .* 更 .*|.* 非但 .* 而且 .*|.* 非但 .* 还 .*|.* 非但 .* 也 .*|.* 非但 .* 又 .*|.* 非但 .* 更 .*|.* 不但不 .* 反而 .*|.* 不但 不 .* 反而 .*|.* 尚且 .* 何况 .*|.* 尚且 .* 还 .*|.* 尚且 .* 更不用说 .*|.* 尚且 .* 更 不用说 .*|.* 尚且 .* 更 不用 说 .*|.* 尚且 .* 更 不 用 说 .*|.* 尚且 .* 更不 用说 .*|.* 尚且 .* 更不 用 说 .*|.* 别说 .* 连 .* 也 .*|.* 别说 .* 连 .* 都 .*|.* 别说 .* 就是 .* 也 .*|.* 别说 .* 就是 .* 都 .*|.* 慢说 .* 连 .* 也 .*|.* 慢说 .* 连 .* 都 .*|.* 慢说 .* 就是 .* 也 .*|.* 慢说 .* 就是 .* 都 .*|.* 别 说 .* 连 .* 也 .*|.* 别 说 .* 连 .* 都 .*|.* 别 说 .* 就是 .* 也 .*|.* 别 说 .* 就是 .* 都 .*|.* 慢 说 .* 连 .* 也 .*|.* 慢 说 .* 连 .* 都 .*|.* 慢 说 .* 就是 .* 也 .*|.* 慢 说 .* 就是 .* 都 .*|.* 不要说 .* 连 .* 也 .*|.* 不要说 .* 连 .* 都 .*|.* 不要说 .* 就是 .* 也 .*|.* 不要说 .* 就是 .* 都 .*|.* 不要 说 .* 连 .* 也 .*|.* 不要 说 .* 连 .* 都 .*|.* 不要 说 .* 就是 .* 也 .*|.* 不要 说 .* 就是 .* 都 .*|.* ， 而且 .*|.* ， 并且 .*|.* ， 况且 .*|.* ， 甚至 .*|.* ， 以至 .*|.* ， 更 .*|.* ， 还 .*|.* ， 甚至于 .*|.* ， 甚至 于 .*|.* ， 尚且 .*|.* ， 何况 .*|.* ， 反而 .*|.* ； 而且 .*|.* ； 并且 .*|.* ； 况且 .*|.* ； 甚至 .*|.* ； 甚至于 .*|.* ； 甚至 于 .*|.* ； 尚且 .*|.* ； 何况 .*|.* ； 反而 .*| .* ， .* 而且 .*|.* ， .* 并且 .*|.* ， .* 况且 .*|.* ， .* 甚至 .*|.* ， .* 甚至于 .*|.* ， .* 甚至 于 .*|.* ， .* 尚且 .*|.* ， .* 何况 .*|.* ， .* 反而 .*|.* ， .* 而且 .*|.* ， .* 并且 .*|.* ， .* 况且 .*|.* ， .* 甚至 .*|.* ， .* 甚至于 .*|.* ， .* 甚至 于 .*|.* ， .* 尚且 .*|.* ， .* 何况 .*|.* ， .* 反而 .*"
        C83递进复句关联词=".*不但 .* 而且 .*|.*不但 .* 还 .*|.*不但 .* 也 .*|.*不但 .* 又 .*|.*不但 .* 更 .*|.*不仅 .* 而且 .*|.*不仅 .* 还 .*|.*不仅 .* 也 .*|.*不仅 .* 又 .*|.*不仅 .* 更 .*|.*不只 .* 而且 .*|.*不只 .* 还 .*|.*不只 .* 也 .*|.*不只 .* 又 .*|.*不只 .* 更 .*|.*不光 .* 而且 .*|.*不光 .* 还 .*|.*不光 .* 也 .*|.*不光 .* 又 .*|.*不光 .* 更 .*|.*非但 .* 而且 .*|.*非但 .* 还 .*|.*非但 .* 也 .*|.*非但 .* 又 .*|.*非但 .* 更 .*|.*不但不 .* 反而 .*|.*不但 不 .* 反而 .*|.*尚且 .* 何况 .*|.*尚且 .* 还 .*|.*尚且 .* 更不用说 .*|.*尚且 .* 更 不用说 .*|.*尚且 .* 更 不用 说 .*|.*尚且 .* 更 不 用 说 .*|.*尚且 .* 更不 用说 .*|.*尚且 .* 更不 用 说 .*|.*别说 .* 连 .* 也 .*|.*别说 .* 连 .* 都 .*|.*别说 .* 就是 .* 也 .*|.*别说 .* 就是 .* 都 .*|.*慢说 .* 连 .* 也 .*|.*慢说 .* 连 .* 都 .*|.*慢说 .* 就是 .* 也 .*|.*慢说 .* 就是 .* 都 .*|.*别 说 .* 连 .* 也 .*|.*别 说 .* 连 .* 都 .*|.*别 说 .* 就是 .* 也 .*|.*别 说 .* 就是 .* 都 .*|.*慢 说 .* 连 .* 也 .*|.*慢 说 .* 连 .* 都 .*|.*慢 说 .* 就是 .* 也 .*|.*慢 说 .* 就是 .* 都 .*|.*不要说 .* 连 .* 也 .*|.*不要说 .* 连 .* 都 .*|.*不要说 .* 就是 .* 也 .*|.*不要说 .* 就是 .* 都 .*|.*不要 说 .* 连 .* 也 .*|.*不要 说 .* 连 .* 都 .*|.*不要 说 .* 就是 .* 也 .*|.*不要 说 .* 就是 .* 都 .*|.*，.* 而且 .*|.*，.* 并且 .*|.*，.* 况且 .*|.*，.* 以至 .*|.*，.* 甚至 .*|.*，.* 甚至于 .*|.*，.* 甚至 于 .*|.*，.* 尚且 .*|.*，.* 何况 .*|.*，.* 反而 .*|.*；.* 而且 .*|.*；.* 并且 .*|.*；.* 况且 .*|.*；.* 以至 .*|.*；.* 甚至 .*|.*；.* 甚至于 .*|.*；.* 甚至 于 .*|.*；.* 尚且 .*|.*；.* 何况 .*|.*；.* 反而 .*|.*,.* 而且 .*|.*,.* 并且 .*|.*,.* 况且 .*|.*,.* 以至 .*|.*,.* 甚至 .*|.*,.* 甚至于 .*|.*,.* 甚至 于 .*|.*,.* 尚且 .*|.*,.* 何况 .*|.*,.* 反而 .*|.*;.* 而且 .*|.*;.* 并且 .*|.*;.* 况且 .*|.*;.* 以至 .*|.*;.* 甚至 .*|.*;.* 甚至于 .*|.*;.* 甚至 于 .*|.*;.* 尚且 .*|.*;.* 何况 .*|.*;.* 反而 .*|.*， 而且 .*|.*， 并且 .*|.*， 况且 .*|.*， 以至 .*|.*， 甚至 .*|.*， 以至 .*|.*， 更 .*|.*， 还 .*|.*， 甚至于 .*|.*， 甚至 于 .*|.*， 尚且 .*|.*， 何况 .*|.*， 反而 .*|.*； 而且 .*|.*； 并且 .*|.*； 况且 .*|.*； 以至 .*|.*； 甚至 .*|.*； 甚至于 .*|.*； 甚至 于 .*|.*； 尚且 .*|.*； 何况 .*|.*； 反而 .*| .*, 而且 .*|.*, 并且 .*|.*, 况且 .*|.*, 以至 .*|.*, 甚至 .*|.*, 以至 .*|.*, 更 .*|.*, 还 .*|.*, 甚至于 .*|.*, 甚至 于 .*|.*, 尚且 .*|.*, 何况 .*|.*, 反而 .*|.*; 而且 .*|.*; 并且 .*|.*; 况且 .*|.*; 以至 .*|.*; 甚至 .*|.*; 甚至于 .*|.*; 甚至 于 .*|.*; 尚且 .*|.*; 何况 .*|.*; 反而 .*"
        C83_递进复句=[]
        for x in 句子去标注有空格:
            for i in re.finditer(C83递进复句关联词,x):
            #print(i.group()+str(i.span()))
                n = i.group()
                C83_递进复句.append(n)
        C83递进复句 = len(C83_递进复句)

        #C84条件复句：《现代汉语》增订六版下册p134，条件复句:合用如“只要……就……”，检索式为 “.* 只要 .* 就 .*”；单用，如“便”，检索式“.* ， 便 .*|.* ； 便 .*|.* ， .* 便 .*|.* ； .* 便 .*"
        #C84条件复句关联词 = ".* 只要 .* 就 .*|.* 只要 .* 都 .*|.* 只要 .* 便 .*|.* 只要 .* 总 .*|.* 只需 .* 就 .*|.* 只需 .* 都 .*|.* 只需 .* 便 .*|.* 只需 .* 总 .*|.* 一旦 .* 就 .*|.* 一旦 .* 都 .*|.* 一旦 .* 便 .*|.* 一旦 .* 总 .*|.* 只有 .* 才 .*|.* 只有 .* 否则 .*|.* 只有 .* 不 .*|.* 唯有 .* 才 .*|.* 唯有 .* 否则 .*|.* 唯有 .* 不 .*|.* 除非 .* 才 .*|.* 除非 .* 否则 .*|.* 除非 .* 不 .*|.* 无论 .* 都 .*|.* 无论 .* 总是 .*|.* 无论 .* 总 .*|.* 无论 .* 还 .*|.* 无论 .* 也 .*|.* 不论 .* 都 .*|.* 不论 .* 总是 .*|.* 不论 .* 总 .*|.* 不论 .* 还 .*|.* 不论 .* 也 .*|.* 不管 .* 都 .*|.* 不管 .* 总是 .*|.* 不管 .* 总 .*|.* 不管 .* 还 .*|.* 不管 .* 也 .*|.* 任凭 .* 都 .*|.* 任凭 .* 总是 .*|.* 任凭 .* 总 .*|.* 任凭 .* 还 .*|.* 任凭 .* 也 .*|.* 任 .* 都 .*|.* 任 .* 总是 .*|.* 任 .* 总 .*|.* 任 .* 还 .*|.* 任 .* 也 .*|.* ， 便 .*|.* ， 就 .*|.* ， 才 .*|.* ， 要不然 .*|.* ， 要 不然 .*|.* ， 要 不 然 .*|.* ； 便 .*|.* ； 就 .*|.* ； 才 .*|.* ； 要不然 .*|.* ； 要 不然 .*|.* ； 要 不 然 .*|.* ， .* 便 .*|.* ， .* 就 .*|.* ， .* 才 .*|.* ， .* 要不然 .*|.* ， .* 要 不然 .*|.* ， .* 要 不 然 .*|.* ； .* 便 .*|.* ； .* 就 .*|.* ； .* 才 .*|.* ； .* 要不然 .*|.* ； .* 要 不然 .*|.* ； .* 要 不 然 .*"
        #在上一步基础上删去单用的: “便”、“就”、“才”
        #C84条件复句关联词 = ".* 只要 .* 就 .*|.* 只要 .* 都 .*|.* 只要 .* 便 .*|.* 只要 .* 总 .*|.* 只需 .* 就 .*|.* 只需 .* 都 .*|.* 只需 .* 便 .*|.* 只需 .* 总 .*|.* 一旦 .* 就 .*|.* 一旦 .* 都 .*|.* 一旦 .* 便 .*|.* 一旦 .* 总 .*|.* 只有 .* 才 .*|.* 只有 .* 否则 .*|.* 只有 .* 不 .*|.* 唯有 .* 才 .*|.* 唯有 .* 否则 .*|.* 唯有 .* 不 .*|.* 除非 .* 才 .*|.* 除非 .* 否则 .*|.* 除非 .* 不 .*|.* 无论 .* 都 .*|.* 无论 .* 总是 .*|.* 无论 .* 总 .*|.* 无论 .* 还 .*|.* 无论 .* 也 .*|.* 不论 .* 都 .*|.* 不论 .* 总是 .*|.* 不论 .* 总 .*|.* 不论 .* 还 .*|.* 不论 .* 也 .*|.* 不管 .* 都 .*|.* 不管 .* 总是 .*|.* 不管 .* 总 .*|.* 不管 .* 还 .*|.* 不管 .* 也 .*|.* 任凭 .* 都 .*|.* 任凭 .* 总是 .*|.* 任凭 .* 总 .*|.* 任凭 .* 还 .*|.* 任凭 .* 也 .*|.* 任 .* 都 .*|.* 任 .* 总是 .*|.* 任 .* 总 .*|.* 任 .* 还 .*|.* 任 .* 也 .*|.* ， 要不然 .*|.* ， 要 不然 .*|.* ， 要 不 然 .*|.* ； 要不然 .*|.* ； 要 不然 .*|.* ； 要 不 然 .*|.* ， .* 要不然 .*|.* ， .* 要 不然 .*|.* ， .* 要 不 然 .*|.* ； .* 要不然 .*|.* ； .* 要 不然 .*|.* ； .* 要 不 然 .*"
        C84条件复句关联词 = ".*只要 .* 就 .*|.*只要 .* 都 .*|.*只要 .* 便 .*|.*只要 .* 总 .*|.*只需 .* 就 .*|.*只需 .* 都 .*|.*只需 .* 便 .*|.*只需 .* 总 .*|.*一旦 .* 就 .*|.*一旦 .* 都 .*|.*一旦 .* 便 .*|.*一旦 .* 总 .*|.*只有 .* 才 .*|.*只有 .* 否则 .*|.*只有 .* 不 .*|.*唯有 .* 才 .*|.*唯有 .* 否则 .*|.*唯有 .* 不 .*|.*除非 .* 才 .*|.*除非 .* 否则 .*|.*除非 .* 不 .*|.*无论 .* 都 .*|.*无论 .* 总是 .*|.*无论 .* 总 .*|.*无论 .* 还 .*|.*无论 .* 也 .*|.*不论 .* 都 .*|.*不论 .* 总是 .*|.*不论 .* 总 .*|.*不论 .* 还 .*|.*不论 .* 也 .*|.*不管 .* 都 .*|.*不管 .* 总是 .*|.*不管 .* 总 .*|.*不管 .* 还 .*|.*不管 .* 也 .*|.*任凭 .* 都 .*|.*任凭 .* 总是 .*|.*任凭 .* 总 .*|.*任凭 .* 还 .*|.*任凭 .* 也 .*|.*任 .* 都 .*|.*任 .* 总是 .*|.*任 .* 总 .*|.*任 .* 还 .*|.*任 .* 也 .*|.*， 要不然 .*|.*， 要 不然 .*|.*， 要 不 然 .*|.*； 要不然 .*|.*； 要 不然 .*|.*； 要 不 然 .*|.*，.* 要不然 .*|.*，.* 要 不然 .*|.*，.* 要 不 然 .*|.*；.* 要不然 .*|.*；.* 要 不然 .*|.*；.* 要 不 然 .*|.*, 要不然 .*|.*, 要 不然 .*|.*, 要 不 然 .*|.*; 要不然 .*|.*; 要 不然 .*|.*; 要 不 然 .*|.*,.* 要不然 .*|.*,.* 要 不然 .*|.*,.* 要 不 然 .*|.*;.* 要不然 .*|.*;.* 要 不然 .*|.*;.* 要 不 然 .*"
        C84_条件复句=[]
        for x in 句子去标注有空格:
            for i in re.finditer(C84条件复句关联词,x):
            #print(i.group()+str(i.span()))
                n = i.group()
                C84_条件复句.append(n)
        C84条件复句 = len(C84_条件复句)


        #C85假设复句：《现代汉语》增订六版下册p135
        #C85假设复句关联词 = ".* 如果 .* 就 .*|.* 如果 .* 那么 .*|.* 如果 .* 那 .*|.* 如果 .* 便 .*|.* 如果 .* 则 .*|.* 假如 .* 就 .*|.* 假如 .* 那么 .*|.* 假如 .* 那 .*|.* 假如 .* 便 .*|.* 假如 .* 则 .*|.* 假使 .* 就 .*|.* 假使 .* 那么 .*|.* 假使 .* 那 .*|.* 假使 .* 便 .*|.* 假使 .* 则 .*|.* 假若 .* 就 .*|.* 假若 .* 那么 .*|.* 假若 .* 那 .*|.* 假若 .* 便 .*|.* 假若 .* 则 .*|.* 假设 .* 就 .*|.* 假设 .* 那么 .*|.* 假设 .* 那 .*|.* 假设 .* 便 .*|.* 假设 .* 则 .*|.* 倘若 .* 就 .*|.* 倘若 .* 那么 .*|.* 倘若 .* 那 .*|.* 倘若 .* 便 .*|.* 倘若 .* 则 .*|.* 倘使 .* 就 .*|.* 倘使 .* 那么 .*|.* 倘使 .* 那 .*|.* 倘使 .* 便 .*|.* 倘使 .* 则 .*|.* 若是 .* 就 .*|.* 若是 .* 那么 .*|.* 若是 .* 那 .*|.* 若是 .* 便 .*|.* 若是 .* 则 .*|.* 若 .* 就 .*|.* 若 .* 那么 .*|.* 若 .* 那 .*|.* 若 .* 便 .*|.* 若 .* 则 .*|.* 要是 .* 就 .*|.* 要是 .* 那么 .*|.* 要是 .* 那 .*|.* 要是 .* 便 .*|.* 要是 .* 则 .*|.* 万一 .* 就 .*|.* 万一 .* 那么 .*|.* 万一 .* 那 .*|.* 万一 .* 便 .*|.* 万一 .* 则 .*|.* 即使 .* 也 .*|.* 即使 .* 还 .*|.* 就是 .* 也 .*|.* 就是 .* 还 .*|.* 就算 .* 也 .*|.* 就算 .* 还 .*|.* 纵使 .* 也 .*|.* 纵使 .* 还 .*|.* 纵然 .* 也 .*|.* 纵然 .* 还 .*|.* 哪怕 .* 也 .*|.* 哪怕 .* 还 .*|.* 再 .* 也 .*|.* ， 那么 .*|.* ， 那 .*|.* ， 便 .*|.* ， 就 .*|.* ， 则 .*|.* 的话 .*|.* 的 话 .*|.* ，也 .*|.* ， 还 .*|.* ； 那么 .*|.* ； 那 .*|.* ； 便 .*|.* ； 就 .*|.* ； 则 .*|.* ； 也 .*|.* ； 还 .*|.* ， .* 那么 .*|.* ， .* 那 .*|.* ， .* 便 .*|.* ， .* 就 .*|.* ， .* 则 .*|.* ， .* 也 .*|.* ， .* 还 .*|.* ； .* 那么 .*|.* ； .* 那 .*|.* ； .* 便 .*|.* ； .* 就 .*|.* ； .* 则 .*|.* ； .* 也 .*|.* ； .* 还 .*"        
        #C85假设复句关联词 = ".* 如果 .* 就 .*|.* 如果 .* 那么 .*|.* 如果 .* 那 .*|.* 如果 .* 便 .*|.* 如果 .* 则 .*|.* 假如 .* 就 .*|.* 假如 .* 那么 .*|.* 假如 .* 那 .*|.* 假如 .* 便 .*|.* 假如 .* 则 .*|.* 假使 .* 就 .*|.* 假使 .* 那么 .*|.* 假使 .* 那 .*|.* 假使 .* 便 .*|.* 假使 .* 则 .*|.* 假若 .* 就 .*|.* 假若 .* 那么 .*|.* 假若 .* 那 .*|.* 假若 .* 便 .*|.* 假若 .* 则 .*|.* 假设 .* 就 .*|.* 假设 .* 那么 .*|.* 假设 .* 那 .*|.* 假设 .* 便 .*|.* 假设 .* 则 .*|.* 倘若 .* 就 .*|.* 倘若 .* 那么 .*|.* 倘若 .* 那 .*|.* 倘若 .* 便 .*|.* 倘若 .* 则 .*|.* 倘使 .* 就 .*|.* 倘使 .* 那么 .*|.* 倘使 .* 那 .*|.* 倘使 .* 便 .*|.* 倘使 .* 则 .*|.* 若是 .* 就 .*|.* 若是 .* 那么 .*|.* 若是 .* 那 .*|.* 若是 .* 便 .*|.* 若是 .* 则 .*|.* 若 .* 就 .*|.* 若 .* 那么 .*|.* 若 .* 那 .*|.* 若 .* 便 .*|.* 若 .* 则 .*|.* 要是 .* 就 .*|.* 要是 .* 那么 .*|.* 要是 .* 那 .*|.* 要是 .* 便 .*|.* 要是 .* 则 .*|.* 万一 .* 就 .*|.* 万一 .* 那么 .*|.* 万一 .* 那 .*|.* 万一 .* 便 .*|.* 万一 .* 则 .*|.* 即使 .* 也 .*|.* 即使 .* 还 .*|.* 就是 .* 也 .*|.* 就是 .* 还 .*|.* 就算 .* 也 .*|.* 就算 .* 还 .*|.* 纵使 .* 也 .*|.* 纵使 .* 还 .*|.* 纵然 .* 也 .*|.* 纵然 .* 还 .*|.* 哪怕 .* 也 .*|.* 哪怕 .* 还 .*|.* 再 .* 也 .*|.* ， 那么 .*|.* 的话 .*|.* 的 话 .*|.* ； 那么 .*|.* ， .* 那么 .*|.* ； .* 那么 .*"
        #在上一步基础上删去单用的: “便”、“就”、“那”、“则”、“也”、“还” 
        
        C85假设复句关联词 = ".*如果 .* 就 .*|.*如果 .* 那么 .*|.*如果 .* 那 .*|.*如果 .* 便 .*|.*如果 .* 则 .*|.*假如 .* 就 .*|.*假如 .* 那么 .*|.*假如 .* 那 .*|.*假如 .* 便 .*|.*假如 .* 则 .*|.*假使 .* 就 .*|.*假使 .* 那么 .*|.*假使 .* 那 .*|.*假使 .* 便 .*|.*假使 .* 则 .*|.*假若 .* 就 .*|.*假若 .* 那么 .*|.*假若 .* 那 .*|.*假若 .* 便 .*|.*假若 .* 则 .*|.*假设 .* 就 .*|.*假设 .* 那么 .*|.*假设 .* 那 .*|.*假设 .* 便 .*|.*假设 .* 则 .*|.*倘若 .* 就 .*|.*倘若 .* 那么 .*|.*倘若 .* 那 .*|.*倘若 .* 便 .*|.*倘若 .* 则 .*|.*倘使 .* 就 .*|.*倘使 .* 那么 .*|.*倘使 .* 那 .*|.*倘使 .* 便 .*|.*倘使 .* 则 .*|.*若是 .* 就 .*|.*若是 .* 那么 .*|.*若是 .* 那 .*|.*若是 .* 便 .*|.*若是 .* 则 .*|.*若 .* 就 .*|.*若 .* 那么 .*|.*若 .* 那 .*|.*若 .* 便 .*|.*若 .* 则 .*|.*要是 .* 就 .*|.*要是 .* 那么 .*|.*要是 .* 那 .*|.*要是 .* 便 .*|.*要是 .* 则 .*|.*万一 .* 就 .*|.*万一 .* 那么 .*|.*万一 .* 那 .*|.*万一 .* 便 .*|.*万一 .* 则 .*|.*即使 .* 也 .*|.*即使 .* 还 .*|.*就是 .* 也 .*|.*就是 .* 还 .*|.*就算 .* 也 .*|.*就算 .* 还 .*|.*纵使 .* 也 .*|.*纵使 .* 还 .*|.*纵然 .* 也 .*|.*纵然 .* 还 .*|.*哪怕 .* 也 .*|.*哪怕 .* 还 .*|.*再 .* 也 .*|.*， 那么 .*|.*的话.*|.*； 那么 .*|.*，.* 那么 .*|.*；.* 那么 .*| .*, 那么 .*|.*的话.*|.*; 那么 .*|.*,.* 那么 .*|.*;.* 那么 .*"    
        C85_假设复句=[]
        for x in 句子去标注有空格:
            for i in re.finditer(C85假设复句关联词,x):
            #print(i.group()+str(i.span()))
                n = i.group()
                C85_假设复句.append(n)
        C85假设复句 = len(C85_假设复句)


        #C86因果复句：《现代汉语》增订六版下册p136
        #C86因果复句关联词 = ".* 因为 .* 所以 .*|.* 因为 .* 才 .*|.* 因为 .* 就 .*|.* 因为 .* 便 .*|.* 因为 .* 故 .*|.* 因为 .* 于是 .*|.* 因为 .* 因此 .*|.* 因为 .* 因而 .*|.* 因为 .* 以致 .*|.* 因 .* 所以 .*|.* 因 .* 才 .*|.* 因 .* 就 .*|.* 因 .* 便 .*|.* 因 .* 故 .*|.* 因 .* 于是 .*|.* 因 .* 因此 .*|.* 因 .* 因而 .*|.* 因 .* 以致 .*|.* 由于 .* 所以 .*|.* 由于 .* 才 .*|.* 由于 .* 就 .*|.* 由于 .* 便 .*|.* 由于 .* 故 .*|.* 由于 .* 于是 .*|.* 由于 .* 因此 .*|.* 由于 .* 因而 .*|.* 由于 .* 以致 .*|.* 之所以 .* 是因为 .*|.* 之所以 .* 是由于 .*|.* 之所以 .* 就在于 .*|.* 之 所以 .* 是因为 .*|.* 之 所以 .* 是由于 .*|.* 之 所以 .* 就在于 .*|.* 之所以 .* 是 因为 .*|.* 之所以 .* 是 由于 .*|.* 之所以 .* 就 在于 .*|.* 之 所以 .* 是 因为 .*|.* 之 所以 .* 是 由于 .*|.* 之 所以 .* 就 在于 .*|.* 既然 .* 那么 .*|.* 既然 .* 就 .*|.* 既然 .* 又 .*|.* 既然 .* 便 .*|.* 既然 .* 则|.* 既然 .* 可见 .*|.* ， 是因为 .*|.* ； 是因为 .*|.* ， 是由于 .*|.* ； 是由于 .*|.* ， 是 因为 .*|.* ； 是 因为 .*|.* ， 是 由于 .*|.* ； 是 由于 .*|.* ， 因为 .*|.* ， 由于 .*|.* ， 所以 .*|.* ， 因此 .*|.* ， 因而 .*|.* ， 以致 .*|.* ， 致使 .*|.* ， 从而 .*|.* ， 以至 .*|.* ， 以至于 .*|.* ， 以至 于 .*|.* ， 既然 .*|.* ， 既 .*|.* ， 可见 .*|.* ； 因为 .*|.* ； 由于 .*|.* ； 所以 .*|.* ； 因此 .*|.* ； 因而 .*|.* ； 以致 .*|.* ； 致使 .*|.* ； 从而 .*|.* ； 以至 .*|.* ； 以至于 .*|.* ； 既然 .*|.* ； 既 .*|.* ； 可见 .*|.* ， .* 是因为 .*|.* ； .* 是因为 .*|.* ， .* 是由于 .*|.* ； .* 是由于 .*|.* ， .* 是 因为 .*|.* ； .* 是 因为 .*|.* ， .* 是 由于 .*|.* ； .* 是 由于 .*|.* ， .* 因为 .*|.* ， .* 由于 .*|.* ， .* 所以 .*|.* ， .* 因此 .*|.* ， .* 因而 .*|.* ， .* 以致 .*|.* ， .* 致使 .*|.* ， .* 从而 .*|.* ， .* 以至 .*|.* ， .* 以至于 .*|.* ， .* 以至 于 .*|.* ， .* 既然 .*|.* ， .* 既 .*|.* ， .* 可见 .*|.* ； .* 因为 .*|.* ； .* 由于 .*|.* ； .* 所以 .*|.* ； .* 因此 .*|.* ； .* 因而 .*|.* ； .* 以致 .*|.* ； .* 致使 .*|.* ； .* 从而 .*|.* ； .* 以至 .*|.* ； .* 以至于 .*|.* ； .* 既然 .*|.* ； .* 既 .*|.* ； .* 可见 .*"
        #在上一步基础上删去单用的: “既”、“就” 
        #C86因果复句关联词 = ".* 因为 .* 所以 .*|.* 因为 .* 才 .*|.* 因为 .* 就 .*|.* 因为 .* 便 .*|.* 因为 .* 故 .*|.* 因为 .* 于是 .*|.* 因为 .* 因此 .*|.* 因为 .* 因而 .*|.* 因为 .* 以致 .*|.* 因 .* 所以 .*|.* 因 .* 才 .*|.* 因 .* 就 .*|.* 因 .* 便 .*|.* 因 .* 故 .*|.* 因 .* 于是 .*|.* 因 .* 因此 .*|.* 因 .* 因而 .*|.* 因 .* 以致 .*|.* 由于 .* 所以 .*|.* 由于 .* 才 .*|.* 由于 .* 就 .*|.* 由于 .* 便 .*|.* 由于 .* 故 .*|.* 由于 .* 于是 .*|.* 由于 .* 因此 .*|.* 由于 .* 因而 .*|.* 由于 .* 以致 .*|.* 之所以 .* 是因为 .*|.* 之所以 .* 是由于 .*|.* 之所以 .* 就在于 .*|.* 之 所以 .* 是因为 .*|.* 之 所以 .* 是由于 .*|.* 之 所以 .* 就在于 .*|.* 之所以 .* 是 因为 .*|.* 之所以 .* 是 由于 .*|.* 之所以 .* 就 在于 .*|.* 之 所以 .* 是 因为 .*|.* 之 所以 .* 是 由于 .*|.* 之 所以 .* 就 在于 .*|.* 既然 .* 那么 .*|.* 既然 .* 就 .*|.* 既然 .* 又 .*|.* 既然 .* 便 .*|.* 既然 .* 则|.* 既然 .* 可见 .*|.* ， 是因为 .*|.* ； 是因为 .*|.* ， 是由于 .*|.* ； 是由于 .*|.* ， 是 因为 .*|.* ； 是 因为 .*|.* ， 是 由于 .*|.* ； 是 由于 .*|.* ， 因为 .*|.* ， 由于 .*|.* ， 所以 .*|.* ， 因此 .*|.* ， 因而 .*|.* ， 以致 .*|.* ， 致使 .*|.* ， 从而 .*|.* ， 以至 .*|.* ， 以至于 .*|.* ， 以至 于 .*|.* ， 既然 .*|.* ， 可见 .*|.* ； 因为 .*|.* ； 由于 .*|.* ； 所以 .*|.* ； 因此 .*|.* ； 因而 .*|.* ； 以致 .*|.* ； 致使 .*|.* ； 从而 .*|.* ； 以至 .*|.* ； 以至于 .*|.* ； 既然 .*|.* ； 可见 .*|.* ， .* 是因为 .*|.* ； .* 是因为 .*|.* ， .* 是由于 .*|.* ； .* 是由于 .*|.* ， .* 是 因为 .*|.* ； .* 是 因为 .*|.* ， .* 是 由于 .*|.* ； .* 是 由于 .*|.* ， .* 因为 .*|.* ， .* 由于 .*|.* ， .* 所以 .*|.* ， .* 因此 .*|.* ， .* 因而 .*|.* ， .* 以致 .*|.* ， .* 致使 .*|.* ， .* 从而 .*|.* ， .* 以至 .*|.* ， .* 以至于 .*|.* ， .* 以至 于 .*|.* ， .* 既然 .*|.* ， .* 可见 .*|.* ； .* 因为 .*|.* ； .* 由于 .*|.* ； .* 所以 .*|.* ； .* 因此 .*|.* ； .* 因而 .*|.* ； .* 以致 .*|.* ； .* 致使 .*|.* ； .* 从而 .*|.* ； .* 以至 .*|.* ； .* 以至于 .*|.* ； .* 既然 .*|.* ； .* 可见 .*"
        C86因果复句关联词 =".*因为 .* 所以 .*|.*因为 .* 才 .*|.*因为 .* 就 .*|.*因为 .* 便 .*|.*因为 .* 故 .*|.*因为 .* 于是 .*|.*因为 .* 因此 .*|.*因为 .* 因而 .*|.*因为 .* 以致 .*|.*因 .* 所以 .*|.*因 .* 才 .*|.*因 .* 就 .*|.*因 .* 便 .*|.*因 .* 故 .*|.*因 .* 于是 .*|.*因 .* 因此 .*|.*因 .* 因而 .*|.*因 .* 以致 .*|.*由于 .* 所以 .*|.*由于 .* 才 .*|.*由于 .* 就 .*|.*由于 .* 便 .*|.*由于 .* 故 .*|.*由于 .* 于是 .*|.*由于 .* 因此 .*|.*由于 .* 因而 .*|.*由于 .* 以致 .*|.*之所以 .* 是因为 .*|.*之所以 .* 是由于 .*|.*之所以 .* 就在于 .*|.*之 所以 .* 是因为 .*|.*之 所以 .* 是由于 .*|.*之 所以 .* 就在于 .*|.*之所以 .* 是 因为 .*|.*之所以 .* 是 由于 .*|.*之所以 .* 就 在于 .*|.*之 所以 .* 是 因为 .*|.*之 所以 .* 是 由于 .*|.*之 所以 .* 就 在于 .*|.*既然 .* 那么 .*|.*既然 .* 就 .*|.*既然 .* 又 .*|.*既然 .* 便 .*|.*既然 .* 则|.*既然 .* 可见 .*|.*， 是因为 .*|.*； 是因为 .*|.*， 是由于 .*|.*； 是由于 .*|.*， 是 因为 .*|.*； 是 因为 .*|.*， 是 由于 .*|.*； 是 由于 .*|.*， 因为 .*|.*， 由于 .*|.*， 所以 .*|.*， 因此 .*|.*， 因而 .*|.*， 以致 .*|.*， 致使 .*|.*， 从而 .*|.*， 以至 .*|.*， 以至于 .*|.*， 以至 于 .*|.*， 既然 .*|.*， 可见 .*|.*； 因为 .*|.*； 由于 .*|.*； 所以 .*|.*； 因此 .*|.*； 因而 .*|.*； 以致 .*|.*； 致使 .*|.*； 从而 .*|.*； 以至 .*|.*； 以至于 .*|.*； 既然 .*|.*； 可见 .*|.*，.* 是因为 .*|.*；.* 是因为 .*|.*，.* 是由于 .*|.*；.* 是由于 .*|.*，.* 是 因为 .*|.*；.* 是 因为 .*|.*，.* 是 由于 .*|.*；.* 是 由于 .*|.*，.* 因为 .*|.*，.* 由于 .*|.*，.* 所以 .*|.*，.* 因此 .*|.*，.* 因而 .*|.*，.* 以致 .*|.*，.* 致使 .*|.*，.* 从而 .*|.*，.* 以至 .*|.*，.* 以至于 .*|.*，.* 以至 于 .*|.*，.* 既然 .*|.*，.* 可见 .*|.*；.* 因为 .*|.*；.* 由于 .*|.*；.* 所以 .*|.*；.* 因此 .*|.*；.* 因而 .*|.*；.* 以致 .*|.*；.* 致使 .*|.*；.* 从而 .*|.*；.* 以至 .*|.*；.* 以至于 .*|.*；.* 既然 .*|.*；.* 可见 .*|.*, 是因为 .*|.*; 是因为 .*|.*, 是由于 .*|.*; 是由于 .*|.*, 是 因为 .*|.*; 是 因为 .*|.*, 是 由于 .*|.*; 是 由于 .*|.*, 因为 .*|.*, 由于 .*|.*, 所以 .*|.*, 因此 .*|.*, 因而 .*|.*, 以致 .*|.*, 致使 .*|.*, 从而 .*|.*, 以至 .*|.*, 以至于 .*|.*, 以至 于 .*|.*, 既然 .*|.*, 可见 .*|.*; 因为 .*|.*; 由于 .*|.*; 所以 .*|.*; 因此 .*|.*; 因而 .*|.*; 以致 .*|.*; 致使 .*|.*; 从而 .*|.*; 以至 .*|.*; 以至于 .*|.*; 既然 .*|.*; 可见 .*|.*,.* 是因为 .*|.*;.* 是因为 .*|.*,.* 是由于 .*|.*;.* 是由于 .*|.*,.* 是 因为 .*|.*;.* 是 因为 .*|.*,.* 是 由于 .*|.*;.* 是 由于 .*|.*,.* 因为 .*|.*,.* 由于 .*|.*,.* 所以 .*|.*,.* 因此 .*|.*,.* 因而 .*|.*,.* 以致 .*|.*,.* 致使 .*|.*,.* 从而 .*|.*,.* 以至 .*|.*,.* 以至于 .*|.*,.* 以至 于 .*|.*,.* 既然 .*|.*,.* 可见 .*|.*;.* 因为 .*|.*;.* 由于 .*|.*;.* 所以 .*|.*;.* 因此 .*|.*;.* 因而 .*|.*;.* 以致 .*|.*;.* 致使 .*|.*;.* 从而 .*|.*;.* 以至 .*|.*;.* 以至于 .*|.*;.* 既然 .*|.*;.* 可见 .*"
        C86_因果复句=[]
        for x in 句子去标注有空格:
            for i in re.finditer(C86因果复句关联词,x):
            #print(i.group()+str(i.span()))
                n = i.group()
                C86_因果复句.append(n)
        C86因果复句 = len(C86_因果复句)


        #C87目的复句：《现代汉语》增订六版下册p138
        #C87目的复句关联词 = ".* ， .* 以便 .*|.* ， .* 以求 .*|.* ， .* 以 .*|.* ， .* 用以 .*|.* ， .* 借以 .*|.* ， .* 好让 .*|.* ， .* 好 .*|.* ， .* 为的是 .*|.* ， .* 为的 是 .*|.* ， .* 为 的 是 .*|.* ， .* 以免 .*|.* ， .* 免得 .*|.* ， .* 省得 .*|.* ， .* 以防 .*|.* ； .* 以便 .*|.* ； .* 以求 .*|.* ； .* 以 .*|.* ； .* 用以 .*|.* ； .* 借以 .*|.* ； .* 好让 .*|.* ； .* 好 .*|.* ； .* 以免 .*|.* ； .* 免得 .*|.* ； .* 省得 .*|.* ； .* 以防 .*|.* ； .* 为的是 .*|.* ； .* 为的 是 .*|.* ； .* 为 的 是 .*|.* ， 以便 .*|.* ， 以求 .*|.* ， 以 .*|.* ， 用以 .*|.* ， 借以 .*|.* ， 好让 .*|.* ， 好 .*|.* ， 为的是 .*|.* ， 为 的 是 .*|.* ， 为的 是 .*|.* ， 以免 .*|.* ， 免得 .*|.* ， 省得 .*|.* ， 以防 .*|.* ； 以便 .*|.* ； 以求 .*|.* ； 以 .*|.* ； 用以 .*|.* ； 借以 .*|.* ； 好让 .*|.* ； 好 .*|.* ； 以免 .*|.* ； 免得 .*|.* ； 省得 .*|.* ； 以防 .*|.* ； 为的是 .*|.* ； 为的 是 .*|.* ； 为 的 是 .*"
        #在上一步基础上删去单用的: “以”、“好” 
        C87目的复句关联词 =".*，.* 以便 .*|.*，.* 以求 .*|.*，.* 以 求 .*|.*，.* 用以 .*|.*，.* 借以 .*|.*，.* 好让 .*|.*，.* 好 让 .*|.*，.* 为的是 .*|.*，.* 为的 是 .*|.*，.* 为 的 是 .*|.*，.* 以免 .*|.*，.* 免得 .*|.*，.* 省得 .*|.*，.* 以防 .*|.*；.* 以便 .*|.*；.* 以求 .*|.*；.* 以 求 .*|.*；.* 用以 .*|.*；.* 借以 .*|.*；.* 好让 .*|.*；.* 好 让 .*|.*；.* 以免 .*|.*；.* 免得 .*|.*；.* 省得 .*|.*；.* 以防 .*|.*；.* 为的是 .*|.*；.* 为的 是 .*|.*；.* 为 的 是 .*|.* ， 以便 .*|.* ， 以求 .*|.* ， 以 求 .*|.* ， 用以 .*|.* ， 借以 .*|.* ， 好让 .*|.* ， 好 让 .*|.* ， 为的是 .*|.* ， 为 的 是 .*|.* ， 为的 是 .*|.* ， 以免 .*|.* ， 免得 .*|.* ， 省得 .*|.* ， 以防 .*|.* ； 以便 .*|.* ； 以求 .*|.* ； 以 求 .*|.* ； 用以 .*|.* ； 借以 .*|.* ； 好让 .*|.* ； 好 让 .*|.* ； 以免 .*|.* ； 免得 .*|.* ； 省得 .*|.* ； 以防 .*|.* ； 为的是 .*|.* ； 为的 是 .*|.* ； 为 的 是 .*|.*,.* 以便 .*|.*,.* 以求 .*|.*,.* 以 求 .*|.*,.* 用以 .*|.*,.* 借以 .*|.*,.* 好让 .*|.*,.* 好 让 .*|.*,.* 为的是 .*|.*,.* 为的 是 .*|.*,.* 为 的 是 .*|.*,.* 以免 .*|.*,.* 免得 .*|.*,.* 省得 .*|.*,.* 以防 .*|.*;.* 以便 .*|.*;.* 以求 .*|.*;.* 以 求 .*|.*;.* 用以 .*|.*;.* 借以 .*|.*;.* 好让 .*|.*;.* 好 让 .*|.*;.* 以免 .*|.*;.* 免得 .*|.*;.* 省得 .*|.*;.* 以防 .*|.*;.* 为的是 .*|.*;.* 为的 是 .*|.*;.* 为 的 是 .*|.* , 以便 .*|.* , 以求 .*|.* , 以 求 .*|.* , 用以 .*|.* , 借以 .*|.* , 好让 .*|.* , 好 让 .*|.* , 为的是 .*|.* , 为 的 是 .*|.* , 为的 是 .*|.* , 以免 .*|.* , 免得 .*|.* , 省得 .*|.* , 以防 .*|.* ; 以便 .*|.* ; 以求 .*|.* ; 以 求 .*|.* ; 用以 .*|.* ; 借以 .*|.* ; 好让 .*|.* ; 好 让 .*|.* ; 以免 .*|.* ; 免得 .*|.* ; 省得 .*|.* ; 以防 .*|.* ; 为的是 .*|.* ; 为的 是 .*|.* ; 为 的 是 .*"
        C87_目的复句=[]
        for x in 句子去标注有空格:
            for i in re.finditer(C87目的复句关联词,x):
                n = i.group()
                C87_目的复句.append(n)
        C87目的复句 = len(C87_目的复句)


        #C88转折复句：《现代汉语》增订六版下册p138
        #C88转折复句关联词 = ".* 虽然 .* 但是 .*|.* 虽然 .* 可是 .*|.* 虽然 .* 然而 .*|.* 虽然 .* 但 .*|.* 虽然 .* 却 .*|.* 虽然 .* 还 .*|.* 虽然 .* 也 .*|.* 虽然 .* 而 .*|.* 虽是 .* 但是 .*|.* 虽是 .* 可是 .*|.* 虽是 .* 然而 .*|.* 虽是 .* 但 .*|.* 虽是 .* 却 .*|.* 虽是 .* 还 .*|.* 虽是 .* 也 .*|.* 虽是 .* 而 .*|.* 虽说 .* 但是 .*|.* 虽说 .* 可是 .*|.* 虽说 .* 然而 .*|.* 虽说 .* 但 .*|.* 虽说 .* 却 .*|.* 虽说 .* 还 .*|.* 虽说 .* 也 .*|.* 虽说 .* 而 .*|.* 虽则 .* 但是 .*|.* 虽则 .* 可是 .*|.* 虽则 .* 然而 .*|.* 虽则 .* 但 .*|.* 虽则 .* 却 .*|.* 虽则 .* 还 .*|.* 虽则 .* 也 .*|.* 虽则 .* 而 .*|.* 虽 .* 但是 .*|.* 虽 .* 可是 .*|.* 虽 .* 然而 .*|.* 虽 .* 但 .*|.* 虽 .* 却 .*|.* 虽 .* 还 .*|.* 虽 .* 也 .*|.* 虽 .* 而|.* 尽管 .* 但是 .*|.* 尽管 .* 可是 .*|.* 尽管 .* 然而 .*|.* 尽管 .* 但 .*|.* 尽管 .* 却 .*|.* 尽管 .* 还 .*|.* 尽管 .* 也 .*|.* 尽管 .* 而 .*|.* 固然 .* 但是 .*|.* 固然 .* 可是 .*|.* 固然 .* 然而 .*|.* 固然 .* 但 .*|.* 固然 .* 却 .*|.* 固然 .* 还 .*|.* 固然 .* 也 .*|.* 固然 .* 而 .*|.* ， .* 虽然 .*|.* ， .* 但是 .*|.* ， .* 但 .*|.* ， .* 然而 .*|.* ， .* 可是 .*|.* ， .* 可 .*|.* ， .* 却 .*|.* ， .* 只是 .*|.* ， .* 不过 .*|.* ， .* 倒 .*|.* ； .* 虽然 .*|.* ； .* 但是 .*|.* ； .* 但 .*|.* ； .* 然而 .*|.* ； .* 可是 .*|.* ； .* 可 .*|.* ； .* 却 .*|.* ； .* 只是 .*|.* ； .* 不过 .*|.* ； .* 倒 .*|.* ， 虽然 .*|.* ， 但是 .*|.* ， 但 .*|.* ， 然而 .*|.* ， 可是 .*|.* ， 可 .*|.* ， 却 .*|.* ， 只是 .*|.* ， 不过 .*|.* ， 倒 .*|.* ； 虽然 .*|.* ； 但是 .*|.* ； 但 .*|.* ； 然而 .*|.* ； 可是 .*|.* ； 可 .*|.* ； 却 .*|.* ； 只是 .*|.* ； 不过 .*|.* ； 倒.*"
        #在上一步基础上删去单用的: “可”、“却” 、“倒”
        #C88转折复句关联词 = ".* 虽然 .* 但是 .*|.* 虽然 .* 可是 .*|.* 虽然 .* 然而 .*|.* 虽然 .* 但 .*|.* 虽然 .* 却 .*|.* 虽然 .* 还 .*|.* 虽然 .* 也 .*|.* 虽然 .* 而 .*|.* 虽是 .* 但是 .*|.* 虽是 .* 可是 .*|.* 虽是 .* 然而 .*|.* 虽是 .* 但 .*|.* 虽是 .* 却 .*|.* 虽是 .* 还 .*|.* 虽是 .* 也 .*|.* 虽是 .* 而 .*|.* 虽说 .* 但是 .*|.* 虽说 .* 可是 .*|.* 虽说 .* 然而 .*|.* 虽说 .* 但 .*|.* 虽说 .* 却 .*|.* 虽说 .* 还 .*|.* 虽说 .* 也 .*|.* 虽说 .* 而 .*|.* 虽则 .* 但是 .*|.* 虽则 .* 可是 .*|.* 虽则 .* 然而 .*|.* 虽则 .* 但 .*|.* 虽则 .* 却 .*|.* 虽则 .* 还 .*|.* 虽则 .* 也 .*|.* 虽则 .* 而 .*|.* 虽 .* 但是 .*|.* 虽 .* 可是 .*|.* 虽 .* 然而 .*|.* 虽 .* 但 .*|.* 虽 .* 却 .*|.* 虽 .* 还 .*|.* 虽 .* 也 .*|.* 虽 .* 而|.* 尽管 .* 但是 .*|.* 尽管 .* 可是 .*|.* 尽管 .* 然而 .*|.* 尽管 .* 但 .*|.* 尽管 .* 却 .*|.* 尽管 .* 还 .*|.* 尽管 .* 也 .*|.* 尽管 .* 而 .*|.* 固然 .* 但是 .*|.* 固然 .* 可是 .*|.* 固然 .* 然而 .*|.* 固然 .* 但 .*|.* 固然 .* 却 .*|.* 固然 .* 还 .*|.* 固然 .* 也 .*|.* 固然 .* 而 .*|.* ， .* 虽然 .*|.* ， .* 但是 .*|.* ， .* 但 .*|.* ， .* 然而 .*|.* ， .* 可是 .*|.* ， .* 只是 .*|.* ， .* 不过 .*|.* ； .* 虽然 .*|.* ； .* 但是 .*|.* ； .* 但 .*|.* ； .* 然而 .*|.* ； .* 可是 .*|.* ； .* 只是 .*|.* ； .* 不过 .*|.* ； .* 倒 .*|.* ， 虽然 .*|.* ， 但是 .*|.* ， 但 .*|.* ， 然而 .*|.* ， 可是 .*|.* ， 只是 .*|.* ， 不过 .*|.* ； 虽然 .*|.* ； 但是 .*|.* ； 但 .*|.* ； 然而 .*|.* ； 可是 .*|.* ； 只是 .*|.* ； 不过 .*"
        C88转折复句关联词 = ".*虽然 .* 但是 .*|.*虽然 .* 可是 .*|.*虽然 .* 然而 .*|.*虽然 .* 但 .*|.*虽然 .* 却 .*|.*虽然 .* 还 .*|.*虽然 .* 也 .*|.*虽然 .* 而 .*|.*虽是 .* 但是 .*|.*虽是 .* 可是 .*|.*虽是 .* 然而 .*|.*虽是 .* 但 .*|.*虽是 .* 却 .*|.*虽是 .* 还 .*|.*虽是 .* 也 .*|.*虽是 .* 而 .*|.*虽说 .* 但是 .*|.*虽说 .* 可是 .*|.*虽说 .* 然而 .*|.*虽说 .* 但 .*|.*虽说 .* 却 .*|.*虽说 .* 还 .*|.*虽说 .* 也 .*|.*虽说 .* 而 .*|.*虽则 .* 但是 .*|.*虽则 .* 可是 .*|.*虽则 .* 然而 .*|.*虽则 .* 但 .*|.*虽则 .* 却 .*|.*虽则 .* 还 .*|.*虽则 .* 也 .*|.*虽则 .* 而 .*|.*虽 .* 但是 .*|.*虽 .* 可是 .*|.*虽 .* 然而 .*|.*虽 .* 但 .*|.*虽 .* 却 .*|.*虽 .* 还 .*|.*虽 .* 也 .*|.*虽 .* 而|.*尽管 .* 但是 .*|.*尽管 .* 可是 .*|.*尽管 .* 然而 .*|.*尽管 .* 但 .*|.*尽管 .* 却 .*|.*尽管 .* 还 .*|.*尽管 .* 也 .*|.*尽管 .* 而 .*|.*固然 .* 但是 .*|.*固然 .* 可是 .*|.*固然 .* 然而 .*|.*固然 .* 但 .*|.*固然 .* 却 .*|.*固然 .* 还 .*|.*固然 .* 也 .*|.*固然 .* 而 .*|.*，.* 虽然 .*|.*，.* 但是 .*|.*，.* 但 .*|.*，.* 然而 .*|.*，.* 可是 .*|.*，.* 可 .*|.*，.* 却 .*|.*，.* 只是 .*|.*，.* 不过 .*|.*；.* 虽然 .*|.*；.* 但是 .*|.*；.* 但 .*|.*；.* 然而 .*|.*；.* 可是 .*|.*；.* 可 .*|.*；.* 却 .*|.*；.* 只是 .*|.*；.* 不过 .*|.*， 虽然 .*|.*， 但是 .*|.*， 但 .*|.*， 然而 .*|.*， 可是 .*|.*， 可 .*|.*， 却 .*|.*， 只是 .*|.*， 不过 .*|.*； 虽然 .*|.*； 但是 .*|.*； 但 .*|.*； 然而 .*|.*； 可是 .*|.*； 可 .*|.*； 却 .*|.*； 只是 .*|.*； 不过 .*|.*,.* 虽然 .*|.*,.* 但是 .*|.*,.* 但 .*|.*,.* 然而 .*|.*,.* 可是 .*|.*,.* 可 .*|.*,.* 却 .*|.*,.* 只是 .*|.*,.* 不过 .*|.*;.* 虽然 .*|.*;.* 但是 .*|.*;.* 但 .*|.*;.* 然而 .*|.*;.* 可是 .*|.*;.* 可 .*|.*;.* 却 .*|.*;.* 只是 .*|.*;.* 不过 .*|.*, 虽然 .*|.*, 但是 .*|.*, 但 .*|.*, 然而 .*|.*, 可是 .*|.*, 可 .*|.*, 却 .*|.*, 只是 .*|.*, 不过 .*|.*; 虽然 .*|.*; 但是 .*|.*; 但 .*|.*; 然而 .*|.*; 可是 .*|.*; 可 .*|.*; 却 .*|.*; 只是 .*|.*; 不过 .*"
        C88_转折复句=[]
        for x in 句子去标注有空格:
            for i in re.finditer(C88转折复句关联词,x):
                n = i.group()
                C88_转折复句.append(n)
        C88转折复句 = len(C88_转折复句)


        
        dic[Filename] = C75_被动句式,C76_无施事者被动句,C77_过去时貌词,C78_进行式句式,C79并列复句,C80顺承复句,C81解说复句,C82选择复句,C83递进复句,C84条件复句,C85假设复句,C86因果复句,C87目的复句,C88转折复句,C75_被动句式句子,C76_无施事者被动句句子,C77_过去时貌词句子,C78进行式句式句子,C79_并列复句,C80_顺承复句,C81_解说复句,C82_选择复句,C83_递进复句,C84_条件复句,C85_假设复句,C86_因果复句,C87_目的复句,C88_转折复句 
    #df = pd.DataFrame(dic,index=["字数"])
    df被动句_复句 = pd.DataFrame(dic,['75.被动句式','76.无施事者被动句',"77.过去时貌词","78.进行式句式",'79.并列复句','80.顺承复句','81.解说复句','82.选择复句','83.递进复句','84.条件复句','85.假设复句','86.因果复句','87.目的复句','88.转折复句',"C75_被动句式句子","C76_无施事者被动句句子","C77_过去时貌词句子","C78_进行式句式句子","C79_并列复句句子","C80_顺承复句句子","C81_解说复句句子","C82_选择复句句子","C83_递进复句句子","C84_条件复句句子","C85_假设复句句子","C86_因果复句句子","C87_目的复句句子","C88_转折复句句子"])

    df被动句_复句.columns = [columns.split("/")[-1] for columns in df被动句_复句.columns]

    # 统计每种检索式的总频度sum
    freq_sum = df被动句_复句.apply(lambda x : x.sum(), axis=1) #axis=0,按列相加；axis=1，按行相加 
    df被动句_复句["sum_s"]=freq_sum 

    df被动句_复句 = df被动句_复句.T
    #df被动句_复句



    ######## 表格合并
    #df92项语言特征 = pd.concat([df,df重叠式[df重叠式.columns[-1]],df被动句_复句],axis=1).fillna(0) #axis=1，从左到右
    df92项语言特征1 = pd.concat([df,df被动句_复句],axis=1).fillna(0) #axis=1，从左到右

    df92项语言特征 =df92项语言特征1.sort_index(ascending=True) 
    
    # df92项语言特征.to_csv("/Users/qinxu/Jupyter_work/2022博士论文语料/运行结果/20220605_92项语言特征原始频度.csv")
  






    ### 数据标准化
    #col = df92项语言特征.columns[11:100]
    col = df92项语言特征.columns[11:99]
    col基本项目 = df92项语言特征.columns[:4]

    df92项语言特征_col基本项目=df92项语言特征[col基本项目]
    #df92项语言特征_col基本项目
    #col
    #df92项语言特征_col基本项目

    df92项语言特征_标准化 = df92项语言特征.apply(lambda x: x[col]/x['字数无标点']*1000, axis=1)
    #df86项语言特征_标准化.to_csv("/Users/qinxu/Jupyter_work/2022博士论文语料/20220404_df88项语言特征_标准化.csv")
    #df92项语言特征_标准化


    df92项语言特征标准化数据= pd.concat([df92项语言特征_标准化,df92项语言特征_col基本项目],axis=1).fillna(0)
    #df92项语言特征标准化数据.to_csv("/Users/qinxu/Jupyter_work/2022博士论文语料/运行结果/20220605_df92项语言特征标准化数据.csv")
    





###### 在界面生成表格
    st.sidebar.title("Frequency Count")
    if st.sidebar.checkbox("Raw Frequency"):
        st.header("Raw Frequency of 92 Linguistic Features")
        #st.write('<span style="color:darkblue;font-size:13px;font-weight:bold">Note: R_Freq is the Relative frequency per 1,000 Chinese characters (Punctuation included).</span>',unsafe_allow_html=True)
        #st.write('<span style="color:darkblue;font-size:13px;font-weight:bold">Note: R_Freq is the Relative frequency per 1,000 Chinese characters (R_Freq 为每1000字中的相对频度).</span>',unsafe_allow_html=True)
        
        #### 在界面生成92项语言特征原始频度表格
        df92项语言特征_output=df92项语言特征.reset_index()
        df92项语言特征_output=df92项语言特征_output.rename(columns={'index': 'Filenames'})
        df92项语言特征_output=df92项语言特征_output.drop('92.平均句长_词数', axis=1)###去除某一列
#         df92项语言特征_output=df92项语言特征_output.sort_values(by='Filenames',inplace=True,ascending=True)
        #df92项语言特征_output=df92项语言特征_output.drop('特殊重叠式4字词语_频度', axis=1)###去除某一列
        #st.write("df92项语言特征原始频度")
        st.write(df92项语言特征_output, height=200)

        ### 生成AgGrid表格形式： 
        # df92项语言特征1=df92项语言特征.reset_index()
        # df92项语言特征2=df92项语言特征1.rename(columns={'index': 'Filenames'})
        # AgGrid(df92项语言特征2, height=350)

        ### 上述表格用于下载 download
        csv_rawfreq_frame = df92项语言特征_output.to_csv(index=False)
        b64 = base64.b64encode(csv_rawfreq_frame.encode()).decode()
        st.download_button(label='⬇️ Download : Raw Frequency of 92 Linguistic Features', data=csv_rawfreq_frame, file_name='Raw Word Frequency of 92 Linguistic Features.csv', mime='text/csv')



    if st.sidebar.checkbox("Relative Frequency"):
        st.header("Relative Frequency of 92 Linguistic Features")
        #### 在界面生成92项语言特征标准化数据表格
        df92项语言特征标准化数据_output=df92项语言特征标准化数据.reset_index()
        df92项语言特征标准化数据_output=df92项语言特征标准化数据_output.rename(columns={'index': 'Filenames'})
        #df92项语言特征标准化数据_output=df92项语言特征标准化数据_output.drop('特殊重叠式4字词语_频度', axis=1)
#         df92项语言特征标准化数据_output=df92项语言特征标准化数据_output.sort_values(by='Filenames',inplace=True,ascending=True)
        st.write("Relative Frequency is the relative frequency per 1,000 Chinese characters (标准化频率为每1000字中的相对频率).")
        st.write(df92项语言特征标准化数据_output, height=200)

        ### 生成AgGrid表格形式： 
        # df92项语言特征标准化数据1=df92项语言特征标准化数据.reset_index()
        # df92项语言特征标准化数据2=df92项语言特征标准化数据1.rename(columns={'index': 'Filenames'})
        # df92项语言特征标准化数据2=df92项语言特征标准化数据2.round(3)
        # AgGrid(df92项语言特征标准化数据2, height=350)

        ### 上述表格用于下载 download
        csv_rawfreq_frame = df92项语言特征标准化数据_output.to_csv(index=False)
        b64 = base64.b64encode(csv_rawfreq_frame.encode()).decode()
        st.download_button(label='⬇️ Download : Relative Frequency of 92 Linguistic Features', data=csv_rawfreq_frame, file_name='Relative Word Frequency of 92 Linguistic Features.csv', mime='text/csv')

     
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
st.write("------------")

# st.markdown("""
# ###### 　作成者：
# - **徐　勤  (大阪大学 言語文化研究科言語文化専攻)**
# - 公開日：2022年9月5日
# """)

st.markdown("""
######
- **作成者：徐　勤 (大阪大学言語文化研究科)**
- **構築日：2022.03**
- **謝　辞：本プロジェクトは，JST 次世代研究者挑戦的研究プログラム JPMJSP2138 の支援を受けたものである（支援期間：2021.10.01-2023.03.31）。**

""")
## st.write(f'<span style="color:black;font-size:12px">謝　辞：本プロジェクトは，JST 次世代研究者挑戦的研究プログラム JPMJSP2138 の支援を受けたものである（支援期間：2021.10.01-2023.03.31）。</span>',unsafe_allow_html=True)

