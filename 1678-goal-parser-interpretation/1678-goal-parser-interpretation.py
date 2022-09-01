class Solution:
    def interpret(self, command: str) -> str:
        #one line solution
        return command.replace("()", "o").replace("(al)","al")