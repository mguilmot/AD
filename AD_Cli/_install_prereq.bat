@echo off

REM Run as admin! :-)
REM Install python3 manually first if not installed yet.

REM Specific for COVESTRO
set http_proxy=10.229.251.70:8080
set https_proxy=10.229.251.70:8080

REM install this manually if needed:
REM https://sourceforge.net/projects/pywin32 --> choose correct version

pip install pywin32
pip install https://github.com/zakird/pyad/archive/master.zip
