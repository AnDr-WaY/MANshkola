const burgerButton = document.querySelector('#burger')
const burgerMenu = document.querySelector('.burger_content')
burgerButton.addEventListener('click', (e)=>{
    burgerButton.classList.toggle('active')
    document.body.classList.toggle('lock')
    burgerMenu.classList.toggle('active')
})