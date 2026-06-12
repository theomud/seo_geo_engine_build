# Copy all research outputs to Downloads
# Run this after all workflows complete
#
# Usage: . .\COPY-TO-DOWNLOADS.ps1

$src = "C:\Users\Theo\OneDrive\Desktop\seo_geo_engine_build"
$dst = "C:\Users\Theo\Downloads\PawRoute_Research_2026-06-11"

Write-Host "Copying $src to $dst ..."

if (Test-Path $dst) {
    Remove-Item $dst -Recurse -Force
}

Copy-Item $src $dst -Recurse

Write-Host "Done. Files in $dst:"
Get-ChildItem $dst -Recurse -Filter "*.md" | Select-Object FullName
