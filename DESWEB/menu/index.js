let listaElementos = document.querySelectorAll('.list__button--click');

listaElementos.forEach(listElement => {
    listElement.addEventListener('click', ()=>{

        let height = 0;
        let menu = listElement.nextElementSibling;
        console.log(menu.scrollHeight);
        if(menu.clientHeight == "0"){
            height = menu.scrollHeight;
        }

        menu.style.height = height+"px";

    })
});