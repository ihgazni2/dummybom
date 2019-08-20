
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


def s2d(s,sp="@"):
    s = s.strip("\n")
    lines = s.split("\n")
    tl = elel.mapv(lines,lambda line:tuple(line.split(sp)))
    d = eded.tlist2dict(tl)
    for k in d:
        v = d[k]
        d[k]  = {}
        d[k]['cn_desc'] = v
        d[k]['return'] = {
            "cn_desc":"",
            "values":[
            ]
        }
    return(d)


