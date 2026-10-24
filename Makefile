PYTHON ?= .venv/bin/python
.PHONY: setup check manifest
setup:
	python3 -m venv .venv
	.venv/bin/python -m pip install -r requirements.txt
check:
	$(PYTHON) scripts/build_manifest.py --output /tmp/autostacgis-workflows-check.json
manifest:
	$(PYTHON) scripts/build_manifest.py
