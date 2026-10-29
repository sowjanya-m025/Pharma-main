from utils.data_loader import load_json
from langchain_community.llms import Ollama

class PatentAgent:
    def __init__(self):
        self.llm = Ollama(model="llama3")

    def run(self, query):
        data = load_json("mock_patent_data.json")
        prompt = f"Summarize patent expiry, FTO risks, and innovation trends for {query} using {data}"
        return self.llm.invoke(prompt)
