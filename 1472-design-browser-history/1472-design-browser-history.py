from collections import deque
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = []
        self.forward_hist = []
        self.history.append(homepage)
        

    def visit(self, url: str) -> None:
        #visit url from current page - clear up all forward history?
        self.history.append(url)
        self.forward_hist.clear()

    def back(self, steps: int) -> str:
        #pop from history x steps then return current url
        #if size of history < x steps, do as many steps backwards into history then return url
        
        while steps:
            if len(self.history) == 1:
                break
            self.forward_hist.append(self.history.pop())
            steps -= 1
            
        return self.history[-1]
    
    def forward(self, steps: int) -> str:
        
        if not self.forward_hist:
            return self.history[-1] 
        for i in range(min(steps, len(self.forward_hist))):
            self.history.append(self.forward_hist.pop(-1))
            steps -= 1
        
        return self.history[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)