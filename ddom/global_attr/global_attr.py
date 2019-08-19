
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

import xxurl.xxurl as xuxu


GLOBAL_ATTRS = {}

URL = "https://www.w3school.com.cn/tags/html_ref_standardattributes.asp"


def new_entry():
    d = {
        "cn_desc":"",
        "values" : []
    }
    return(d)


def get_values(attr_url):
    res = req.get(attr_url)
    html_txt = res.text
    root = LXHTML(html_txt)
    nd = engine.xpath(root,'//h3')[0]
    nd = engine.rsib(nd)
    values = engine.xpath(nd,"tr/td")
    values = elel.select_evens(values)
    nvalues = []
    for i in range(len(values)):
        val = values[i]
        child = engine.child(val,0)
        if(child == None):
            nvalues.append(val.text)
        elif(child.tag ==  "i"):
            nvalues.append("_"+child.text)
        else:
            pass
    return(nvalues)

def get_global_attrs():
    res = req.get(URL)
    html_txt = res.text
    root = LXHTML(html_txt)
    nd = engine.xpath(root,'//p[@class="html5_new_note"]')[0]
    nd = engine.rsib(nd)
    attrs = engine.xpath(nd,"tr/td/a")
    for i in range(len(attrs)):
        nd = attrs[i]
        attr_name = nd.text
        attr_url = xuxu.get_abs_url(URL,nd.attrib['href'])
        nd = engine.parent(nd)
        cn_desc  = engine.rsib(nd).text
        d = new_entry()
        values = get_values(attr_url)
        d['cn_desc'] = cn_desc
        d['values'] = values
        GLOBAL_ATTRS[attr_name] = d
    fs.rjson("global_attrs.json",GLOBAL_ATTRS)
    return(GLOBAL_ATTRS)


if(__name__=="__main__"):
    get_global_attrs()
else:
    pass