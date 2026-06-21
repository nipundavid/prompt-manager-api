class Prompt:
    def __init__(self, title, content, category):
        self.title = title
        self.content = content
        self.category = category

    def to_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "category": self.category
        }