Write-Host "Iniciando proceso automatizado..."

# Cambiar al directorio del proyecto
Set-Location "C:\Users\rportatil113\Desktop\Repositorio_data sciense\proyectoguapo"

# Pedir al usuario la búsqueda
$busqueda = Read-Host "¿Qué quieres buscar?"

# Ruta al script de Python
$pythonScript = "C:\Users\rportatil113\Desktop\Repositorio_data sciense\proyectoguapo\Prueba API.py"

# Ejecutar el script Python directamente en la misma ventana (para ver output y Edge)
Write-Host "Ejecutando scraping y análisis de sentimientos..."
python "$pythonScript" "$busqueda"

# Verificar si hubo error con el último comando
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Hubo un error en el proceso de scraping o análisis."
    Read-Host "Presiona una tecla para continuar..."
    exit
}

# Abrir Power BI con el archivo específico
Write-Host "Abriendo Power BI..."
Start-Process -FilePath "C:\Users\rportatil113\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\SQLite ODBC Driver for Win64\Shells\proyectoguapo.pbix" `
    -ArgumentList "C:\Users\rportatil113\Desktop\Repositorio_data sciense\proyectoguapo\mi_archivo.pbix"

Write-Host "Proceso completado."
Read-Host "Presiona una tecla para cerrar..."

