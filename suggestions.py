# もしかして
import sys
from pytrends.request import TrendReq

args = sys.argv

if len(args) != 1:
    keyword = args[1]
else: 
    keyword = 'カフェ'

# hl:言語
# tz:タイムゾーン
pytrends = TrendReq(hl='ja-JP', tz=360)

r = pytrends.suggestions(keyword)

print(r)