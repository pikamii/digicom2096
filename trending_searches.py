import sys
from pytrends.request import TrendReq

args = sys.argv

if len(args) != 1:
    area = args[1:]
else: 
    area = 'japan'

# hl:言語
# tz:タイムゾーン
pytrends = TrendReq(hl='ja-JP', tz=360)

r = pytrends.trending_searches(pn=area)

print(r)
