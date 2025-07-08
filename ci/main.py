from intents.intent import PresetDependency
from logging import Logger
from intents.intent import Intent
from tasks.task import Task
from github import PopulateDeps

import pkgutil
import importlib
import os
import shutil
import logging
from types import ModuleType
from typing import Any, Type


def load_tests(HeadPkgName) -> list[Type['Intent']]:
    tests:list[Type['Intent']] = []
    pkg: ModuleType = importlib.import_module(HeadPkgName)
    for _, intentType, _ in pkgutil.iter_modules(pkg.__path__):
        mod: ModuleType = importlib.import_module(f'{HeadPkgName}.{intentType}')
        for fnc in dir(mod):
            obj: Any = getattr(mod, fnc)
            if isinstance(obj, type) and issubclass(obj, Intent) and obj is not Intent:
                tests.append(obj)
    return tests

def load_tasks(HeadPkgName) -> list[Type['Task']]:
    tasks: list[Type['Task']] = []
    pkg: ModuleType = importlib.import_module(HeadPkgName)
    for _, intentType, _ in pkgutil.iter_modules(pkg.__path__):
        mod: ModuleType = importlib.import_module(f'{HeadPkgName}.{intentType}')
        for fnc in dir(mod):
            obj: Any = getattr(mod, fnc)
            if isinstance(obj, type) and issubclass(obj, Task) and obj is not Task:
                tasks.append(obj)
    return tasks

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.ERROR)
    logger: Logger = logging.getLogger(__name__)

    deps: PresetDependency = PopulateDeps.GenerateDefaultDependenciesObject()

    # Start intent performances
    failures: list[str] = []

    intent_classes: list[Type['Intent']] = load_tests('intents')
    tests: list[Any] = [intent_class(deps) for intent_class in intent_classes]

    stat = True
    for test in tests:
        if not test.check():
            stat = False
            failures.append(test.FailureReason)

    # Start task performances
    task_results: list[str] = []
    task_classes: list[Type['Task']] = load_tasks('tasks')
    tasks: list[Any] = [task_class(deps) for task_class in task_classes]
    for task in tasks:
        task.load()
        task.run()
        task_results.append(task.OutputMessage)

    try: 
        shutil.rmtree("sanity_output/")
    except FileNotFoundError:
        True
    os.mkdir("sanity_output/")

    with open("sanity_output/errors.log", "a") as errlog:
        if len(failures) != 0:
        # append greeting to failure
            errlog.write("Your board failed the automated review phase due to the following reasons:")
            for r in failures:
                logger.error(r)
                errlog.write(f"- {r}\n")
        else:
            errlog.write("Your PR has no errors that were automatically detected. Take a breather and grab yourself a little snack to celebrate! 🎉")
    
    for r in task_results:
        logger.info(r)
        with open("sanity_output/tasks.log", "a") as tsklog:
            tsklog.write(f"- {r}\n")

    

    exit(0 if stat else 1)