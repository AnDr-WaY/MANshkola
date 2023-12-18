const scrollDownButton = document.querySelector('.intro_arrow')
const scrollTo = document.querySelector('.wrapper')

scrollDownButton.addEventListener('click', (e)=>{
    scrollTo.scrollIntoView({ behavior: "smooth", block: "start", inline: "start" })
})