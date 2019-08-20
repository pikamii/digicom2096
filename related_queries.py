import sys
from pytrends.request import TrendReq

args = sys.argv

if len(args) != 1:
    kw_list = args[1:]
else: 
    kw_list = ["カフェ","現代アート"]

pytrends = TrendReq(hl='ja-JP', tz=360)
pytrends.build_payload(kw_list, cat=23, timeframe='today 5-y', geo='JP', gprop='')

r = pytrends.related_queries()

print(r)
