# Automated Review

This folder contains the python scripts required to complete automated review of PCB commits to the Reflow repository.

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