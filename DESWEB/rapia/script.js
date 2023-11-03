
let items = []; 
const cartItemsContainer = document.querySelector('.cart-items');
 

function loadCart() {
    if (localStorage.getItem('cartItems')) {
        items = JSON.parse(localStorage.getItem('cartItems'));
        updateCart();
    }
}


function updateCart() {
    cartItemsContainer.innerHTML = ''; 

    items.forEach(item => {
        const cartItem = document.createElement('div');
        cartItem.classList.add('cart-item');
        cartItem.innerHTML = `
            <img src="${item.image}" alt="${item.name}">
            <span>${item.name} - $${item.price}</span>
        `;
        cartItemsContainer.appendChild(cartItem);
    });


    const cartIcon = document.getElementById('cart-icon');
    cartIcon.setAttribute('title', `Elementos en el carrito: ${items.length}`);
}


window.addEventListener('load', loadCart);


const cartIcon = document.querySelector('.cart svg');
const cartItems = document.querySelector('.cart .cart-items');

cartIcon.addEventListener('click', () => {
    cartItems.classList.toggle('active');
});



fetch('pagina2.php', {
    method: 'POST',
    headers: {
    'Content-Type': 'application/json'
    },
    body: JSON.stringify({ key: 'value' })
   })
   .then(response => response.json())
   .then(data => console.log(data))
   .catch(error => console.error('Error:', error));
