from tools.content_line import ContentLine


class FandomContentResult:
    def __init__(self, title: str, url: str, content: [ContentLine], url_image:str):
        self.title = title
        self.url = url
        self.content = content
        self.url_image = url_image

    def get_content_as_markdown(self) -> str:
        """
        Get the content as markdown.
        """
        markdown_content = ""
        for line in self.content:
            markdown_content += line.as_markdown()
            # markdown_content +=line.text
        return markdown_content

    def get_content_as_text(self) -> str:
        """
        Get the content as markdown.
        """
        markdown_content = ""
        for line in self.content:
            markdown_content +=line.text
        return markdown_content

    def __repr__(self):
        return f"FandomContentResult(title={self.title}, url={self.url}, content={self.content}, url_image={self.url_image})"

    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url,
            "content": self.content,
            "url_image": self.url_image
        }
    def __str__(self):
        return f"Title: {self.title}\nURL: {self.url}\nContent: {self.content}\nImage URL: {self.url_image}"


ERROR_FANDOM_CONTENT_RESULT =FandomContentResult("","",[],"")
