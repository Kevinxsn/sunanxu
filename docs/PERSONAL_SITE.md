# Editing my personal site

The site uses the existing al-folio layouts without local layout, include, or Sass overrides.

## Content

| Content                 | File                       |
| ----------------------- | -------------------------- |
| Biography and portrait  | `_pages/about.md`          |
| Research and CV entries | `_data/cv.yml`             |
| Research page structure | `_pages/research.md`       |
| Publication records     | `_bibliography/papers.bib` |
| Teaching and outreach   | `_pages/teaching.md`       |
| Email and GitHub links  | `_data/socials.yml`        |
| Site title and metadata | `_config.yml`              |

In `_data/cv.yml`, find `position: Research with Tiffany`. Fill in her name, project title, dates, summary, and highlights, then remove `reserved: true`. Research entries with `type: research` appear on both the Research page and the CV. The existing GRN work and January 2024–March 2026 dates belong to Bing Ren, as confirmed during setup.

BMS is omitted. The original PDF is not copied or linked because it contains that experience. The CV page uses `_data/cv.yml`; `assets/json/resume.json` is unused basic contact metadata. Add a revised PDF later by setting `cv_pdf` in `_pages/cv.md`.

The original photo is used unchanged at `assets/img/IMG_6260.JPG`. Demo collections and unused pages remain in source but are excluded from the build, navigation, and search.

Publication metadata is linked to the [EMNLP proceedings](https://aclanthology.org/2024.emnlp-main.990/) and the [brain atlas preprint record](https://pubmed.ncbi.nlm.nih.gov/41676689/). The latter remains labeled as a preprint.

## Preview

To view the generated site without installing Ruby, run from this folder:

```bash
python3 bin/preview_site.py
```

Open `http://127.0.0.1:4000/al-folio/`. This serves the existing `_site` build; rebuild after editing content.

To rebuild or preview with live updates, use the repository's [installation guide](INSTALL.md) to set up Ruby and Bundler, then run:

```bash
bundle install
bundle exec jekyll serve --baseurl /al-folio
```

## GitHub Pages

The deployment workflow uses `_config.github.yml` to serve the `Kevinxsn/sunanxu` repository at `/sunanxu`. The base configuration keeps `/al-folio` for local development and the starter checks. If the repository name or domain changes, update the deployment configuration too.

Build the deployment version with:

```bash
bundle exec jekyll build --config _config.yml,_config.github.yml
```

The site has been prepared locally. No commit, push, or deployment was performed during personalization.
