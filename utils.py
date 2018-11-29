import pandas as pd

def limit_decimal(value, n=7):
    tmp="0:.{}f".format(n)
    tmp = '{'+tmp+'}'
    return float(tmp.format(value))

def array_to_dict(f,x,n):
    t={}
    for i in range(0,n):
        t[x[i]]=limit_decimal(f(x[i]))
    return t

def print_dict(t):
    keys = list(t.keys())
    data = []
    for i in range(len(t)):
        data.append(t[keys[i]])
    return pd.DataFrame([keys,data])

def print_array(data, columns=None):
    return pd.DataFrame(data, columns)

