Home Seek

Objetivo Funcional
Home Seek es una plataforma diseñada para publicar, tasar y encontrar viviendas para compra y/o alquiler. Su objetivo es facilitar el proceso de búsqueda de vivienda, proporcionando herramientas útiles tanto para compradores y arrendatarios como para vendedores y arrendadores.

Descripción General
Este proyecto ofrece una interfaz sencilla para que los usuarios puedan explorar propiedades disponibles para alquilar o comprar, así como tasar propiedades para entender mejor su valor en el mercado actual. Con funcionalidades como búsqueda avanzada, publicación de propiedades y tasación instantánea.

Tecnologías Utilizadas
	•	Backend: Django (Python)
	•	Base de Datos: SQLite
	•	Frontend: HTML, CSS, Bootstrap para el diseño responsive
	•	Autenticación: Sistema de autenticación de Django para el manejo de usuarios y sesiones

Descripción de los Modelos
	•	Alquilar: Representa las propiedades disponibles para alquilar, incluyendo información como tipo de propiedad, metros cuadrados y precio.
	•	Comprar: Similar al modelo Alquilar, pero dedicado a propiedades en venta.
	•	Tasar: Utilizado para solicitar tasaciones de propiedades, almacenando datos relevantes para realizar la valoración.
	•	Profile: Extiende el modelo de usuario de Django para incluir información adicional del perfil, como avatar, nombre y correo electrónico.

Instrucciones de Instalación y Configuración

Para ejecutar este proyecto localmente, sigue estos pasos:
		Clona el repositorio en tu máquina local.
		Asegúrate de tener Python y Django instalados.
		Navega al directorio del proyecto y ejecuta python manage.py migrate para configurar la base de datos.
		Inicia el servidor con python manage.py runserver.
		Abre tu navegador y visita http://127.0.0.1:8000/ para acceder a la aplicación.

Cómo Usar
	•	Para usuarios buscando propiedades: Navega a través de las secciones de alquilar o comprar para explorar las propiedades disponibles. Utiliza la función de búsqueda para filtrar por tipo de propiedad, ubicación, etc.
	•	Para propietarios: Regístrate y accede al sistema para publicar tus propiedades en alquiler o venta. También puedes solicitar tasaciones para conocer el valor de mercado de tus propiedades.
	•	Administración: Accede al panel de administración con el usuario admin y la contraseña admin para gestionar usuarios, propiedades y solicitudes de tasación.

Usuario Administrador y Contraseña
	•	Usuario: admin
	•	Contraseña: admin
