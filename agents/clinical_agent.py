from utils.data_loader import load_json
from langchain_community.llms import Ollama

class ClinicalAgent:
    def __init__(self):
        self.llm = Ollama(model="llama3")

    def run(self, query):
        data = load_json("mock_clinical_data.json")
        prompt = f"List active/completed clinical trials for {query} from {data}"
        return self.llm.invoke(prompt)
