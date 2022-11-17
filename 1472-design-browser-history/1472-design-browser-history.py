class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [] #main browser history
        self.forward_history = [] #stores forward history
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        self.history.append(url)
        
        self.forward_history.clear()

    def back(self, steps: int) -> str:

        
        for i in range(min(steps, len(self.history))):
            if len(self.history) == 1:
                return self.history[-1]
            self.forward_history.append(self.history.pop())
            steps -=1

        return self.history[-1]

    def forward(self, steps: int) -> str:
        
        if len(self.forward_history) == 0:
            return self.history[-1]
        
        else:
            for i in range(min(steps, len(self.forward_history))):
                self.history.append(self.forward_history.pop())
                steps -= 1
                
        return self.history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)