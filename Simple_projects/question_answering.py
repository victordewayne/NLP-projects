from transformers import pipeline 

qa_pipeline = pipeline("question-answering")

context = """
Albert Einstein was born in Ulm, Germany in 1879. He developed the theory of relativity, 
one of the two pillars of modern physics. He received the Nobel Prize in Physics in 1921.
"""
questions = [
    "Where was Einstein born?",
    "When was Einstein born?",
    "What did he develop?",
    "When did he win the Nobel Prize?"
]
for q in questions:
    result = qa_pipeline(question=q, context=context)
    print(f"\nQ: {q}")
    print(f"A: {result['answer']} ({round(result['score'], 4)})")