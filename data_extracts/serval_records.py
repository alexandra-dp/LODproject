import requests

# open file with list of identifiers

filename = input('Enter identifiers file name (full path): ')
f = open(filename)

# generate list of OAI getRecord urls

base_url = 'https://serval.unil.ch/oaiprovider?verb=GetRecord&metadataPrefix=mods&identifier=oai:serval.unil.ch:'

urls = []

for i in f:
    r = requests.get(f'{base_url}{i.strip()}')  # strip spaces and new lines around the identifiers
    url = r.url
    urls.append(url)

    # generate one file per request call

    for url in urls:
        content = r.content
        url_list = url.split(':')  # create a new list with every element of the url using : as separator
        id_list = url_list[-1:]  # create a new list with the last item in the url_list i.e. the identifier
        id_str = ''  # initialise an empty string

        for identifier in id_list:  # loop through list items to append to id_str
            id_str += identifier   # work around to convert identifier as list to identifier as str

        # save content to file named by the identifier
        with open(id_str + '.xml', 'wb') as f2:
            f2.write(content)
