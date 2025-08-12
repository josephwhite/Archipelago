<#
    .SYNOPSIS
    Builds Archipelago application(s) for Windows.
    .PARAMETER Dependencies
    Downloads run-time dependencies.
    .PARAMETER Setup
    Build setup with innosetup.
    .PARAMETER GWEnv
    Enables setting enviornment variables for GitHub Workflows.
#>

[CmdletBinding()]
param(
    [Parameter()]
    [switch]$Dependencies,
    [Parameter()]
    [switch]$Setup,
    [Parameter()]
    [switch]$GWEnv
)

$ARCHIPELAGO_ENEMIZER_VERSION = "7.1"
$ARCHIPELAGO_INNOSETUP_VERSION = "6.2.2"

$PATH_CHOCO = choco --version
$PATH_INNOSETUP = choco list -e innosetup --version=$ARCHIPELAGO_INNOSETUP_VERSION --limit-output
$PATH_PYTHON = python --version
$PATH_7ZIP = 7z i

if ($PATH_CHOCO -eq $null) {
    Write-Error "Chocolatey not installed!"
    exit 1
}
if ($PATH_PYTHON -eq $null) {
    Write-Error "Python not installed!"
    exit 1
}
if ($PATH_7ZIP -eq $null) {
    Write-Error "7-Zip not installed!"
    exit 1
}
if (($PATH_INNOSETUP -eq $null) -and ($Sign) -and (-not $Dependencies)) {
    Write-Error "innosetup version $ARCHIPELAGO_INNOSETUP_VERSION not installed!"
    exit 1
}

# Ensure build is in the root of the repo.
if ((Get-Location).Path -ne $PSScriptRoot) {
    Set-Location -Path $PSScriptRoot
}

if ($Dependencies) {
    $enemizer_zip = "https://github.com/Ijwu/Enemizer/releases/download/$ARCHIPELAGO_ENEMIZER_VERSION/win-x64.zip"
    Invoke-WebRequest -Uri $enemizer_zip -OutFile "enemizer.zip"
    Expand-Archive -Path "enemizer.zip" -DestinationPath "EnemizerCLI" -Force
    if ($Sign) {
        choco install innosetup --version=$ARCHIPELAGO_INNOSETUP_VERSION --allow-downgrade
    }
}

Write-Output "Upgrading pip..."
python -m pip install --upgrade pip

python setup.py build_exe --yes
if ( $? -eq $false ) {
    Write-Error "setup.py failed!"
    exit 1
}

$NAME="$(ls build | Select-String -Pattern 'exe')".Split('.',2)[1]
$ZIP_NAME = "Archipelago_$NAME.7z"
Write-Output "$NAME -> $ZIP_NAME"
if ($GWEnv) {
    Write-Output "ZIP_NAME=$ZIP_NAME" >> $Env:GITHUB_ENV
}

New-Item -Path "dist" -ItemType Directory -Force
Set-Location -Path "build"
Rename-Item -Path "exe.$NAME" -NewName "Archipelago"
7z a -mx=9 -mhe=on -ms "../dist/$ZIP_NAME" Archipelago
Rename-Item -Path "Archipelago" -NewName "exe.$NAME"

if ($Sign) {
    Set-Location -Path ".."
    & "${env:ProgramFiles(x86)}\Inno Setup 6\iscc.exe" inno_setup.iss /DNO_SIGNTOOL
    if ( $? -eq $false ) {
        Write-Error "Building setup failed!"
        exit 1
    }
    if ($GWEnv) {
        $contents = Get-ChildItem -Path "setups/*.exe" -Force -Recurse
        $SETUP_NAME=$contents[0].Name
        Write-Output "SETUP_NAME=$SETUP_NAME" >> $Env:GITHUB_ENV
    }
}

exit 0
