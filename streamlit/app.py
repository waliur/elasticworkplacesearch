import streamlit as st
from elasticsearch import Elasticsearch

# Configure Elasticsearch with network drive connector
from elasticsearch import Elasticsearch

# Initialize Elasticsearch with appropriate scheme, host, and port
es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200, 'scheme': 'http'}])

st.title("Search App")

# Search box
query = st.text_input("Enter search query") 

if query:
   # Search using drive connector
   res = es.search(index="folder-a", body={"query": {"query_string": {"query": query}}})  

   # Display results
   for hit in res['hits']['hits']: 
      st.write(hit["_source"])
