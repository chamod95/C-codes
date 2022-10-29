from webinterface import WebInterface
import urllib
import time

SLEEP_TIME = 10 # stop for 10 seconds

def getAddressFromCortera(wbInt, company_name):
	pg_no = 1
	while pg_no <= 3:
		if pg_no == 1:
			querystring = urllib.parse.urlencode({'q': 'site:cortera.com "' + company_name + '"'})
			wbInt.get('https://www.bing.com/search?' + querystring, 'input[class="b_searchbox"]')
		else:
			next_page_button = wbInt.getElementByAttribute("a", "aria-label", "Page " + str(pg_no), False)
			if not next_page_button is None:
				wbInt.execute_script("arguments[0].click();", next_page_button)
				while wbInt.getElementByAttribute("a", "aria-label", "Page " + str(pg_no), False) is not None:
					pass
			else:
				break
		el = wbInt.getElementById("b_results", False)
		if el is None:	
			return None
		search_results = wbInt.getChildrenWithCSS(el, ".b_algo", False)
		i = 0
		while i < len(search_results):
			result = search_results[i]
			h2elem = wbInt.getChildWithCSS(result, "h2")
			link = wbInt.getChildWithTag(h2elem, "a")
			title = link.text
			if company_name.lower().replace(',', '').replace('.', '') in title.lower().replace(',', '').replace('.', ''):
				wbInt.get(link.get_attribute("href"), 'span[itemprop="name"]')
				if wbInt.getElementByAttribute("span", "itemprop", "name").text.lower().replace(',', '').replace('.', '') == company_name.lower().replace(',', '').replace('.', ''):
					return ['Cortera', wbInt.getElementByAttribute("div", "itemprop", "streetAddress").text,
					wbInt.getElementByAttribute("span", "itemprop", "addressLocality").text,
					wbInt.getElementByAttribute("span", "itemprop", "addressRegion").text,
					wbInt.getElementByAttribute("span", "itemprop", "postalCode").text]
				wbInt.execute_script("window.history.go(-1)")
				search_results = wbInt.getChildrenWithCSS(wbInt.getElementById("b_results"), ".g")
			i+=1
		pg_no += 1
		time.sleep(SLEEP_TIME)
	return None

def getAddressesFromCortera(company_names, indices, addresses):
	wbInt = WebInterface()
	lastIn = -1
	for i in range(len(addresses)-1, 0, -1):
		if not addresses[i] is None:
			if addresses[i][0] == 'Cortera':
				lastIn = i;
				break;
			if addresses[i][0] in ['Corporation Wiki']:
				lastIn = indices[-1]
				break
	
	for i in indices:
		if i <= lastIn: continue
		while True:
			try:
				addresses[i] = getAddressFromCortera(wbInt, company_names[i])
				time.sleep(SLEEP_TIME)
				print(addresses[i])
				break
			except:
				print("Problematic Search: Cortera, " + company_names[i] + ", retrying")
				import traceback
				traceback.print_exc()
	wbInt.close()
	wbInt.quit()
	
if __name__=="__main__":
	company_names = ['More Wine Inc']
	addresses = [None, None]
	getAddressesFromCortera(company_names, [0], addresses)
	for company in addresses:
		print(company)