import re

def step(url):

    example_url = 'https://thehiddenbay.com/search/killing%20eve/1/99/0'

    m = re.search('\/(\d)\/99\/0$', url)
    page_number = m.group(1)

    string_to_replace = '/' + page_number + '/99/0'
    new_string_end = '/' + str(int(page_number) + 1) + '/99/0'
    new_url = url.replace(string_to_replace, new_string_end)

    return(new_url)


        
        
    