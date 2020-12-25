@echo off
color 3

set fn=%1
set flag=%2
cd /d %~dp0

If "%1"=="" (
    echo "parametros invalidos"
) else ( 
    if "%2"=="n" (
        python webNuvem.py %fn% %flag%
        ) else (
            if "%2"=="l" (
                python webLocal.py %fn%
            )
        )
    )
