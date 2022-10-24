from webinterface import WebInterface
import time

SLEEP_TIME = 10  # seconds


def getAddressFromCorpWiki(wbInt, company_name):
    wbInt.get("https://corporationwiki.com", "#keywords")
    wbInt.execute_script("arguments[0].value= \'\' + arguments[1]", wbInt.getElementById("keywords"), company_name)
    wbInt.execute_script("arguments[0].click()", wbInt.getElementByCSS(".sub-search-handle"))
    result_details = wbInt.getElementById("results-details", True)
    results = wbInt.getChildrenWithCSS(result_details, ".list-group-item", False)
    for i in range(len(results)):
        link = wbInt.getChildWithTag(wbInt.getChildWithTag(wbInt.getChildWithCSS(results[i], ".row"), "div"), "a")
        if link.text.strip().lower().replace(',', '').replace('.', '') == company_name.lower().replace(',', '').replace(
                '.', ''):
            wbInt.get(link.get_attribute('href'), "h2")
            title_h2 = wbInt.getElementByCSS("h2")
            p_tag = None
            p_tags = wbInt.getChildrenWithCSS(title_h2.find_element_by_xpath(".."), "p", False)
            if len(p_tags) > 1:
                p_tag = p_tags[1]
            if p_tag is None or not "no longer active" in \
                                    wbInt.getChildrenWithCSS(title_h2.find_element_by_xpath(".."), "p", False)[1].text:
                addr = wbInt.getElementByAttribute('span', 'itemprop', 'address', False)
                if not addr is None:
                    toRet = []

                    st_addr = wbInt.getChildWithAttribute(addr, 'span', 'itemprop', 'streetAddress', False)
                    if not st_addr is None:
                        toRet.append(st_addr.text)
                    else:
                        return None

                    add_local = wbInt.getChildWithAttribute(addr, 'span', 'itemprop', 'addressLocality', False)
                    if not st_addr is None:
                        toRet.append(add_local.text)
                    else:
                        return None

                    add_reg = wbInt.getChildWithAttribute(addr, 'span', 'itemprop', 'addressRegion', False)
                    if not add_reg is None:
                        toRet.append(add_reg.text)
                    else:
                        return None

                    ps_code = wbInt.getChildWithAttribute(addr, 'span', 'itemprop', 'postalCode', False)
                    if not ps_code is None:
                        toRet.append(ps_code.text)
                    else:
                        return None
                    toRet.insert(0, 'Corporation Wiki')
                    return toRet
            time.sleep(SLEEP_TIME)
            wbInt.execute_script("window.history.go(-1)")
            result_details = wbInt.getElementById("results-details", True)
            results = wbInt.getChildrenWithCSS(result_details, ".list-group-item", False)
    return None


def getAddressesFromCorpWiki(company_names, indices, addresses):
    wbInt = WebInterface()
    lastIn = -1

    for i in range(len(addresses) - 1, 0, -1):
        if not addresses[i] is None:
            if addresses[i][0] == 'Corporation Wiki':
                lastIn = i;
                break;

    for i in indices:
        if i <= lastIn: continue
        while True:
            try:
                addresses[i] = getAddressFromCorpWiki(wbInt, company_names[i])
                print(addresses[i])
                break
            except:
                print("Problematic Search: Corporation Wiki, " + company_names[i] + ", Retrying")
                import traceback
                traceback.print_exc()
    wbInt.close()
    wbInt.quit()


def test():
    company_names = ['Aj & Sons Transportation Inc']
    addresses = [0]
    getAddressesFromCorpWiki(company_names, [0], addresses)
    for address in addresses:
        print(address)


if __name__ == "__main__":
    test()
