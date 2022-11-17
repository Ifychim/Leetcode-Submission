class BrowserHistory:

    def __init__(self, homepage: str):
        self.front = 0
        self.cur = -1
        self.hashMap = {-1:homepage}

    def visit(self, url: str) -> None:
        self.front = self.cur + 1
        self.hashMap[self.front] = url
        self.front += 1
        self.cur += 1

    def back(self, steps: int) -> str:
        loc = max(-1, self.cur - steps)
        self.cur = loc
        return self.hashMap[self.cur]
            

    def forward(self, steps: int) -> str:
        loc = min(steps + self.cur, self.front - 1)
        self.cur = loc
        return self.hashMap[self.cur]
