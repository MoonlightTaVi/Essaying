from random import Random


class Decryptor:
    tags: list = ["xyz", "abc", "qwe"]
    current_tag: str = tags[0]
    def __init__(self, keyword: str) -> None:
        self.keyword = keyword
    def get_index(self, repeat_times: int, limit: int = 7000) -> int:
        random = Random(self.keyword)
        id: int = 0
        for _ in range(repeat_times):
            id = random.randint(0, limit)
        last_id = len(self.tags) - 1
        self.current_tag = self.tags[random.randint(0,last_id)]
        return id
    def get_portion(self, source: str, version: int = 1, length: int = 20):
        start: int = self.get_index(version, len(source))
        return source[start:start+length]
    