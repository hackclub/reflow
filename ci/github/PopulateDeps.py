from typing import Any
import json
from loguru import logger
import os
import requests

from intents.intent import PresetDependency

def GenerateDefaultDependenciesObject(argus) -> PresetDependency:
    # populate environment
    try:
        pr_repo: str = argus.repo
        pr_id: str = argus.pull
    except KeyError: # env vars missing, shove in dummy data - you're likely running this for the sake of seeing how a _failing_ commit behaves.
        pr_repo: str = os.environ["PR_REPO"]
        pr_id: str = os.environ["PR_NUMBER"]    
    try:
        gh_token: str = argus.token
    except KeyError:
        gh_token: str = os.environ["GH_TOKEN"]

    # populate headers
    headers: dict[str, str] = {
        "Accept": "application/json",
        "Authorization": f"Bearer {gh_token}"
    }

    # start paging github api for:
    # author
    try:
        author: Any = json.loads(requests.get(f'https://api.github.com/repos/{pr_repo}/pulls/{pr_id}', headers=headers).content)["user"]["id"]
        logger.info(f"Author is {author}")
        # fies
        blobs: list[Any] = [item['blob_url'] for item in json.loads(requests.get(f'https://api.github.com/repos/{pr_repo}/pulls/{pr_id}/files?per_page=1000', headers=headers).content)]
        files: list[Any] = [item['filename'] for item in json.loads(requests.get(f'https://api.github.com/repos/{pr_repo}/pulls/{pr_id}/files?per_page=1000', headers=headers).content)]
        for each in files:
            logger.info(f"Found file in PR: {each}")
    except Exception as e:
        logger.error("An exception occured. You're probably ratelimited. Enable a full trace.")
        logger.info(f"Failed to get endpoint: {e}")
        exit(1)

    # assemble it all!
    deps: PresetDependency = PresetDependency(
        author = author,
        files_list = files,
        pr_id = pr_id,
        gh_token = gh_token,
        pr_repo = pr_repo,
        files_blobs = blobs,
        dryrun = argus.dryrun,
        argus = argus
    )
    return deps


if __name__ == "__main__":
    print("\033[91m MANKIND IS DEAD. BLOOD IS FUEL. HELL IS FULL\033[0m \n talk is dull, send patches. hi@pomonella.dev")