@echo off
REM === Activar entorno virtual y ejecutar FastAPI ===

REM Activar entorno virtual
call venv\Scripts\activate

REM Iniciar servidor en modo desarrollo
uvicorn backend.app.main:app --reload

REM Mantener ventana abierta si hay error
pause
