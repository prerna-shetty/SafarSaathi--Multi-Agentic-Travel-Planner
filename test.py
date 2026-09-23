
#from tools.tavily import tavily_search 
from tools.flight import search_flights
res=search_flights("Plan 7 day nepal trip from bangladesh")
print(res)