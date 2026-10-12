SOURCES=$(shell python3 scripts/read-config.py --sources )
FAMILY=$(shell python3 scripts/read-config.py --family )
DRAWBOT_SCRIPTS=$(shell ls documentation/*.py)
DRAWBOT_OUTPUT=$(shell ls documentation/*.py | sed 's/\.py/.png/g')
# Animation scripts written for drawbot-skia (DrawBot-app-only scripts and gif_tools.py are skipped)
ANIMATION_OUTPUT=$(shell grep -l '^from drawbot_skia.drawbot import \*' documentation/animated/*.py | sed 's/\.py/.gif/g')

help:
	@echo "###"
	@echo "# Build targets for $(FAMILY)"
	@echo "###"
	@echo
	@echo "  make build:  Builds the fonts and places them in the fonts/ directory"
	@echo "  make test:   Tests the fonts with fontspector"
	@echo "  make proof:  Creates HTML proof documents in the proof/ directory"
	@echo "  make images: Creates PNG specimen images and animated GIFs in the documentation/ directory"
	@echo

build: build.stamp

venv: venv/touchfile

customize: venv
	. venv/bin/activate; python3 scripts/customize.py

build.stamp: venv sources/config.yaml $(SOURCES)
	rm -rf fonts
	(for config in sources/config*.yaml; do . venv/bin/activate; gftools builder $$config; done)  && touch build.stamp

# requirements.txt is resolved for Python 3.11 (same as GitHub Actions).
PYTHON ?= python3.11

venv/touchfile: requirements.txt
	@which $(PYTHON) >/dev/null || (echo "$(PYTHON) not found. Install it with 'brew install python@3.11'." && exit 1)
	test -d venv || $(PYTHON) -m venv venv
	. venv/bin/activate; pip install --upgrade pip
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

test: build.stamp
	which fontspector || (echo "fontspector not found. Please install it with 'cargo binstall fontspector'." && exit 1)
	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; mkdir -p out/ out/fontspector; fontspector --profile googlefonts -l warn --full-lists --succinct --html out/fontspector/fontspector-report.html --ghmarkdown out/fontspector/fontspector-report.md --badges out/badges $$TOCHECK  || echo '::warning file=sources/config.yaml,title=fontspector failures::The fontspector QA check reported errors in your font. Please check the generated report.'

proof: venv build.stamp
	which diff3proof || (echo "diff3proof not found. Please install it with 'cargo binstall diffenator3'." && exit 1)
	TOCHECK=$$(find fonts/variable -type f 2>/dev/null); if [ -z "$$TOCHECK" ]; then TOCHECK=$$(find fonts/ttf -type f 2>/dev/null); fi ; . venv/bin/activate; mkdir -p out/ out/proof; diff3proof $$TOCHECK --output out/proof

images: venv $(DRAWBOT_OUTPUT) $(ANIMATION_OUTPUT)

%.png: %.py build.stamp
	. venv/bin/activate; python3 $< --output $@

%.gif: %.py documentation/animated/gif_tools.py build.stamp
	. venv/bin/activate; python3 $< --output $@

clean:
	rm -rf venv
	find . -name "*.pyc" -delete

update-project-template:
	npx update-template https://github.com/googlefonts/googlefonts-project-template/

update: venv
	venv/bin/pip install --upgrade uv
	# Resolve for the GitHub Actions runner (Ubuntu, Python 3.11), not the
	# local machine, so pins that only work on macOS can't sneak in.
	venv/bin/uv pip compile requirements.in --upgrade --python-version 3.11 \
		--python-platform x86_64-manylinux_2_28 --custom-compile-command "make update" \
		-o requirements.txt

	git commit -m "Update requirements" requirements.txt
	git push
