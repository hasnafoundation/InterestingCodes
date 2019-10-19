
from wikipedia_search import WikipediaSearch

ws = WikipediaSearch()
#exception case
#print(ws.brief_search("fsfsfsfs").get_result())
print(ws.brief_search("Jimi Hendrix"))
print(ws.brief_search("Nikola Tesla"))
ws.set_language("fr")
print(ws.brief_search("Thomas Edison"))
#assertion error
#print(ws.brief_search("Nikola Tesla", sentences=11))

