from ..math import Vec2, Vec3, Vec4, Mat4

try:
    from IPython.display import Markdown as show
    g_hasIPython = True
except:
    g_hasIPython = False

def tolatex(v, delim=""):
    """Pretty print Vec2, Vec3, Vec4, Mat4 as LaTeX expression"""
    if type(v) is Vec2:
        return "%s\\begin{pmatrix}%s\\\\%s\\end{pmatrix}%s" % (delim,str(v.x),str(v.y),delim)
    elif type(v) is Vec3:
        return "%s\\begin{pmatrix}%s\\\\%s\\\\%s\\end{pmatrix}%s" % (delim,str(v.x),str(v.y),str(v.z),delim)
    elif type(v) is Vec4:
        return "%s\\begin{pmatrix}%s\\\\%s\\\\%s\\\\%s\\end{pmatrix}%s" % (delim,str(v.x),str(v.y),str(v.z),str(v.w),delim)
    elif type(v) is Mat4:
        return "%s\\begin{pmatrix}%s\\end{pmatrix}%s" % (delim,'\\\\'.join(['&'.join([str(v[i,j]) for i in range(4)]) for j in range(4)]),delim)
    else:
        return None

def tomd(v):
    """Markdown representation of value v"""
    if type(v) is tuple:
        return " ".join([tomd(x) for x in v])
    elif type(v) is list:
        return ", ".join([tomd(x) for x in v])
    else:
        return tolatex(v,'$') or str(v)

def bullet(l):
    """Markdown bullet list representation of l elements"""
    return "\n".join(["* %s" % tomd(v) for v in l])

