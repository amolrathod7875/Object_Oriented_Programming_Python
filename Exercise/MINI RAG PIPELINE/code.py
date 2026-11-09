class DocumentLoader:
    def __init__(self):
        self.documents = [
            {
                "id":1,
                "content": "Python is a programming language used in AI and machine learning."
            },
            {
                "id":2,
                "content":"Machine Learning enables computer to learn patterns from data"
            },
            {
                "id":3,
                "content":"RAG combines information retrieval with text generation."
            },
            {
                "id":4,
                "content":"Vector databases store and search vector embeddings."
            },
            {
                "id":5,
                "content":"Random Forest is an ensemble machine learning algorithm. "
            }
        ]
    def load(self):
        return self.documents

import re


def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


class Retriever:
    def retrieve(self, question, documents):
        question_words = tokenize(question)
        retrieved_documents = []
        for doc in documents:
            document_words = tokenize(doc["content"])
            common_words = question_words.intersection(document_words)
            if common_words:
                retrieved_documents.append(doc)
        return retrieved_documents

class Reranker:
    def rerank(self, question, retrieved_documents):
        question_words = tokenize(question)
        scored_documents = []
        for doc in retrieved_documents:
            document_words = tokenize(doc["content"])
            score = len(question_words.intersection(document_words))
            scored_documents.append((score, doc))
        scored_documents.sort(
            key=lambda item: item[0],
            reverse=True
        )
        return [doc for score, doc in scored_documents]

class Generator:
    def generate(self, question, context):
        answer = (
            f"Question: {question}\n\n"
            f"Based on the available documents:\n"
            f"{context}"
        )
        return answer

class RAGPipeline:
    def __init__(self, loader, retriever, reranker, generator):
        self.loader = loader
        self.retriever = retriever
        self.reranker = reranker
        self.generator = generator

    def ask(self, question):
        documents = self.loader.load()
        retrieved_docs = self.retriever.retrieve(question, documents)
        if not retrieved_docs:
            return "Sorry, I couldn't find relevant information"
        ranked_docs = self.reranker.rerank(question, retrieved_docs)
        if not ranked_docs:
            return "Sorry, no relevant context is available."
        context = "\n".join(doc["content"] for doc in ranked_docs)
        answer = self.generator.generate(question, context)
        return answer
    
loader = DocumentLoader()
retriever = Retriever()
reranker = Reranker()
generator = Generator()

rag = RAGPipeline(
    loader, retriever, reranker, generator
)

question = "Learning"
answer = rag.ask(question)

print(answer)