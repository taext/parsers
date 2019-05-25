import requests, re, collections, itertools

def run(search_term, count=30):
    """Takes thehiddenbay.com torrent search, 
    returns 30 item result list and dictionary. 
    Also includes unused page stepper function."""

    example_url = 'https://thehiddenbay.com/search/killing%20eve/1/99/0'
    new_search_term = search_term.replace(' ', '%20')
    new_url = example_url.replace('killing%20eve', new_search_term)
    torrent_list = []
    torrent_dict = collections.OrderedDict()
    while len(torrent_list) <= count: 

        r = requests.get(new_url)
        # get magnet links
        magnet_match = re.findall('href\=\"(magnet.+?)\"', r.text)
        # get torrent page links
        torrent_match = re.findall('href\=\"(https.+?torrent.+?)\"', r.text)
        # get titles
        title_match = re.findall('title\=\"Details for.+?">(.+?)<', r.text)
        # get upload date
        upload_date_match = re.findall('Uploaded (\S+)', r.text)
        # get torrent size
        size_match = re.findall('Size (\S+)', r.text)
        # get torrent category
        category_match = re.findall('category\">(.+?)<', r.text)[1::2]
        
        
        for i, item in enumerate(magnet_match):
            #print(f'category: {category_match[i]}')  # delete_me
            torrent_title = title_match[i]
            torrent_magnet = magnet_match[i]
            torrent_page = torrent_match[i]
            temp_date = upload_date_match[i]
            torrent_date = temp_date.replace('&nbsp;',' ')[:-1]
            temp_size = size_match[i].replace('&nbsp;',' ')[:-1]
            torrent_size = temp_size.replace('&nbsp;',' ')[:-1]
            torrent_category = category_match[i]
            Torrent = collections.namedtuple('Torrent', ' title magnet_link torrent_page_link torrent_date torrent_size torrent_category')
            torrentOfTheLoop = Torrent(title=torrent_title, 
                                magnet_link=torrent_magnet, 
                                torrent_page_link=torrent_page, 
                                torrent_date=torrent_date, 
                                torrent_size=torrent_size,
                                torrent_category=torrent_category)
            torrent_list.append(torrentOfTheLoop)
            torrent_dict[torrent_title] = torrentOfTheLoop
        
        new_url = step(new_url)
    
    truncated_list = torrent_list[:count]
    
    to_remove = list(torrent_dict.keys())[count:] # slice off first 500 keys
    for key in to_remove:
        del torrent_dict[key]

    return(truncated_list, torrent_dict)


def step(url):

    example_url = 'https://thehiddenbay.com/search/killing%20eve/1/99/0'

    m = re.search('\/(\d+)\/99\/0$', url)
    page_number = m.group(1)

    string_to_replace = '/' + page_number + '/99/0'
    new_string_end = '/' + str(int(page_number) + 1) + '/99/0'
    new_url = url.replace(string_to_replace, new_string_end)

    return(new_url)
        
    