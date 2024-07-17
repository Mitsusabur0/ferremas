# FERREMAS - Plataforma de Comercio Electrónico

## Descripción del Proyecto

FERREMAS es una distribuidora líder de productos de ferretería y construcción en Chile, con más de 40 años de experiencia en el mercado. Este proyecto tiene como objetivo desarrollar una plataforma de comercio electrónico robusta y eficiente para FERREMAS, permitiéndoles adaptarse a las nuevas demandas del mercado y superar los desafíos presentados por la pandemia de COVID-19.

## Tecnologías Utilizadas

- **Lenguajes de Programación:**
  - Python
  - JavaScript
  - HTML
  - CSS

- **Base de Datos:**
  - SQLite

- **Framework:**
  - Django

## Arquitectura

El proyecto sigue una arquitectura basada en el patrón Modelo-Vista-Controlador (MVC), que se adapta perfectamente al framework Django utilizado. Esta arquitectura permite una separación clara de las responsabilidades y facilita el mantenimiento y escalabilidad del sistema.

## Pasos de Implementación

1. **Análisis y Planificación:**
   - Creación de diagramas BPMN "AS IS" para representar el modelo actual de la tienda.
   - Desarrollo de diagramas BPMN "TO BE" para visualizar el nuevo flujo de procesos con la plataforma de e-commerce.

2. **Diseño:**
   - Diseño de la arquitectura del sistema.
   - Creación de mockups y prototipos de la interfaz de usuario.

3. **Desarrollo:**
   - Implementación del backend utilizando Django.
   - Desarrollo del frontend con HTML, CSS y JavaScript.
   - Integración de la base de datos.
   - El sistema posee 4 apps de Django: 
      - ferremas_project (app del projecto).
      - tienda (app principal, donde se genera la funcionalidad del catálogo, usuarios, ofertas, etc).
      - carro (app donde se desarrolla el carro de compras).
      - pago (app donde se desarolla el pago del carro de compras).
   - La administración del sitio se realiza a través del panel de administración de Django (se creó un superuser -usuario:admin, password:javalist- para realizar todos los procesos de administración en url "/admin").
   - El admin puede asignar un grupo a cada usuario registrado. Con estos grupos se le dan los permisos correspondientes a cada staff de la tienda, para que puedan realizar sus tareas correspondientes en el panel de administración.
   - Se crea una API propia que devuelve un JSON del catálogo completo de productos (url= "/api/productos"), y también de cada producto (url= "/api/productos/id"). El id de cada producto se obtiene de la lista de todos los productos.
   - Se convierte la moneda a USD utilizando la API del sitio "https://api.exchangerate-api.com/v4/latest/usd" y las librerías requests y json

4. **Pruebas:**
   - Realización de pruebas unitarias y de integración.
      - Estas pruebas se realizan con el sistema de pruebas integrado del framework Django (las pruebas están en "tienda/tests.py").
   - Pruebas de usuario para garantizar una experiencia fluida.
      - Pruebas manuales del funcionamiento fluido de la app.

## Instalación y Configuración

Es un proyecto django. Se deben instalar todas las librerías y dependencias para que funcione correctamente (con pip install u otro).
