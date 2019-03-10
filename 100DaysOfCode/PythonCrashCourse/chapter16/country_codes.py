from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""

    for code, name in COUNTRIES.items():
        if country_name == 'Yemen, Rep.':
            return 'ye'
        elif name == country_name:
            return code
    # if the country wasn't found, return None.
    return None

#print(get_country_code('Andorra'))
#print(get_country_code('United Arab Emirates'))
#print(get_country_code('Yemen, Rep.'))
