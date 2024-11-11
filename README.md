# Proyecto de Administración de API para Residencias Profesionales

Este proyecto se centra en la administración y pruebas de una API utilizando Docker y Jenkins, desarrollado en equipo para la gestión de proyectos de residencias profesionales en el Instituto Tecnológico de León.

## Equipo de Desarrollo
- **Monjaraz Perez Sara Alexandra** ([SaraAlexMP](https://github.com/SaraAlexMP))
- **García Solís Francisco** ([Upstagebunion](https://github.com/Upstagebunion))
- **Brandon** ([Brandon1924](https://github.com/Brandon1924))
- **Miguel Ángel Loza López** ([Esblad](https://github.com/Esblad))

## Descripción General
Este proyecto implementa una API administrada mediante Docker, con integración de pruebas automáticas en Jenkins. A continuación se muestran las etapas principales de configuración, ejecución y resolución de errores en el pipeline, incluyendo capturas de cada paso clave.

---

### 1. Instalación y Configuración del Plugin de Docker en Jenkins
Para habilitar el uso de contenedores en Jenkins, fue necesario instalar el plugin de Docker. Esta integración permite ejecutar la API en contenedores y realizar pruebas de manera continua.

![Instalación de plugin Docker en Jenkins](https://github.com/user-attachments/assets/e5d1db37-5a8b-49fb-bbd8-d9a658f83854)

---

### 2. Configuración del Pipeline
El pipeline fue configurado para ejecutar la API en un contenedor Docker y correr pruebas automatizadas con `pytest`.

![Ajuste de pipeline](https://github.com/user-attachments/assets/6e4e386b-6a7e-44ae-bbda-125fa0da3b30)

### Código del Pipeline
pipeline {
    agent any
    stages {
        stage('Run Tests') {
            steps {
                bat 'docker run project-management-api pytest'
            }
        }
    }
}

### 3. Primera Ejecución: Error por Comando Incorrecto
En la primera ejecución, surgió un error al intentar ejecutar un comando de Linux en un entorno Windows, lo que se resolvió reemplazando sh con bat.
![primer ejecucion - comando linux sh, reemplazado por bat](https://github.com/user-attachments/assets/2864edb6-b0c2-4509-b261-c0fa31304fd3)

### 4. Ejecución del Contenedor Docker y Pruebas
Tras configurar correctamente el contenedor Docker, se ejecutó el archivo de pruebas. Sin embargo, fue necesario ajustar el Dockerfile para incluir pytest en las dependencias.
![Segundo error - pytest no estaba instalado en las dependencias y docker file no lo especificaba](https://github.com/user-attachments/assets/c57be236-282a-4a40-92e5-03b9b3a41b37)

### 5. Ajustes Adicionales para Ejecutar Pruebas
Hubo varios errores que requirieron ajuste en el Dockerfile y la estructura de la API:
  Error: pytest no estaba incluido en el Dockerfile.
  Error: La aplicación no se encontraba correctamente para las pruebas iniciales.
  ![ejecucion 6 - error al encontrar el archivo de pruebas - no se incluyo en el container](https://github.com/user-attachments/assets/4060a6fb-77ea-46c1-af15-ff5efbd48a4c)
  ![ejecución 7 - se ejecuto el archivo de pruebas, pero no encontraba la app para crearla y probarla](https://github.com/user-attachments/assets/97c41265-eeab-48ec-98d6-ae4287f60986)
  
### 6. Prueba Completa y Ejecución Satisfactoria
Finalmente, las pruebas se completaron exitosamente, lo cual validó la configuración del pipeline, el contenedor Docker y la API.
![ejecución 8 - Prueba completada Con exito](https://github.com/user-attachments/assets/35cca04b-60a7-41f6-b313-7e7f19069f49)
![pruebas de api hasta success](https://github.com/user-attachments/assets/be09f884-725f-4890-9ece-8948a772660e)

### Conclusión
La integración de Docker y Jenkins para la gestión de la API resultó exitosa tras varias iteraciones y ajustes. Este pipeline ahora permite ejecutar pruebas automatizadas de forma continua, optimizando el proceso de despliegue y aseguramiento de calidad para futuros desarrollos.
