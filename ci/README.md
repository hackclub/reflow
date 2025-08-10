# Automated Review

This folder contains the python scripts required to complete automated review of PCB commits to the Reflow repository.

## Instructions for Use (ur welcone jenin)
1. General upkeep - cd into the repository, selectively clone your PR with `git restore --source=${{ github.sha }} --staged --worktree pcb/` (where github.sha is the hash of the latest commit of the PR)
3. cd into /ci/
4. If you have `uv` installed, make a venv with `uv venv` and then `uv sync` deps.
5. Run the script with `uv run main.py`.

There's a series of flags or environment variables you need to set. The mandatory ones are:
- `-r` | determines the repository you work on. Usually hackclub/reflow, previouly pmnlla/reload.
- `-p` | The # of the pull request within that repo.
- `--token` | Github auth token. Used due to its much higher ratelimits in opposition to non-authenticated requests.

And a couple you'll want to keep watch over:
- `-v` | Verbose logging. Emable this to see task output as well as better logs of which files get processed.
- `--dryrun` | Dry run - will _not_ send a comment to github underneath the PR.

## Adding a new intent

A new intent is defined in the intents/ folder as a python script, inheriting the `intent` type and defining a `check()` function.

In this function, a series of properties are exposed:

- Github PR Number (as self.deps.pr_id)
- Github Repo (as self.deps.pr_repo)
- Github Authentication Token (as self.deps.gh_token)
- ID of the author, as exposed through commits, by the Github API
- List of files modified
- List of file blob addresses, in the order of files modified.

Aside from these factors, no additional information is exposed to an intent.

An intent is meant to ping the Github API independently for any of its additional requirements, such as authors & contributors, modified files, diffs & patches, etc.

A logging interface is exposed through the logger library, and can be acquired with `logging.getLogger(__name__)`.

An intent reports its status as a boolean - True or False, with True representing a pass and False representing a failure. It is a good idea to default to passing and trip a failure upon events to simplify code readability and clearly define failure vectors.

See the intents/ folder for examples.

## Adding a new task

Tasks follow a very similar structure to Tasks.

The primary difference is the new "final" modifier. It determines whether the task runs as one of the last tasks required, rather than by how Python organizes it.

This is useful for the github comment modifier, etc.

Artifact uploading is handled in the workflow file since it's the easiest way to directly interface with Github. However, 

## Tech Stack

The CI pipeline uses the uv package manager and python 3.12.
