# AutostacGIS workflows

Published workflows are ordinary capability-grouped JSON configuration files. They are discovered by the Python library and both AutostacGIS GUIs from `https://autostacgis.github.io/autostacgis-workflows/workflows.json`.

```sh
autostacgis workflows available
autostacgis workflows download mosaic ./workflows
autostacgis validate ./workflows/mosaic.json
```

Edit the downloaded goal before running. The example asks for `properties.ready == true`; provide STAC inputs or add a metadata source and processing plugins that can produce your goal. No plugins are installed by downloading a workflow.

See [CONTRIBUTING.md](CONTRIBUTING.md) to publish through a pull request. Releases pin source URLs to a commit and SHA-256, using the same registry transport as Python plugins. Saved copies and edits in the GUIs belong to the connected backend; publication does not change them.
