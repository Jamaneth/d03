import requests
from bs4 import BeautifulSoup
import sys

def wiki_argument():

    if len(sys.argv) == 2:
        query = sys.argv[1]
    else:
        raise Exception('Wrong number of arguments (exactly one argument needed)')

    #if ' ' in query:
    #    query = query.replace(' ', '_')

    return query


def page_content(address):

    try:
        r = requests.get(address)
        if r.status_code != 200:
            raise Exception('HTTP Error ' + str(r.status_code))

    except:
        raise Exception('Connection not found')

    return r.content


def intro_finder(content):

    soup = BeautifulSoup(content, "lxml")
    #full_article_content = soup.findAll("div", {"class": "mw-parser-output"})
    article_content = soup.findAll(["p", "h2"])
    intro_content = []
    links = []
    for paragraph in article_content:
        if str(paragraph)[0:4] != '<h2>':
            intro_content += [paragraph]
        else:
            break

    return intro_content


def link_getter(introduction):

    links = []

    for paragraph in introduction:
        links += [a['href'] for a in paragraph('a', href=True) if a.text \
        and '/wiki/' in a['href'] and '/Help:' not in a['href'] and '/Portal:' not in a['href']]

    return links


def next_link(wiki_address):

    raw_content = page_content(wiki_address)
    intro_content = intro_finder(raw_content)
    links = link_getter(intro_content)

    if len(links) > 0:
        return 'https://en.wikipedia.org' + links[0]
    else:
        return False


def link_finder():

    query = wiki_argument()
    print(query)

    address_list = ['https://en.wikipedia.org/wiki/' + query]


    while address_list[-1] != "https://en.wikipedia.org/wiki/Philosophy":

        #print(address_list[-1])
        new_address = next_link(address_list[-1])

        if new_address == False:
            print("It leads to a dead end!")
            break

        else:
            article_title = new_address.split('/')[-1].replace('_', ' ')
            print(article_title)

            if new_address in address_list:
                print("It leads to an infinite loop!")
                break
            else:
                address_list.append(new_address)

    else:
        print('%d roads from %s to philosophy!' % (len(address_list), query))



if __name__ == '__main__':

    #wiki_page = wiki_argument()
    #raw_content = page_content(wiki_page)
    #intro_content = intro_finder(raw_content)
    #links = link_getter(intro_content)
    #print(links)
    link_finder()
