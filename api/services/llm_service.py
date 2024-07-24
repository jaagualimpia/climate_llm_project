class LLMService():
        def __init__(self):
            self.llm = LLM()
        
        def get_response(self, query):
            return self.llm.get_response(query)