from analyzer import SentimentAnalyzer

def main():
    sa = SentimentAnalyzer()
    print("Sentiment Analyzer CLI")
    print("Type 'quit' to exit\n")
    while True:
        text = input("Enter text: ")
        if text.lower() == "quit":
            break
        result = sa.analyze(text)
        label = "Positive" if result["compound"] > 0.05 else "Negative" if result["compound"] < -0.05 else "Neutral"
        print(f"  → {label} (score: {result['compound']})\n")

if __name__ == "__main__":
    main()
