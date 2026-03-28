# Leet Code Algo 359. Logger Rate Limiter

class Logger:

    def __init__(self):
        self.log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.log:
            self.log[message] = timestamp + 10
            return True
        else:
            if self.log[message] > timestamp:
                return False
            else:
                self.log[message] = timestamp + 10
                return True
