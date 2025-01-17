document.addEventListener('DOMContentLoaded', function() {
    /* Formulario */ 
    var formulario = document.getElementById('test-form');
    
    /* Inputs */ 
    var inp_email = document.getElementById('email');

    /* MSGs de errores */
    var msg_error_email_null = document.querySelector('.msg_error_email_null');
    var msg_error_email_fomat = document.querySelector('.msg_error_email_format');

    /* Errores condicionales */
    var error_email_null = false;
    var error_email_format = false;

    function validarEmail(){

        /* MANEJO DE ERRORES (email vacío) */
        if (inp_email.value.length < 1) {
            msg_error_email_null.classList.remove('invisible');
            error_email_null = true
        } else {
            msg_error_email_null.classList.add('invisible');
            error_email_null = false
        }
    
        /* MANEJO DE ERRORES (formato válido) */
        if (!inp_email.value.includes('@') || !inp_email.value.includes('.')){
            msg_error_email_fomat.classList.remove('invisible');
            error_email_format = true;
        } else {
            msg_error_email_fomat.classList.add('invisible');
            error_email_format = false;
        }

        /* Agregar la clase error al input si hay un error */ 
        if (error_email_null || error_email_format) {
            inp_email.classList.add('error');
        } else {
            inp_email.classList.remove('error');
        }
    }

    /* Evento al enviar el formulario */
    formulario.addEventListener('submit', function(event) {
        event.preventDefault();
    
        validarEmail();
    
        /* Verificar si hay errores */
        if (error_email_null || error_email_format) {
            
            inp_email.classList.add('shake');
    
            setTimeout(function() {
                inp_email.classList.remove('shake');
            }, 500);
        } else {
            formulario.submit();
        }
    });
    
});