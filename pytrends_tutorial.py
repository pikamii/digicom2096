import sys
from pytrends.request import TrendReq

args = sys.argv

if len(args) != 1:
    kw_list = args[1:]
else: 
    kw_list = ["Java","Python","JavaScript"]

pytrends = TrendReq(hl='ja-JP', tz=360)
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='JP', gprop='')

# Trending Searches
# pytrends.trending_searches(pn='united_states') # trending searches in real time for United States
# pytrends.trending_searches(pn='japan') # Japan

r = pytrends.related_queries()

print(r)

