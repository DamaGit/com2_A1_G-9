# 📄 Introducción a GitHub y Comandos Básicos

Este repositorio contiene las instrucciones y pasos esenciales para trabajar con GitHub, desde la creación de la cuenta y repositorio, hasta la gestión de cambios y sincronización con un repositorio remoto.  
El objetivo es aprender el uso de Git y GitHub para el trabajo colaborativo, aplicando comandos en la terminal de Linux para administrar código y documentación.

## ⚙️ Comandos de Git y su función

- **`git clone <url>`** → Descarga un repositorio remoto a tu máquina local.
- **`git status`** → Muestra el estado actual del repositorio: rama activa, cambios sin guardar, archivos en *staging*, etc.
- **`git add <archivo>` / `git add .`** → Añade cambios al área de *staging* para prepararlos antes del commit.
- **`git commit -m "mensaje"`** → Guarda en el historial los cambios añadidos al *staging*, junto con un mensaje descriptivo.
- **`git push`** → Sube los commits locales al repositorio remoto en GitHub.
- **`git pull`** → Descarga y fusiona los cambios más recientes desde el repositorio remoto.
- **`mkdir <carpeta>`** → Crea un nuevo directorio en el sistema de archivos.
- **`cd <carpeta>`** → Cambia de directorio en la terminal.
- **`pwd`** → Muestra la ruta actual en el sistema de archivos.
- **`ls`** → Lista los archivos y carpetas en el directorio actual.

## 📌 Flujo básico de trabajo
1. Crear o clonar un repositorio desde GitHub.
2. Hacer cambios en los archivos.
3. Revisar el estado con `git status`.
4. Añadir cambios al *staging* con `git add`.
5. Guardar cambios con `git commit -m "mensaje"`.
6. Subir cambios al remoto con `git push`.
7. Sincronizar cambios de otros colaboradores con `git pull`.

Este flujo permite mantener el repositorio actualizado, trabajar en equipo y registrar la evolución de los proyectos de forma organizada.
