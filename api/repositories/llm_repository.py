from langchain_openai import ChatOpenAI
import os
class LLMRepository():

    def __init__(self):
        self._llm = ChatOpenAI(
            model=os.environ.get("OPENAI_MODEL"),
            temperature=1,
            max_tokens=1000,
            timeout=None,
            max_retries=2,
        )

    def __get_query_template(self, query):
        messages = [
        (
            "system",
            """You are an expert on the climate of the Colombian pacific region and you're going to be consulted about
              some data an recommendations int the topic as the expert you are. You need to be capable of mantain a accurate but 
              easy to follow conversation with the user. It is allowed for you to give some predictions only if you are sure about them. If not
              you can always ask for more information. You must answer in the user language and be polite and respectful at all times.""",
        ),
        ("human", f"{query}"),]
        
        return messages

    def get_response(self, query):
        return self._llm.invoke(self.__get_query_template(query))