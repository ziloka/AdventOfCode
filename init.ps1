if (-not (Test-Path .\\.venv)) {
    python -m venv .venv
}
# Write-Host $(Get-Location)
.\.venv\Scripts\activate.ps1
$pkgs = pip list
if (!($pkgs | Select-String -Pattern "advent-of-code-data")) {
    pip install --require-virtualenv advent-of-code-data python-dotenv
}