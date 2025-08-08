from . import task
import urllib.parse

class UploadToKiCanvasTask(task.Task):
    def __init__(self, deps) -> None:
        super().__init__(deps)
        self.OutputMessage = "The KiCanvas link for manual review is available "
        self.runlevel = 4


    def run(self) -> None:
        instances = 0
        idx = 0
        for file in self.deps.files_list:
            if file.endswith(("kicad_pro")):
                if instances == 0:
                    GhString: str = f"{self.deps.files_blobs[idx]}"
                    # github is REALLY stupid. it ensures the url is parsed after the /blob/commit/ portion, but not before. so, we need to manually parse it, and then undo some of the parsing.
                    safeString: str = urllib.parse.quote_plus(GhString).replace("%25", "%")
                    self.OutputResult = f"[Here](https://kicanvas.org/?github={safeString})"
                else:
                    GhString = f"{self.deps.files_blobs[idx]}"
                    safeString: str = urllib.parse.quote_plus(GhString)
                    self.OutputResult += f"And [Here](https://kicanvas.org/?github={safeString})"
                instances += 1
            idx += 1
        self.OutputMessage += self.OutputResult

