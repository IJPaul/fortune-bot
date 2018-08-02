def getPageElements(url, tag, attrs = ""):
    """
    Returns all of the page elements that match specified page element tag and attributes.
    This function is able to by-pass the server security feature of some sites that block known
    spider/bot user agents.

    Parameter url: a valid webapge url
    Precondition: url is a string

    Parameter tag: an element tag on the page
    Precondition: tag is a string

    Parameter attrs: the specified attribut
    Precondition: attrs is a string
    """
    assert isinstance(url, str) and isinstance(tag, str)
    assert isinstance(attrs, str) or isinstance(attrs, dict)
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req).read()
        bsObj = BeautifulSoup(html, 'lxml')
        items = bsObj.findAll(tag, attrs)
        try:
            return items
        except AttributeError:
            print('Attribute error. Are the attributes of that tag valid?')
    except HTTPError:
        print('Http error')
        
    except ValueError:
        print('Value error. Is the url valid?')
        
internalLinks = set()
def getInternalLinks(bsObj, baseURL):
    """
    Returns all internal links for a website.
    
    Parameter bsObj: the website to find all internal links of
    Precondition:BsObj is a BeautifulSoup object
    
    Parameter baseURL: the url that is common to every internal link
    Precondition: baseURL is a string
    """
    # finds all links that begin with '?start='
    for link in bsObj.findAll("a", href=re.compile("^(\?start=)")):
        if link.attrs['href'] is not None:
            if (str(baseURL) + link.attrs['href']) not in internalLinks:
                internalLinks.add(str(baseURL) + link.attrs['href'])
                
                html = urlopen(str(baseURL) + link.attrs['href'])
                bsObj = BeautifulSoup(html, 'lxml')
                getInternalLinks(bsObj, baseURL)
    return internalLinks
