
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()  
        self.retriever = retriever

    def get_recommendation(self, query: str):
        docs = self.retriever.invoke(query)
        context = "\n".join([doc.page_content for doc in docs])
        prompt_text = self.prompt.format(context=context, question=query)
        result = self.llm.invoke(prompt_text)
        return result.content