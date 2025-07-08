from . import intent # intent deps
class FileTypesIntent(intent.Intent):
    def check(self) -> bool:
        self.FailureReason = "Presence of non-KiCAD files"

        status = True

        for file in self.deps.files_list:
            if not file.endswith(("kicad_dru","kicad_sch","kicad_pcb","kicad_pro", "md")):
                self.logger.error(f'File FAILS: {file}')
                status = False
            else:
                self.logger.info(f'File Passes: {file}')
        
        # no non-kicad files are being added by repository, assume good intent
        return status

        
if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")