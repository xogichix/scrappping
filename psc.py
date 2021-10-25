import requests	
from bs4 import BeautifulSoup	
import pprint
from math import ceil
res=requests.get('https://ssc.nic.in/ApplicationForm/ValidateConstableGDForm')
soup=BeautifulSoup(res.text,'html.parser')
item= soup.tbody.select('span')
def test(links):
    title=[]
    for i,item in enumerate(links):
            title.append(item.getText())
    title.remove('Stock split')
    return my_reshape(title,6)

def my_reshape(arr, cols):
    rows = ceil(len(arr) / cols)
    res = []
    for row in range(rows):
        current_row = []
        for col in range(cols):
            arr_idx = row * cols + col
            if arr_idx < len(arr):
                current_row.append(arr[arr_idx])
            else:
                current_row.append(None)
        res.append(current_row)
    return res
print(test(item))

