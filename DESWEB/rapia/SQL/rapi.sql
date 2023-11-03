--OJO ESTA TABLA ES SOLO DE PRUEBA, HASTA QUE SE DEFINA QUE BD USAREMOS

CREATE TABLE Categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

CREATE TABLE Productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    img VARCHAR(255) NOT NULL,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
);

INSERT INTO Categorias (nombre) VALUES
('Frutas'),
('Lácteos'),
('Productos de Limpieza');

INSERT INTO Productos (nombre, precio, img, categoria_id) VALUES
('Manzanas', 1000,"https://fruverhome.co/wp-content/uploads/2020/08/Manzana-roja-x-05-kg.jpg", 1), 
('Leche Entera', 2500, "https://images.lider.cl/wmtcl?source=url[file:/productos/5101a.jpg]&scale=size[2000x2000]&sink", 2),
('Detergente Líquido', "https://images-na.ssl-images-amazon.com/images/I/81Hp7saZCdL._AC_SL1500_.jpg", 5000, 3); 