

// Sidebar toggle variables
const menuToggler = document.querySelector('.menu-toggler');
const sideBar = document.querySelector('.side-bar');

// page navigation variables
const navItemLinks = document.querySelectorAll('.nav li a')
const page = document.querySelectorAll('.page')

// togglin sidebar in mobile
menuToggler.addEventListener('click', function(){
    sideBar.classList.toggle('active');
})

// page navigation funtionality

for (let i = 0; i < navItemLinks.length; i++) {
    // added onclick event in nav link
    navItemLinks[i].addEventListener('click', function(){
        // collected nav links innertext
        const itemLinkText = this.textContent.toLowerCase();

        // defined page and add active class 
        for (let i = 0; i < page.lenth; i++) {

            // defining page condition
            if (page[i].classList.contains(itemLinkText)){
                // add active class on current page
                page[id].classList.add('active');
                // add active class on clicked van link
                navItemLinks[i].classList.add('active');
            } else {
                // remove active class from other pages
                pages[i].classList.remove('active');
                // remove active class from other nav links
                navItemLinks[i].classList.remove('active');
            }
        }
    })
}
