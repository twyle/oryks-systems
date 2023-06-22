const toggleButton = document.querySelector('.toggle-btn')
const navMenu = document.querySelector('.nav-menu')

toggleButton.addEventListener('click', () => {
    navMenu.classList.toggle('active')
})
