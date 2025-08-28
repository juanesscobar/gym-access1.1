# 🏋️‍♂️ GymAccess 1.1

**GymAccess** es una aplicación web minimalista y moderna para gestionar el acceso de usuarios a un gimnasio.  
Está desarrollada con **FastAPI** (backend) y **HTML/CSS/JavaScript** (frontend) con integración de plantillas Jinja2 y manejo de archivos estáticos.

---

## 🚀 Características

- 📌 **Panel de acceso rápido** para control de usuarios.
- 🎨 **Interfaz minimalista y responsive** inspirada en Nike Training y Apple Fitness.
- ⚡ **Backend con FastAPI** y soporte de templates HTML.
- 📂 **Gestión de archivos estáticos** (CSS, JS, imágenes).
- 🔒 Preparado para integración futura con **bases de datos** y APIs externas.

---

## 📷 Vista previa

![Vista previa de GymAccess](frontend/static/images/preview.png)

---

## 🛠 Tecnologías utilizadas

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) 🐍
- **Frontend:** HTML5, CSS3, JavaScript
- **Plantillas:** [Jinja2](https://jinja.palletsprojects.com/)
- **Servidor local:** Uvicorn
- **Control de versiones:** Git & GitHub

---

## 📦 Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/juanesscobar/gym-access1.1.git
   cd gym-access1.1
Crear y activar entorno virtual

python -m venv venv
source venv/bin/activate   # En macOS/Linux
venv\Scripts\activate      # En Windows


Instalar dependencias

pip install -r requirements.txt


Ejecutar el servidor

uvicorn backend.main:app --reload


Abrir en el navegador

http://127.0.0.1:8000

📂 gym-access1.1/
│
├── backend/
│   ├── main.py             # Configuración principal de FastAPI
│   └── __init__.py
│
├── frontend/
│   ├── templates/          # Archivos HTML (base.html, home.html, etc.)
│   └── static/
│       ├── css/            # Archivos de estilos
│       ├── js/             # Archivos JavaScript
│       └── images/         # Imágenes del proyecto
│
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación


🧑‍💻 Contribución

¡Las contribuciones son bienvenidas!
Si deseas mejorar el proyecto:

Haz un fork del repositorio.

Crea una nueva rama (git checkout -b nueva-funcionalidad).

Realiza tus cambios y haz commit (git commit -m 'Agrega nueva funcionalidad').

Haz push a tu rama (git push origin nueva-funcionalidad).

Abre un Pull Request.

📄 Licencia

Este proyecto está bajo la licencia MIT.
Consulta el archivo LICENSE
 para más detalles.
