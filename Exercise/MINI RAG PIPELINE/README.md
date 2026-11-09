# Mini RAG Pipeline (Mock Version)

## Overview

This exercise demonstrates **composition**, **interfaces**, **dependency injection**, and **modularity** in Python by building a small mock Retrieval-Augmented Generation (RAG) pipeline. Each stage is a separate component (`DocumentLoader`, `Retriever`, `Reranker`, `Generator`), and `RAGPipeline` coordinates them through a single `ask(question)` method. Components are passed into the pipeline via its constructor, so implementations can be swapped without rewriting the pipeline (no paid APIs or external services required).

## Tasks

- [x] Create `DocumentLoader` that returns a small set of sample documents.
- [x] Create `Retriever` with `retrieve(question, documents)` that selects documents using a simple keyword-match rule.
- [x] Create `Reranker` with `rerank(question, retrieved_documents)`.
- [x] Create `Generator` with `generate(question, context)` that returns a simple template-based answer.
- [x] Create `RAGPipeline` that coordinates these four components.
- [x] Pass components into `RAGPipeline` via its constructor rather than creating them inside the pipeline.
- [x] Provide a single `ask(question)` method.
- [x] Handle empty retrieval results with a helpful fallback message.

## Pass Checks

- [x] A sample question retrieves relevant documents.
- [x] The pipeline runs loader -> retriever -> reranker -> generator.
- [x] A question with no matches returns a fallback rather than crashing.
- [x] The `Retriever` implementation can be swapped without rewriting `RAGPipeline` (it depends on the injected component interface).

## Code

```python
import re


def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))


class DocumentLoader:
    def __init__(self):
        self.documents = [
            {"id": 1, "content": "Python is a programming language used in AI and machine learning."},
            {"id": 2, "content": "Machine Learning enables computer to learn patterns from data"},
            {"id": 3, "content": "RAG combines information retrieval with text generation."},
            {"id": 4, "content": "Vector databases store and search vector embeddings."},
            {"id": 5, "content": "Random Forest is an ensemble machine learning algorithm. "},
        ]

    def load(self):
        return self.documents


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
        scored_documents.sort(key=lambda item: item[0], reverse=True)
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

rag = RAGPipeline(loader, retriever, reranker, generator)

question = "Learning"
answer = rag.ask(question)

print(answer)
```

## How the Code Satisfies the Tasks

- **Modularity**: Each stage is a focused class with a clear responsibility (load, retrieve, rerank, generate).
- **Dependency injection/composition**: `RAGPipeline` receives `loader`, `retriever`, `reranker`, and `generator` in its constructor and stores them, rather than instantiating concrete components internally.
- **Shared flow**: `ask(question)` runs the pipeline in order: load documents, retrieve matches, rerank by keyword overlap, build context, generate a template-based answer.
- **Keyword matching**: `tokenize()` normalizes text to lowercase alphanumeric tokens, so matching is punctuation-tolerant (e.g., `data` vs `data.`).
- **Fallback handling**: If retrieval returns no documents, `ask` returns a helpful message instead of crashing.
- **Swappable components**: A different retriever (e.g., embedding/vector search later) can be injected as long as it implements `retrieve(question, documents)`.

## Sample Behavior

For `question = "Learning"`, the pipeline retrieves and ranks documents containing `learning`/`machine learning` and prints a template-based answer with that context.

## Running the example

```bash
cd "Exercise/MINI RAG PIPELINE"
python code.py
```
