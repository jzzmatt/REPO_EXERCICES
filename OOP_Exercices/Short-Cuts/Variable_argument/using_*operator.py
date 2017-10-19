'''
For example a fuction that accept a link or list of links
Download the web pages
'''

def get_pages(*links):
    '''
    The *links will accept any number of arguments and put them all in a lst
    :param links: 
    :return: 
    '''
    for link in links:
        #download the link with urlib
        print(link)



get_pages()
get_pages('http://www.archlinux.org')
get_pages('http://www.archlinux.org', 'http://ccphillips.net/')




