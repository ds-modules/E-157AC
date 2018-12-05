import re

def test_tract(census_tract1, census_tract2, census_tract3, tracts):
    """Checks if census tract is valid.
    :param t: Census tract numbers
    :returns: None"""
    if not census_tract1 in tracts:raise Exception("census_tract1 not a valid census tract" )
    if not census_tract2 in tracts:raise Exception("census_tract2 not a valid census tract" )
    if not census_tract3 in tracts:raise Exception("census_tract3 not a valid census tract" )
    print("success! Keep going with the lab")

def fix_tract(t):
    """Clean up census tract names.
    :param t: Series of string tract names
    :returns: Series of cleaned tract names"""
    p = re.compile('[0-9]{4}.?[0-9]?[0-9]?')
    if p.match(t[13:]) != None:
        return str(p.match(t[13:]).group()).rstrip(",")
    else:
        return str('0000')
