//productos
const productos = [
    {
        id: "prod-1", //bd id
        titulo: "manzana", //bd nombre
        imagen: "../manzana.jpg", //ruta de la img
        precio: "500" //bd precio
    },
    {
        id: "prod-2", //bd id
        titulo: "pera", //bd nombre
        imagen: "../pera.jpg", //ruta de la img
        precio: "700" //bd precio 
    }
]

const mainContent = document.querySelector("#main-content");
let botonesAgregar = document.querySelectorAll(".producto-agregar");

function mostrarProductos(){
    productos.forEach(producto =>{

        const div = document.createElement("div");
        div.classList.add("producto");
        div.innerHTML = `
        <img class="producto-imagen" src="${producto.imagen}" alt="${producto.titulo}">
        <div class="producto-detalles">
            <h3 class="porducto-titulo">${producto.titulo}</h3>
            <p class="producto-precio">${producto.precio}</p>
            <button class="producto-agregar" id="${producto.id}">Agregar</button>
        </div>
        `;

    mainContent.append(div);
    })

    actualizaBotonesAgregar();
}

mostrarProductos();

function actualizaBotonesAgregar(){
    botonesAgregar = document.querySelectorAll(".producto-agregar")

    botonesAgregar.forEach(boton => {
        boton.addEventListener("click", agregarAlCarrito)
    })
}


let productosCarrito;

let productosEnCarritoALM = localStorage.getItem("productos-en-carrito");

if (productosEnCarritoALM){
    productosCarrito = JSON.parse(productosEnCarritoALM);
} else {
    productosCarrito = [];
}


function agregarAlCarrito(e) {
    const idBoton = e.currentTarget.id;
    const productoAgregado = productos.find(producto => producto.id === idBoton);

    if(productosCarrito.some(producto => producto.id === idBoton)) {
        const index = productosCarrito.findIndex(producto => producto.id === idBoton);
        productosCarrito[index].cantidad++;
    } else{
        productoAgregado.cantidad = 1;
        productosCarrito.push(productoAgregado);
    }

    localStorage.setItem("productos-en-carrito", JSON.stringify(productosCarrito));
}