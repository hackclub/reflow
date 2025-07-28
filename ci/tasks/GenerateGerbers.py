import subprocess
from . import task

class UploadToKiCanvasTask(task.Task):
    def load(self) -> None:
        self.OutputMessage = "Gerbers have been generated and attached to the output artifact"

    def run(self) -> None:
        for file in self.deps.files_list:
            if file.endswith(("kicad_pcb")):
                self.logger.info(f'Writing gerbers from: {file}')
                try:
                    subprocess.run(f"kicad-cli pcb export gerbers -o sanity_output/gerbers/ ../{file}", shell=True) # we can discard the output of this
                    subprocess.run(f"kicad-cli pcb export drill -o saniity_output/gerbers/ ../{file}", shell=True) # and this
                except FileNotFoundError:
                    self.logger.error("Kicad executable not found! Failing as fallback.")
                    self.OutputMessage = "Kicad executables not found. Gerbers cannot be generated"

