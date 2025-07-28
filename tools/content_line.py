

CONTENT_LINE_TYPE_TITLE= "title"
CONTENT_LINE_TYPE_TEXT = "text"

class ContentLine:
    def __init__(self, content_type: str, text: str, level: int = 0):
        self.content_type = content_type
        self.text = text
        self.level = level

    def __repr__(self):
        return f"ContentLine(content_type={self.content_type}, text={self.text}, level={self.level})"

    def to_dict(self):
        return {
            "content_type": self.content_type,
            "text": self.text,
            "level": self.level
        }

    def __str__(self):
        return f"{self.content_type} (level {self.level}): {self.text}"

    def as_markdown(self):
        if self.content_type == CONTENT_LINE_TYPE_TITLE:
            return f"{'#' * self.level} {self.text}\n"
        elif self.content_type == CONTENT_LINE_TYPE_TEXT:
            return f"{self.text}\n"
        else:
            return f"{self.text}\n"

def create_content_type_title(text: str, level: int)->ContentLine:
        return ContentLine(content_type=CONTENT_LINE_TYPE_TITLE, text=text, level=level)

def create_content_type_text(text: str)->ContentLine:
        return ContentLine(content_type=CONTENT_LINE_TYPE_TEXT, text=text)

