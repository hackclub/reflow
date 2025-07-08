import logging

class PresetDependency:
    def __init__ (self, author: str, pr_repo: str, pr_id: str, gh_token: str, files_list: list[str], files_blobs: list[str]) -> None:
        self.author: str = author
        self.pr_repo: str = pr_repo
        self.pr_id: str = pr_id
        self.gh_token: str = gh_token
        self.files_list: list[str] = files_list
        self.files_blobs: list[str] = files_blobs

class Intent:
    def __init__(self, deps: PresetDependency) -> None:
        self.deps: PresetDependency = deps
        self.FailureReason: str = ""
        self.logger = logging.getLogger(__name__)

if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")