class TextAnalyzer:
    """
    Responsible only for analyzing text.
    This class follows the Single Responsibility Principle.
    """

    def __init__(self, text: str):
        self.text = text

    def word_count(self) -> int:
        words = self.text.split()
        return len(words)


class TextFileSaver:
    """
    Responsible only for saving text to a file.
    This separates I/O responsibility from text analysis.
    """

    def save(self, text: str, filename: str) -> None:
        with open(filename, "w") as f:
            f.write(text)


if __name__ == "__main__":
    text = "An example that now follows the SOLID Single Responsibility Principle."
    analyzer = TextAnalyzer(text)
    saver = TextFileSaver()

    count = analyzer.word_count()
    print(f"Word count: {count}")

    saver.save(text, "example.txt")
    print("Text saved to example.txt")
