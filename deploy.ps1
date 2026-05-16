# Deploy wrapper for bennettvet.com
#
# What it does:
# 1. Regenerates sitemap.xml from current site state (Python script)
# 2. Stages the regenerated sitemap if it changed
# 3. Runs `netlify deploy --prod --dir=.`
#
# Use this INSTEAD of running `netlify deploy` directly, so the sitemap
# never drifts out of sync with the site contents.

$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot

Set-Location $ProjectRoot

Write-Host "Regenerating sitemap.xml..." -ForegroundColor Cyan
python "$ProjectRoot\scripts\build-sitemap.py"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Sitemap generation failed. Aborting deploy." -ForegroundColor Red
    exit 1
}

# If sitemap changed, stage it (don't commit — leave that to the human)
$sitemapDiff = git diff --quiet sitemap.xml
if ($LASTEXITCODE -ne 0) {
    Write-Host "Note: sitemap.xml changed — remember to commit it after deploy." -ForegroundColor Yellow
}

Write-Host "Deploying to Netlify..." -ForegroundColor Cyan
netlify deploy --prod --dir=.
