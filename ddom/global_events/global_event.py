
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



CATEGORY_EN = ["window","form","keyboard","mouse","media"]
CATEGORY_CN = ['Window 事件属性', 'Form 事件', 'Keyboard 事件', 'Mouse 事件', 'Media 事件']

CATEGORY_MD = {
    'window': 'Window 事件属性',
    'form': 'Form 事件',
    'keyboard': 'Keyboard 事件',
    'mouse': 'Mouse 事件',
    'media': 'Media 事件',
    'Window 事件属性': 'window',
    'Form 事件': 'form',
    'Keyboard 事件': 'keyboard',
    'Mouse 事件': 'mouse',
    'Media 事件': 'media'
}

URL = "https://www.w3school.com.cn/tags/html_ref_eventattributes.asp"
GLOBAL_EVENTS = {}


def get_global_events():
    res = req.get(URL)
    html_txt = res.text
    root = LXHTML(html_txt)
    ele = engine.xpath(root,"//div[@id='intro']")[0]
    sibs = engine.following_sibs(ele)[:-2]
    global_events = elel.mapv(sibs,engine.xpath,["table"])
    for i in range(len(global_events)):
        tb = global_events[i][0]
        tds = engine.xpath(tb,"tr/td")
        ns = elel.select_interval(tds,3)
        descs = elel.select_interval(tds[2:],3)
        ns = elel.mapv(ns,lambda ele:txt.iter_text(ele).strip(" "))
        descs = elel.mapv(descs,lambda ele:txt.iter_text(ele).strip(" "))
        GLOBAL_EVENTS[CATEGORY_EN[i]] = eded.kvlist2d(ns,descs)
    fs.wjson("global_events.json",GLOBAL_EVENTS)
    return(GLOBAL_EVENTS)


if(__name__=="__main__"):
    get_global_events()
else:
    pass
