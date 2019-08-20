import elist.elist as elel

def s2d(s,sp=" "):
    s = s.strip("\n")
    lines = s.split("\n")
    tl = elel.mapv(lines,lambda line:tuple(line.split(sp)))
    d = eded.tlist2dict(tl)
    return(d)