import requests 
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://ssc.nic.in/ApplicationForm/ValidateConstableGDForm')
soup = BeautifulSoup(res.text, 'html.parser') 
subtext=soup.select('.subtext')
links= soup.select('.storylink')

def sor(hnli):
	return sorted(hnli , key= lambda k:k['score'], reverse= True)

def test(subtext , links):
	hn=[]
	for idx,item in enumerate(links):
		title= item.getText()
		href=item.get('href', None)
		score= subtext[idx].select('.score')
		if len(score):
			point= int(score[0].getText().replace(' points',''))
			if point >99:
				hn.append({'title' : title ,'links':href, 'score':point})
	return sor(hn)

pprint.pprint(test(subtext, links))