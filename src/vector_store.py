from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader

from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

class VectorStoreBuilder:
    def __init__(self,csv_path:str,persist_dir:str="chroma_db"):
        self.csv_path=csv_path
        self.persist_dir=persist_dir
        self.embedding=HuggingFaceEmbeddings(model_name="")

