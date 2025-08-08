import loguru

class Task:
    def __init__(self, deps) -> None:
        self.deps = deps
        self.OutputMessage = ""
        self.logger = loguru.logger
        self.OutputResult = ""
        self.runlevel = 99
        
if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")