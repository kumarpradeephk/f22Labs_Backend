import urllib.request
import json
r = urllib.request.urlopen("https://gist.githubusercontent.com/murtuzakz/4bd887712703ff14c9b0f7c18229b332/raw/d0dd1c59016e2488dcbe0c8e710a1c5df9c3672e/season7.json")
rjson = json.loads(r.read())


investor_to_product = {}

for key in rjson.keys():
	for json1 in rjson[key]:
		invest = json1['investors']
		product = json1['product']
		product = product.replace('\n','')
		#process invest
		invest_list = invest.replace(',',' and ').split(' and ')

		for invest1 in invest_list:
			invest1 = invest1.strip()
			invest1 = invest1.replace('\n','').replace('O\u2019','').replace('  ',' ')
			if invest1 not in investor_to_product.keys() and invest1 != '':
				investor_to_product[invest1] = []
			if invest1!='':
				investor_to_product[invest1].append(product)

dict_items = sorted(investor_to_product.items(),key=lambda x:len(x[1]))
i=1
for k,v in dict_items:
    print(str(i)+". "+k+" : "+str(v)+"\n")
    i=i+1
