
import os
from dotenv import load_dotenv
from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

load_dotenv()


class ConvertTextToQuery:
    def __init__(self):

        ## initialize
        self.llm = GooglePalm(google_api_key=os.getenv('GOOGLE_API_KEY'), temperature=0.9)
        db_user = os.getenv('db_user')
        db_password = os.getenv('db_password')
        db_host = os.getenv('db_host')
        db_name = os.getenv('db_name')

        self.db_connection = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=3)

    def main(self, query):
        try:

            db_chain = SQLDatabaseChain.from_llm(llm=self.llm, db=self.db_connection, verbose=True, top_k=3)           
            reslut = db_chain.run(query)
            return reslut

        except Exception as error:
            print(error)



if __name__ == "__main__":

    query = "How many t-shirts do we have left for Nike in extra small and white color? If no t-shits match this condition, return `0` "

    query_obj = ConvertTextToQuery()
    print(query_obj.main(query))
