from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="t5-small")

# Long text input
text = """
Natural Language Processing (NLP) is a field of Artificial Intelligence that focuses on the interaction 
between humans and computers using natural language. It involves enabling machines to understand, interpret, 
and generate human language. With the advent of deep learning, models like BERT, GPT, and T5 have pushed 
the boundaries of what machines can understand and generate. These advancements have significantly improved 
tasks like question answering, summarization, and contextual understanding.
"""

# Generate summary
summary = summarizer(text, max_length=60, min_length=20, do_sample=False)
print("Summary:", summary[0]['summary_text'])
