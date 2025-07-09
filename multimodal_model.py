import spacy
import wikipedia

class MultimodalAssistant:
    def __init__(self):
        self.qa_db = {
            "photosynthesis": "Photosynthesis is the process by which green plants use sunlight to make food.",
            "neural network": "A neural network is a computer system modeled after the human brain."
        }
        self.history = []
        self.nlp = spacy.load("en_core_web_sm")

    def smart_answer(self, question):
        # Try to match known topics first
        doc = self.nlp(question)
        keywords = [chunk.text.lower() for chunk in doc.noun_chunks]
        for kw in keywords:
            for key in self.qa_db:
                if key in kw:
                    self.history.append((question, self.qa_db[key]))
                    return self.qa_db[key]

        # If not found, try fetching from Wikipedia
        try:
            summary = wikipedia.summary(question, sentences=2)
            self.history.append((question, summary))
            return summary
        except Exception as e:
            fallback = "Sorry, I couldn't find an answer to that."
            self.history.append((question, fallback))
            return fallback
