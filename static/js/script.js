
function closeButton(button){
    let alert = button.closest('.alert');
    alert.style.display = 'none';
}
$(document).ready(function(){
    

    $('#logout').on('click', function(e){
        e.preventDefault();
        if (confirm("Are you sure to logout?")){
            window.location.href = $(this).attr('href')
        }
    })
})