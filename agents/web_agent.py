from langchain_community.llms import Ollama

class WebAgent:
    def __init__(self):
        self.llm = Ollama(model="llama3")

    def run(self, query):
        prompt = f"Search simulated web for recent guidelines or news about {query} and summarize key insights."
        return self.llm.invoke(prompt)
