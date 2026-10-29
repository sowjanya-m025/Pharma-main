from langchain_community.llms import Ollama

class InternalAgent:
    def __init__(self):
        self.llm = Ollama(model="llama3")

    def run(self, query):
        prompt = f"Summarize key takeaways from internal documents for {query}."
        return self.llm.invoke(prompt)
