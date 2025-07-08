from subprocess import CompletedProcess
import subprocess
from . import task
import urllib.parse

class UploadToKiCanvasTask(task.Task):
    def load(self) -> None:
        self.OutputMessage = "Gerbers have been generated and attached to the output artifact"

    def run(self) -> None:
        instances = 0
        idx = 0
        for file in self.deps.files_list:
            if file.endswith(("kicad_pcb")):
                self.logger.info(f'Checking File for DRC Failures: {file}')
                try:
                    subprocess.run(f"kicad-cli pcb export gerbers -o output/gerbers/ --format gerberx2 ../{file}") # we can discard the output of this
                    subprocess.run(f"kicad-cli pcb export drill -o output/gerbers/ ../{file}") # and this
                except FileNotFoundError:
                    self.logger.error("Kicad executable not found! Failing as fallback.")
                    self.OutputMessage = "Kicad executables not found. Gerbers cannot be generated"
                    status = False

