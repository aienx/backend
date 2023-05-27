import pyshorteners
from decouple import config

#Bitly shortener service
type_bitly = pyshorteners.Shortener(api_key= config("BITLY_TOKEN"))

def reduce(url):
    return type_bitly.bitly.short(url)
 
