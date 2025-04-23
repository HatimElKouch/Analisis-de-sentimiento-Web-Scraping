@echo off
echo Iniciando proceso automatizado...

:: Cambiar al directorio del proyecto
cd /d "C:\Users\rportatil113\Desktop\Repositorio_data sciense\proyectoguapo"

:: Pedir al usuario la búsqueda
set /p busqueda="¿Qué quieres buscar?: "

:: Ejecutar el script con la búsqueda como argumento (esperará hasta que termine)
echo Ejecutando scraping y análisis de sentimientos...
python "C:\Users\rportatil113\Desktop\Repositorio_data sciense\proyectoguapo\Prueba API.py" "%busqueda%"

:: Verificar que el proceso de scraping se haya completado
if %errorlevel% neq 0 (
    echo ❌ Hubo un error en el proceso de scraping o análisis.
    pause
    exit /b
)

:: Abrir Power BI con el archivo específico
echo Abriendo Power BI...
start "" "C:\Users\rportatil113\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\SQLite ODBC Driver for Win64\Shells\proyectoguapo.pbix" "C:\Users\rportatil113\Desktop\Repositorio_data sciense\proyectoguapo\mi_archivo.pbix"

echo Proceso completado.
pause
