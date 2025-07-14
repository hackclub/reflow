from githubkit.auth.token import TokenAuthStrategy
import os
import logging
from logging import Logger

from typing import TypedDict
from githubkit import GitHub, Response
from githubkit.versions.latest.models import IssueComment
from githubkit.versions.latest.types import IssueCommentType

async def PublishGithubComment(post: str) -> None:
    logger: Logger = logging.getLogger(__name__)
    
    # populate environment
    try:
        pr_repo: str = os.environ["PR_REPO"]
        pr_id: str = os.environ["PR_NUMBER"]     
        gh_token: str = os.environ["GH_TOKEN"]
    except KeyError:
        logger.error("Running without fully populated env-vars. Will not post comment to GitHub.")
        return None 

    github: GitHub[TokenAuthStrategy] = GitHub(gh_token)
    repo_string_thing: list[str] = pr_repo.split("/")

    github.rest.issues.create_comment(
        owner = repo_string_thing[0],
        repo = repo_string_thing[1],
        issue_number = int(pr_id),
        body = post
    )

    
    


    
        