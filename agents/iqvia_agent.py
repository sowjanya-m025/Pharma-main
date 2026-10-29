from utils.data_loader import load_json
from langchain_community.llms import Ollama

class IQVIAAgent:
    def __init__(self):
        self.llm = Ollama(model="llama3")

    def run(self, query):
        data = load_json("mock_market_data.json")
        prompt = f"""
        You are a pharma market analyst. Using this data: {data},
        summarize market size, CAGR, and competitive intensity for query: {query}.
        """
        return self.llm.invoke(prompt)
