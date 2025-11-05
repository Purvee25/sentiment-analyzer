import re
from collections import defaultdict

class SentimentAnalyzer:
    def __init__(self):
        self.positive_words = {"good","great","excellent","amazing","wonderful","fantastic","love","best","happy","perfect","awesome","brilliant","outstanding","superb","beautiful","delightful","pleasant","impressive","remarkable","exceptional"}
        self.negative_words = {"bad","terrible","awful","horrible","worst","hate","poor","ugly","boring","disappointing","dreadful","pathetic","mediocre","lousy","unpleasant","annoying","frustrating","disgusting","inferior","worthless"}
        self.intensifiers = {"very":1.5,"extremely":2.0,"incredibly":1.8,"absolutely":1.9,"really":1.3,"quite":1.2,"somewhat":0.8,"slightly":0.6,"barely":0.4}
        self.negations = {"not","no","never","neither","nobody","nothing","nowhere","nor","cannot","cant","dont","doesnt","didnt","wont","wouldnt","shouldnt","couldnt","isnt","arent","wasnt","werent"}

    def _tokenize(self, text):
        return re.findall(r"\b\w+\b", text.lower())

    def analyze(self, text):
        tokens = self._tokenize(text)
        pos_score, neg_score = 0.0, 0.0
        i = 0
        while i < len(tokens):
            word = tokens[i]
            multiplier = 1.0
            negated = False
            if i > 0 and tokens[i-1] in self.negations:
                negated = True
            if i > 0 and tokens[i-1] in self.intensifiers:
                multiplier = self.intensifiers[tokens[i-1]]
            if i > 1 and tokens[i-2] in self.intensifiers:
                multiplier = self.intensifiers[tokens[i-2]]
            if word in self.positive_words:
                if negated:
                    neg_score += multiplier
                else:
                    pos_score += multiplier
            elif word in self.negative_words:
                if negated:
                    pos_score += multiplier
                else:
                    neg_score += multiplier
            i += 1
        total = pos_score + neg_score + 1
        return {"positive": round(pos_score/total, 3), "negative": round(neg_score/total, 3), "neutral": round(1/total, 3), "compound": round((pos_score - neg_score) / total, 3)}

    def analyze_aspects(self, text, aspects):
        sentences = re.split(r'[.!?]+', text)
        results = {}
        for aspect in aspects:
            relevant = [s for s in sentences if aspect.lower() in s.lower()]
            if relevant:
                scores = [self.analyze(s) for s in relevant]
                avg_compound = sum(s["compound"] for s in scores) / len(scores)
                results[aspect] = {"compound": round(avg_compound, 3), "mentions": len(relevant)}
            else:
                results[aspect] = {"compound": 0, "mentions": 0}
        return results

    def batch_analyze(self, texts):
        return [self.analyze(t) for t in texts]

if __name__ == "__main__":
    sa = SentimentAnalyzer()
    print(sa.analyze("This is a very good product"))
    print(sa.analyze("The service was not good at all"))
    print(sa.analyze_aspects("The food was great but service was terrible.", ["food", "service"]))
