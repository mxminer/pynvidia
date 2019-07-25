# encoding utf-8

import os
import xmltodict
from collections import OrderedDict
'''
读取linux中的gpu配置文件转化为json
stdout = os.popen("nvidia-smi -q -x")
content = stdout.read()
convertJson = xmltodict.parse(content, encoding='utf-8')

'''


def xmltojson(xml):

    try:
        convertJson = xmltodict.parse(xml, encoding='utf-8')
        return convertJson

    except Exception:
        print('Error')



def ToJson(orderdict):

    NList = ['product_name','product_brand','accounting_mode_buffer_size','uuid',
             'fb_memory_usage','temperature','fan_speed','power_readings']

    for k,v in orderdict.items():
        GpuList=[]

        if type(v) == OrderedDict:
            for a,b in v.items():
                # NumberGpu = len(b)
                if type(b) == list:
                    for c in b:
                        # print (c)
                        if type(c) == OrderedDict:
                            for d,e in c.items():
                                if d in NList:
                                    # 构建一个存放显卡信息的字典
                                    f = {d:e}

                                    # 将这个字典append到list去
                                    GpuList.append(f)
        return GpuList



def GetGpuInfo():
    stdout = os.popen("nvidia-smi -q -x")
    content = stdout.read()
    x = xmltojson(content)
    x = ToJson(x)
    return x






if __name__ =="__main__":

    x = GetGpuInfo()
    print(x)

    # stdout = os.popen("nvidia-smi -q -x")
    # content = stdout.read()
    # x = xmltojson(content)
    # x = ToJson(x)
    # print(x)