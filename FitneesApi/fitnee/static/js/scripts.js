function toggleMenu() {
    const menu = document.querySelector('.menu');
    menu.classList.toggle('active');
}

function scrollToContent() {
    const content = document.querySelector('.content');
    if (content) {
        content.scrollIntoView({
            behavior: 'smooth'
        });
    }
}

$(document).ready(function () {
   
    window.setTimeout(function () {
        const $alertMessages = $(".alert");
        
        if ($alertMessages.length > 0) {
            $alertMessages.fadeTo(400, 0).slideUp(400, function () {
                $(this).remove();
                
            });
        } 
    }, 5000); // 5000 milliseconds = 5 seconds
});