const burgerButton = document.querySelector('#burger')
const burgerMenu = document.querySelector('.burger_content')
const header = document.querySelector('.header')
burgerButton.addEventListener('click', (e)=>{
    burgerButton.classList.toggle('active')
    document.body.classList.toggle('lock')
    burgerMenu.classList.toggle('active')
    header.classList.toggle('no-radius')
})