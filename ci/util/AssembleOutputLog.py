from logging import Logger
import logging

def AssembleOutputLog(failures: list[str], task_results: list[str]) -> str:
    logger: Logger = logging.getLogger(__name__)
    errlog: str = "" 
    if len(failures) != 0:
        # append greeting to failure
        errlog += ("Your board failed the automated review phase due to the following reasons:\n")
        for r in failures:
            errlog += (f"- {r}\n")
    else:
        errlog += ("Your PR has no errors that were automatically detected. Take a breather and grab yourself a little snack to celebrate! 🎉")
    
    tsklog: str = "We've also got a couple things you might want to look at: \n"

    for r in task_results:
        logger.info(r)
        tsklog += (f"- {r}\n")

    fin: str = ""

    fin += errlog
    fin += "\n"
    fin += tsklog

    return fin
