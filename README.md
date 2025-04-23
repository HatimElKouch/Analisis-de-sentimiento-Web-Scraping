# Proyecto-Reseñas

Este proyecto automatiza la extracción y análisis de reseñas desde Google Maps utilizando Python, Selenium y la API de OpenAI. El proceso comienza con una búsqueda proporcionada por el usuario, que se usa para abrir Microsoft Edge mediante Selenium y realizar scraping de reseñas de un lugar específico. Se extraen el texto, la fecha y la puntuación en estrellas de cada reseña, asegurando que estén ordenadas por las más recientes y expandiendo las reseñas largas.

Una vez extraídas, las reseñas se envían a la API de OpenAI para realizar un análisis de sentimiento, clasificando cada una como positiva, negativa o neutra. Toda esta información se guarda automáticamente en una base de datos SQLite.

Finalmente, el proyecto abre Power BI para visualizar los datos almacenados, permitiendo al usuario explorar gráficamente los resultados del análisis. 
