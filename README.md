Orden de Prueba de las Funcionalidades

1. Página de Bienvenida

	•	Ruta: app/
	•	Descripción: Página inicial que da la bienvenida a los usuarios.
	•	Vista: bienvenida en views.py.
	•	Plantilla: bienvenida.html.

2. Registro de Usuario

	•	Ruta: app/ingresar_usuario/
	•	Descripción: Permite a los usuarios registrarse proporcionando información personal.
	•	Vista: ingresar_usuario en views.py.
	•	Plantilla: ingresar_usuario.html.
	•	Modelo: Usuario en models.py.
	•	Formulario: FormularioUsuario en forms.py.

3. Realizar una Publicación

	•	Ruta: app/hacer_posteo/
	•	Descripción: Los usuarios pueden crear nuevas publicaciones con título, imagen y descripción.
	•	Vista: hacer_posteo en views.py.
	•	Plantilla: hacer_posteo.html.
	•	Modelo: Posteo en models.py.
	•	Formulario: FormularioPosteo en forms.py.

4. Tomar el Test de Eneagrama

	•	Ruta: app/hacer_test/
	•	Descripción: Los usuarios pueden completar un test de Eneagrama y guardar sus resultados.
	•	Vista: hacer_test en views.py.
	•	Plantilla: hacer_test.html.
	•	Modelo: Test_Eneagrama en models.py.
	•	Formulario: FormularioTest en forms.py.

5. Buscar un Usuario

	•	Ruta: app/buscar_usuario/
	•	Descripción: Permite buscar usuarios registrados por su nombre de usuario.
	•	Vista: buscar_usuario en views.py.
	•	Plantilla: buscar_usuario.html.
	•	Formulario: FormularioBuscarUsuario en forms.py.

Detalles de las Funcionalidades

	•	Registro de Usuario: Los usuarios pueden registrarse proporcionando su nombre de usuario, nombre completo, correo electrónico, contraseña, género y edad. Los datos se almacenan en el modelo Usuario.
	•	Posteos: Los usuarios pueden crear posteos que incluyen un título, imagen y descripción. Se almacenan en el modelo Posteo.
	•	Test de Eneagrama: Los usuarios pueden ingresar resultados de su test de eneagrama y guardar sus resultados en el modelo Test_Eneagrama.
	•	Búsqueda de Usuarios: Se puede buscar usuarios registrados por su nombre de usuario exacto.
