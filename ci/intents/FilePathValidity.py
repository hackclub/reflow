from . import intent # intent deps

class FilePathValidityIntent(intent.Intent):
    def __init__(self, deps) -> None:
        super().__init__(deps)
        self.FailureReason = "Invalid or backtracking file path"
        self.runlevel = 3

    def check(self) -> bool: 
        status = True

        for file in self.deps.files_list:
            if not file.startswith("pcb/") or ".." in file:
                self.logger.error(f'FAIL: {file}')
                status = False
            else:
                self.logger.info(f'Pass: {file}')
        
        # no files attempt to escape the pcb/ directory, assume good intent
        return status

if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")