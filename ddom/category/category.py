
import requests as req

from lxml.etree import HTML as LXHTML
from lxml.etree import XML as LXML
from xdict.jprint import pdir,pobj
from nvhtml import txt
from nvhtml import lvsrch
from nvhtml import fs
from nvhtml import engine
from nvhtml import utils
import lxml.sax
import argparse
from efdir import fs
import elist.elist as elel
import estring.estring as eses
import edict.edict as eded
import spaint.spaint as spaint
from xml.sax.handler import ContentHandler

import copy
import re



CATEGORY_EN = ["basic","format","form","frame","img","auvi","link","list","table","style","meta","script"]
CATEGORY_CN = ['基础', '格式', '表单', '框架', '图像', '音频/视频', '链接', '列表', '表格', '样式/节', '元信息', '编程']

CATEGORY_MD = {
    'basic': '基础',
    'format': '格式',
    'form': '表单',
    'frame': '框架',
    'img': '图像',
    'auvi': '音频/视频',
    'link': '链接',
    'list': '列表',
    'table': '表格',
    'style': '样式/节',
    'meta': '元信息',
    'script': '编程',
    '基础': 'basic',
    '格式': 'format',
    '表单': 'form',
    '框架': 'frame',
    '图像': 'img',
    '音频/视频': 'auvi',
    '链接': 'link',
    '列表': 'list',
    '表格': 'table',
    '样式/节': 'style',
    '元信息': 'meta',
    '编程': 'script'
}

URL = "https://www.w3school.com.cn/tags/html_ref_byfunc.asp"
CATES = {}


def get_cates():
    res = req.get(URL)
    html_txt = res.text
    root = LXHTML(html_txt)
    cates = engine.xpath(root,"//h3")
    for i in range(len(cates)):
        nd = cates[i]
        cate = CATEGORY_MD[nd.text]
        tb = engine.rsib(nd)
        a = engine.xpath(tb,"tr/td/a")
        tags = elel.mapv(a,lambda ele:ele.text[1:-1])
        ntags = []
        for tag in tags:
            if(tag == "!DOCTYPE"):
                tag = "<doctype>"
                ntags.append(tag)
            elif(tag == "!--...--"):
                tag = "<comment>"
                ntags.append(tag)
            elif(tag == 'h1> to <h6'):
                arr = ["h1","h2","h3","h4","h5","h6"]
                ntags.extend(arr)
            else:
                ntags.append(tag)
        CATES[cate] = ntags
    fs.rjson("category.json",CATES)
    return(CATES)


if(__name__=="__main__"):
    get_cates()
else:
    pass