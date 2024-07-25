from api.repositories.llm_repository import LLMRepository


class LLMService():
        def __init__(self):
            self.__llm_repository = LLMRepository()
        
        def get_response(self, query):
            return self.__llm_repository.get_response(query)