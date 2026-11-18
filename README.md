# basecamp-sandbox

Project for testing BaseCamp releases.

## Getting started

Turn on the pre-commit hook, which runs `just check` before every commit:

```sh
git config core.hooksPath .githooks
```

## Updating from the template

This project was made from the BaseCamp template. To bring in template changes, run the update by hand on a branch, never on `main`:

```sh
git switch -c chore/template-update
uvx copier update
git diff
```

Review the diff, then merge it through a PR like any other change. The update never touches this README.

