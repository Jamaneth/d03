import requests
import json
import dewiki
import sys

def wikipedia_query(query):

    #file = open(query + '.html', 'w')
    api_url = 'https://en.wikipedia.org/w/api.php?action=parse&format=json&prop=wikitext&redirects=True&page=' + query
    try:
        r = requests.get(api_url)
        if r.status_code != 200:
            raise Exception('HTTP Error ' + str(r.status_code))
    except:
        raise Exception('Connection not found')


    json_result = r.json()

    try:
        return json_result['parse']['wikitext']['*']
    except KeyError:
        raise Exception('Error: the page does not exist.')

    #file.write(r.text)


    #return r.text


def text_cleaner(wiki_text):
    unmarked_text = dewiki.from_string(wiki_text) # Remove Wiki markup
    clean_text = ''.join(unmarked_text.split('}}')[1:]) # Remove weird introduction thing
    return clean_text


def file_writer(query, clean_text):
    file = open(query + '.wiki', 'w')
    file.write(clean_text)


def wiki_argument():

    if len(sys.argv) == 2:
        query = sys.argv[1]
    else:
        raise Exception('Wrong number of arguments (exactly one argument needed).')

    if ' ' in query:
        raise Exception('No white space in the query.')

    return query

if __name__ == '__main__':
    #print(wikipedia_query('Chocolatine'))
    query = wiki_argument()
    api_result = wikipedia_query(query)
    clean_text = text_cleaner(api_result)
    file_writer(query, clean_text)
    #print(clean_text)
    #print(api_result)
