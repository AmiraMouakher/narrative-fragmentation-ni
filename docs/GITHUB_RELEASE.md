# Publish on GitHub

Suggested repository name: `narrative-fragmentation-ni`.

Suggested description: Research code for political instability and narrative fragmentation in Northern Ireland using GDELT, PSNI and time-series analysis.

Suggested topics: `gdelt`, `political-science`, `narrative-fragmentation`, `northern-ireland`, `time-series`, `reproducible-research`.

Create an empty repository in the intended account, choose visibility, then upload the contents of this folder (not the ZIP itself). Include `.github/` and `.gitignore`; a Git client is the most reliable way to include these files.

Alternatively, from this folder after creating the remote:

```bash
git init
git add .
git commit -m "Prepare research code and documentation"
git branch -M main
git remote add origin https://github.com/YOUR_ACCOUNT/narrative-fragmentation-ni.git
git push -u origin main
```

Replace YOUR_ACCOUNT. No GitHub repository was created by packaging this archive. Keep the visible data-availability and methodological-review notices until resolved. Add repository URL/version/DOI to citation metadata only when those identifiers exist. Confirm the existing MIT choice with all code rightsholders before a public release.
