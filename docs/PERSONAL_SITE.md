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

For automatic rebuilds, run from this folder:

```bash
./bin/dev
```

Open `http://127.0.0.1:4000/al-folio/` and keep the terminal running while you edit. Saving Markdown, bibliography, or data files rebuilds the site; refresh the browser to see the result. Press `Ctrl+C` to stop the server. After changing `_config.yml`, stop and restart the server so Jekyll loads the new settings.

The launcher does not enable Jekyll's optional LiveReload browser refresh because the theme's Content Security Policy blocks its separate WebSocket port. Automatic rebuilding works without it.

This Mac has a project-local Ruby, Bundler, and Node runtime in `vendor/dev-runtime`, with Jekyll dependencies in `vendor/bundle`. These folders are ignored by Git and excluded from the website. The launcher uses that runtime when available; on another computer it uses the installed `bundle` command after following the [installation guide](INSTALL.md).

For a static preview of the last build without Jekyll, run:

```bash
python3 bin/preview_site.py
```

This serves the existing `_site` build; it does not rebuild after editing content. Run only one preview server at a time because both use port 4000.

With a system Ruby and Bundler installation, the equivalent commands are:

```bash
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

## GitHub Pages

The deployment workflow uses `_config.github.yml` to serve the `Kevinxsn/sunanxu` repository at `/sunanxu`. The base configuration keeps `/al-folio` for local development and the starter checks. If the repository name or domain changes, update the deployment configuration too.

Build the deployment version with:

```bash
bundle exec jekyll build --config _config.yml,_config.github.yml
```

The site has been prepared locally. No commit, push, or deployment was performed during personalization.
