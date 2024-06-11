examples = [
    {
        "input": "List all brokers.",
        "query": "SELECT * FROM Broker;"
    },
    {
        "input": "Get details of a specific property type.",
        "query": "SELECT * FROM PropertyType WHERE type_name = 'Apartment';"
    },
    {
        "input": "Retrieve all properties with a price greater than $500,000.",
        "query": "SELECT * FROM Property WHERE price > 500000;"
    },
    {
        "input": "Show details of properties located in a specific city.",
        "query": "SELECT * FROM Property WHERE locality = 'New York';"
    },
    {
        "input": "List all addresses with their corresponding latitude and longitude.",
        "query": "SELECT main_address, latitude, longitude FROM Address;"
    },
    {
        "input": "Get the total number of properties listed by a specific broker.",
        "query": "SELECT COUNT(*) FROM Property WHERE broker_id = 1; -- Assuming 1 is the broker_id of the desired broker"
    },
    {
        "input": "Find the average price of properties in a specific locality.",
        "query": "SELECT AVG(price) FROM Property WHERE locality = 'Los Angeles';"
    },
    {
        "input": "Retrieve the full name and contact details of brokers associated with a specific agency.",
        "query": "SELECT p.full_name, p.email, b.broker_title FROM Broker b JOIN Property p ON b.broker_id = p.broker_id WHERE b.agcyid = 1; -- Assuming 1 is the agency identifier"
    }
]

from langchain_community.vectorstores import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings
import streamlit as st

@st.cache_resource
def get_example_selector():
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        examples,
        OpenAIEmbeddings(),
        Chroma,
        k=3,
        input_keys=["input"],
    )
    return example_selector