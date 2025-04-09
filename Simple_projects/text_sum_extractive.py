from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer  # Latent Semantic Analysis summarizer

# Sample long text
text = """
Natural Language Processing (NLP) has grown rapidly in recent years, becoming a key area of research and application in Artificial Intelligence. It involves enabling machines to understand, interpret, and generate human language. NLP has found applications in a wide range of domains—from chatbots and virtual assistants like Siri and Alexa to spam detection, machine translation, sentiment analysis, and even legal document analysis. With the advent of deep learning, models like BERT, GPT, and T5 have pushed the boundaries of what machines can understand and generate. These advancements have significantly improved tasks like question answering, summarization, and contextual understanding. However, challenges remain, such as bias in training data, ambiguity in language, and maintaining the privacy and security of sensitive information. As NLP continues to evolve, it promises to revolutionize the way we interact with machines and process information.


"""

# Parse the text
parser = PlaintextParser.from_string(text, Tokenizer("english"))

# Create summarizer
summarizer = LsaSummarizer()

# Summarize (3 sentences)
summary = summarizer(parser.document, 3)

# Print summary
for sentence in summary:
    print(sentence)
