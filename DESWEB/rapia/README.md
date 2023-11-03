# RapiAlimentos

Es la recien creada nueva red de supermercados #RapiAliemntos con la cual se podra llevar alimentos a todo chile,
mejorando la calidad de servicios de delivery en paginas web a otro nivel, destacando en la rapidez y lo efectivo que es en la compra de ltus productos, que con un solo click ya tendras todo listo y no tendras esos tediosos tiempos de espera. 

El fin de la empresa es el logra la facilidad de la compra de insumos basicos en general, tales como, Comida, ropa, electrodimesticos, muebles, etc.., y lo mejor es al precio mas barato. 


#WHATS NEW??

# V 1.1
04-10-2023

Html 
se mejor la interfaz haciendola mas atractivo y moderna para el usuario, 

Actualizaciones

se agrego elementos de conctato, productos y un nuevo html de inicio de sesion y registro de usuario,

JavaScript

Se ha implementado la funcionalidad del carrito hacienque se agregen productos y dependia del valor del producto se calcula un costo total de compra, se implemento la funcion de contacto a la empresa y se conecto mediante el usa fecht a la base de datos

PHP

se creo el archivo Conexion.php con el proposito enviar nuevos registros de usuario a la base de datos.

Css 

Cambio de color de las poaginas:
  - inicio
  - productos
  - contactos
  - carrito
  - inicio sesion
    




# V 1.0
30-8-2023






Introducción

UML
Diagrama de casos de uso.
En el diagrama de uso proporcionado se representa un sistema que gestiona la venta de insumos a través de una página web. Esta plataforma cuenta con una base de datos que almacena todos los productos disponibles, junto con sus respectivas categorías. Los usuarios pueden acceder a esta información detallada, incluyendo categoría, nombre, precio, etc.
El proceso de compra se inicia cuando el cliente explora los productos y selecciona aquellos que le interesan. Estos productos seleccionados se agregan a un carrito virtual, lo que permite al cliente tener una vista consolidada de los elementos que planea adquirir. Esto también facilita el cálculo del total de la compra.
Una vez que el cliente ha finalizado su selección y está listo para realizar el pago, se procede a la transacción. Después de que el pago se haya completado con éxito, la página web notifica al sistema sobre la transacción exitosa. En este punto, la base de datos marca los productos seleccionados cómo vendidos, actualizando su estado en el inventario.
Adicionalmente, el sistema genera automáticamente una boleta o factura electrónica que documenta los detalles de la compra, como los productos adquiridos, sus precios individuales y el monto total. Esta boleta o factura se envía al cliente, completando así el proceso de compra y venta de los insumos a través de la página web.
Diagrama de clases
Este diagrama consiste en obtener la posible cantidad básica de datos y de métodos para cumplir la función del programa.
Para empezar el usuario básicamente se sabrá su nombre, apellido, correo,  número de tarjeta de crédito, lista de compra, el producto, precio, fecha, nombre del producto con sus respectivos tipos de datos, como String, Integer, etc...
Una vez hecho se debe usar los métodos creados para hacer funcionar el sitio web. dar la información que es requerida o se debe proveer. 


MER
Se ha diseñado un modelo entidad-relación exhaustivo que establece la estructura de la base de datos de nuestro supermercado. Al registrar nuevos usuarios, se requerirá información clave, incluyendo su rut, nombre, apellidos paterno y materno, correo electrónico, contraseña y el id de su ciudad de residencia. Cada ciudad estará representada por su propio id, nombre y referencia al id de la región a la que pertenece. De manera similar, las regiones se definirán por su id único y nombre identificativo.
El sistema también contempla la categorización de productos. Cada categoría dispondrá de un id distintivo, su nombre descriptivo y la relación con los id de los productos asociados a esa categoría. En la entidad "productos", se almacenará el id del producto, su nombre y el precio correspondiente.
La funcionalidad de carrito de compras se refleja en la entidad "carrito". Aquí se consignarán el id del carrito en sí y los id de los productos que un usuario ha seleccionado para adquirir. Para el proceso de venta, se utilizará la entidad "venta", que contendrá su id único, la fecha en que se efectuó y el id del carrito relacionado.
Para documentar las transacciones, se introducirá la entidad "boleta de venta" o "factura electrónica". Cada boleta tendrá su propio id para su identificación única. Además, se vinculó con el id de la venta correspondiente, el rut del cliente involucrado y los id de los productos que han sido comprados en esa transacción en particular.




Interfaz gráfica de la página web
Nuestra base de código está compuesta por lenguajes HTML y CSS, y en estos últimos días, hemos logrado desarrollar una interfaz básica que refleja la idea inicial de lo que aspiramos como equipo para nuestra página web. Justo debajo del título principal, hemos establecido parámetros clave que albergan los distintos enlaces esenciales, tales como "Inicio", "Productos", "Carrito" y "Contacto". Además, hemos proporcionado una vista previa de cómo planeamos llevar a cabo la promoción y posterior venta de nuestros productos. En esta sección, cada artículo se presenta con una imagen ilustrativa, su nombre, una breve descripción, el precio correspondiente y un botón que facilita la inclusión directa en el carrito de compras. 
Posteriormente, en la parte inferior de la página, hemos reservado un espacio para un mensaje de copyright que certifica nuestros derechos en relación al diseño web de esta plataforma. Este mensaje refuerza nuestra autoría y compromiso en la creación y desarrollo de esta experiencia en línea.



