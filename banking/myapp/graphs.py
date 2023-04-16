import matplotlib.pyplot as plt
import numpy as np
import io
import urllib , base64
def pieChart(p1,p2):
    x = np.array([p1, p2])
    print(x)
    labels = np.array(["Deposit", "Withdrawl"])
    myexplode = [0.2, 0]
    plt.pie(x, labels = labels, explode = myexplode)
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf , format = "png")
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return uri

def barChart(p1,p2):
    x = np.array([p1, p2])
    print(x)
    labels = np.array(["Deposit", "Withdrawl"])
    barGraph = plt.figure(1)
    plt.bar(labels, x)
    fig1 = plt.gcf()
    buf1 = io.BytesIO()
    fig1.savefig(buf1 , format = "jpg")
    buf1.seek(0)
    string1 = base64.b64encode(buf1.read())
    uri1 = urllib.parse.quote(string1)
    
    return uri1