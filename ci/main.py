
from intents.intent import PresetDependency
from logging import Logger
from intents.intent import Intent
from tasks.task import Task
from github import PopulateDeps, PublishLog
from util import AssembleOutputLog

from argparse import ArgumentParser
import asyncio
import pkgutil
import importlib
import sys, os
import shutil
from loguru import logger
from types import ModuleType
from typing import Any, Type

def keyFn(e: Intent) -> int:
    return e.runlevel

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

def init(argus) -> None:
    deps: PresetDependency = PopulateDeps.GenerateDefaultDependenciesObject(argus)

    # Start intent performances
    failures: list[str] = []

    intent_classes: list[Type['Intent']] = load_tests('intents')
    tests: list[Any] = [intent_class(deps) for intent_class in intent_classes]
    tests.sort(key=keyFn)

    stat = True
    for test in tests:
        if not test.check():
            stat = False
            failures.append(test.FailureReason)

    # Start task performances
    task_results: list[str] = []
    task_classes: list[Type['Task']] = load_tasks('tasks')
    tasks: list[Any] = [task_class(deps) for task_class in task_classes]
    tasks.sort(key=keyFn)
    for task in tasks:
        task.run()
        task_results.append(task.OutputMessage)

    try: 
        shutil.rmtree("sanity_output/")
    except FileNotFoundError:
        True
    os.mkdir("sanity_output/")

    finlog: str = AssembleOutputLog.AssembleOutputLog(failures, task_results)
    asyncio.run(PublishLog.PublishGithubComment(finlog, deps))

    exit(0 if stat else 1)

if __name__ == "__main__":
    parser: ArgumentParser = ArgumentParser(
        prog="BorderCollei",
        description="Simple sanity checks for Reflow",
        epilog="Keep It Simple, Stupid, and Sane"
    )
    parser.add_argument("--dryrun", action='store_true')
    parser.add_argument("-r", "--repo")
    parser.add_argument("-p", "--pull")
    parser.add_argument("--token")
    parser.add_argument("-v", "--verbose", action="store_true")

    argus = parser.parse_args()
    if not argus.verbose:
        logger.remove()
        logger.add(sys.stderr, level="ERROR")

    init(argus)

    


 