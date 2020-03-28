from googleapiclient.discovery import build   #Import the library
from Data_storage import database_obj


class Util(object):
    """ Util Class to get the result from google and to store the keyword for
        search history"""
    def __init__(self):
        # database object to store searched keyword
        self.db_obj = database_obj

    # fetching result as per query from google using google search engine api
    def google_query(self, query, api_key, cse_id, **kwargs):
        # storing the search keyword passed with !google
        try:
            self.db_obj.insert_values(query)
            query_service = build("customsearch",
                                  "v1",
                                  developerKey=api_key
                                  )
            query_results = query_service.cse().list(q=query,    # Query
                                                     cx=cse_id,  # CSE ID
                                                     **kwargs
                                                     ).execute()
        except Exception as e:
            print(e)

        if 'items' not in query_results.keys():
            query_results['items'] = -1

        return query_results['items']

    # fetching the search history of google based on the query
    def search_query(self, query):
        # fetching the stored value from
        flag = 0
        try:
            res = self.db_obj.fetch_value()
            res_out = []
            # matching the keyword passed with !recent
            for i in range(0, len(res)):
                if query in res[i][0]:
                    res_out.append(res[i][0])
                    flag = 1
                    print(res[i][0])
            if flag == 0:
                res_out.append("No Match Found with this keyword")

        except Exception as e:
            print(e)
            res_out = ['No match found']
        return res_out


