# Publish a workflow

1. Fork this repository and create `workflows/<unique-slug>/`.
2. Add `publication.json` with `id` (matching the folder), semantic `version`, and a useful `description`.
3. Add `workflow.json`. Use plugin types as top-level keys, installed plugin IDs inside each section, and parameter objects as values. At least one goal and exactly one solver are required. A trigger is optional and defaults to immediate execution. Multiple instances of one goal may use an array of parameter objects.
4. Use portable inputs and placeholders; never submit credentials or machine-specific paths. Describe required plugins and how to provide inputs in a README in your folder.
5. Run `make setup` once, then `make check`, test execution locally with the Python CLI, then open a pull request. Bump the workflow version whenever its JSON changes.

Reviewers check usefulness, compatibility, provenance, and the absence of secrets. GitHub Actions validates the structure without executing contributed workflows. Merging publishes `workflows.json` on GitHub Pages with immutable commit URLs and checksums. Enable Pages with GitHub Actions in repository settings once.

The CLI can use `--registry https://.../workflows.json` for another registry. Backend deployments use `AUTOSTACGIS_WORKFLOW_REGISTRY_URL`.
