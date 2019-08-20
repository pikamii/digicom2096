import sys
from pytrends.request import TrendReq

pytrends = TrendReq(hl='ja-JP', tz=360)

r = pytrends.related_queries()

print(r)
