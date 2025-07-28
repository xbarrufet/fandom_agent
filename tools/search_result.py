class SearchResult:
    def __init__(self, title: str, url: str, description: str = None):
        self.title = title
        self.url = url
        self.description = description

    def __repr__(self):
        return f"SearchResult(title={self.title}, url={self.url}, description={self.description})"
