# Deploy wrapper for bennettvet.com
#
# What it does:
# 1. Regenerates sitemap.xml from current site state (Python)
# 2. Deploys to Netlify via the CLI with --skip-functions-cache so
#    Netlify does NOT re-run the build command locally (the build
#    command in netlify.toml is for Netlify's Linux build servers
#    only; running 'python3' locally on Windows would fail).
#
# Use this INSTEAD of running 'netlify deploy' directly, so the
# sitemap never drifts out of sync with the site contents.

$ErrorActionPreference = "Stop"
$ProjectRoot = $PSScriptRoot
Set-Location $ProjectRoot

Write-Host "Regenerating sitemap.xml..." -ForegroundColor Cyan
python "$ProjectRoot\scripts\build-sitemap.py"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Sitemap generation failed. Aborting deploy." -ForegroundColor Red
    exit 1
}

# Note if sitemap diverged from what's committed
git diff --quiet sitemap.xml 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Note: sitemap.xml changed locally. Commit it after deploy if you want it tracked." -ForegroundColor Yellow
}

Write-Host "Deploying to Netlify..." -ForegroundColor Cyan
# --dir=. tells Netlify to deploy the current directory as-is.
# We avoid 'netlify build' because the build command is meant for Netlify's
# Linux build servers (python3 alias); on Windows we run the Python script
# directly above.
netlify deploy --prod --dir="."
