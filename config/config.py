#!/usr/bin/python
from configparser import ConfigParser
 
def get_config(filename='config/config.ini', section='default'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default 
    conf = {}
    
    # Checks to see if section (default) parser exists
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            conf[param[0].upper()] = param[1]
         
    # Returns an error if a parameter is called that is not listed in the initialization file
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return conf

