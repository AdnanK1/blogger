import urllib.request,json
from .models import RandomQuotes

#Get base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['RANDOM_BASE_URL']

def get_random_quote():
    get_quote_url = base_url

    with urllib.request.urlopen(get_quote_url) as url:
        get_data = url.read()
        get_response = json.loads(get_data)

        quote_results = None
        if get_response['quotes']:
            results_list = get_response['quotes']
            results = process_results(results_list)
    return results

def process_results(quote_list):
    results = []
    for quote_item in quote_list:
        author = quote_item.get('author')
        id = quote_item.get('id')
        quote = quote_item.get('quote')
        permalink = quote_item.get('permalink')

        new_object = RandomQuotes(author,id,quote,permalink)
        results.append(new_object)
    return results