let productosCarrito = localStorage.getItem("productos-en-carrito");
productosCarrito = JSON.parse(productosCarrito);

const carritoVacio = document.querySelector("#carrito-vacio");
const carritoProductos = document.querySelector("#carrito-productos");
const carritoAciones = document.querySelector("#carrito-acciones");
let botonEliminar = document.querySelectorAll(".carrito-producto-eliminar");
const botonVaciar = document.querySelector("#carrito-acciones-vaciar");
const total = document.querySelector("#total");
const botonComprar = document.querySelector("#carrito-acciones-comprar");

function cargarProductosCarrito(){
    if (productosCarrito && productosCarrito.length > 0) {

        carritoVacio.classList.add("disabled");
        carritoProductos.classList.remove("disabled");
        carritoAciones.classList.remove("disabled");
    
        carritoProductos.innerHTML = "";
    
        productosCarrito.forEach(producto => {
        const div = document.createElement("div");
        div.classList.add("carrito-producto");
        div.innerHTML = `
            <img class="carrito-producto-imagen" src="${producto.imagen}" alt="${producto.titulo}">
            <div class="carrito-producto-titulo">
                <small>Producto</small>
                <h3>${producto.titulo}</h3>
            </div>
            <div class="carrito-producto-cantidad">
                <small>Cantidad</small>
                <p>${producto.cantidad}</p>
            </div>
            <div class="carrito-producto-precio">
                <small>Precio</small>
                <p>${producto.precio}</p>
            </div>
            <div class="carrito-producto-subtotal">
                <small>Subtotal</small>
                <p>${producto.precio *producto.cantidad}</p>
            </div>
            <button class="carrito-producto-eliminar" id="${producto.id}"><i class="bi bi-trash-fill"></i></button>
            `;
    
        carritoProductos.append(div);
        })
    } else{
    
        carritoVacio.classList.remove("disabled");
        carritoProductos.classList.add("disabled");
        carritoAciones.classList.add("disabled");
    }

    actualizaBotonesEliminar();
    actualizaTotal();
}

cargarProductosCarrito();

function actualizaBotonesEliminar(){
    botonEliminar = document.querySelectorAll(".carrito-producto-eliminar")

    botonEliminar.forEach(boton => {
        boton.addEventListener("click", eliminarDelCarrito);
    });
}

function eliminarDelCarrito(e){
    const idBoton = e.currentTarget.id;
    const index = productosCarrito.findIndex(producto => producto.id === idBoton);

    productosCarrito.splice(index, 1);
    cargarProductosCarrito();

    localStorage.setItem("productos-en-carrito", JSON.stringify(productosCarrito));
}

botonVaciar.addEventListener("click", vaciarCarrito);

function vaciarCarrito(){
    productosCarrito.length = 0;
    localStorage.setItem("productos-en-carrito", JSON.stringify(productosCarrito));
    cargarProductosCarrito();
}

function actualizaTotal(){
    const totalFinal = productosCarrito.reduce((acc, producto) => acc + (producto.precio * producto.cantidad), 0);
    total.innerText = `$${totalFinal}`;
}

botonComprar.addEventListener("click", comprarCarrito);

function comprarCarrito(){
    productosCarrito.length = 0;
    localStorage.setItem("productos-en-carrito", JSON.stringify(productosCarrito));

    carritoVacio.classList.remove("disabled");
    carritoProductos.classList.add("disabled");
    carritoAciones.classList.add("disabled");

    alert("gracias por su compra");
}