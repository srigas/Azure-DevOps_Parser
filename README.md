# Repos Parser

The present repository contains some simple scripts that can be used to parse public or private repositories (note that private repositories require PATs). More specifically, the user inserts details such as repo name/url inside the script and specifies a folder name within the given repo (it can also be the root folder). The script parses all of the contents of the given folder and generates a contents.txt file which reads:

```
folder/file_1:

```file_1 contents
```​

folder/file_2:

```file_2 contents
```​

etc.

```

This can be used with LLMs such as ChatGPT which are helpful for code generation, but have some limitations. For example, as of 2023, the VSCode integrated Copilot service only checks a given open file at a time to provide code suggestions, without having a complete overview of the whole codebase. Using this script, a user can directly copy-paste its contents to any available LLM (even locally hosted) and ask for personalized code suggestions which respect the user's existing codebase. In this way, conflicts between the LLM's code suggestions and the user's current codebase can be minimized.

For now, the present repo holds a script that parses the contents of an Azure DevOps Repo folder. After setting up your details in the configuration section, run

```
python azure_repo.py
```

to run the script.

In the future, similar scripts for GitHub, GitLab, etc. will be uploaded.
