import logging
class Task:
    def __init__(self, deps) -> None:
        self.deps = deps
        self.OutputMessage = ""
        self.logger = logging.getLogger(__name__)
        self.OutputResult = ""
        
if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")