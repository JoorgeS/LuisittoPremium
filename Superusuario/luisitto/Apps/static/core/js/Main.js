const Showpass = () => {
document.querySelector('#eye').addEventListener('click', l => {
    const passwordInput = document.querySelector('.pass');
    if (l.target.classList.contains('show')) {
        l.target.classList.remove('show');
        passwordInput.type = 'text';
    } else {
        l.target.classList.add('show');
        passwordInput.type = 'password';
    }
})
};


document.querySelector('.menubtn').addEventListener('click', () => {
    document.querySelector('.nav-menu').classList.toggle('show');
});


ScrollReveal().reveal('.carousel-inner', { delay: 500 });
ScrollReveal().reveal('.main-content', { delay: 500 });
ScrollReveal().reveal('.cards', { delay: 500 });
ScrollReveal().reveal('.content-section', { delay: 500 });
ScrollReveal().reveal('.tituloTyC', { delay: 500 });
ScrollReveal().reveal('.parrafos', { delay: 500 });
ScrollReveal().reveal('.Somos', { delay: 500 });
ScrollReveal().reveal('.image-Logo', { delay: 500 });
ScrollReveal().reveal('.headline', { delay: 500 });
ScrollReveal().reveal('.headline', { delay: 500 });


//Desplegar informacion terminos y condiciones//
$(document).ready(() => {
	$('#myBtn').click(function() {
		$('#hidetext').show();
		$('#myBtn').hide();


		$('#parrafos').show('slow')
	});
});

//Suscribirse Realizado con JQUERY//

$('#validate').click(function() {

    var regex = /[\w-\.]{2,}@([\w-]{2,}\.)*([\w-]{2,}\.)[\w-]{2,4}/;

    if (regex.test($('#email').val().trim())) {
        Swal.fire(
			'Good job!',
			'Su correo se ha enviado exitosamente!',
			'success'
		  )

    } else {
        Swal.fire({
			icon: 'error',
			title: 'No pudimos procesar su solicitud',
			text: 'escribe un correo valido e intentalo nuevamente!',
			footer: '<a href="">¿Necesitas ayuda?</a>'
		  })
    }
});

/*/Alerta CRUD
let text = "¿Seguro que quieres eliminar la cuenta?";
  if (confirm(text) == true) {
    ;
  } else {
    text = "You canceled!";*/



//Contacto JS//
const formulario = document.getElementById('formulario');
const inputs = document.querySelectorAll('#formulario input');

const expresiones = {
	usuario: /^[a-zA-Z0-9\_\-]{4,16}$/, // Letras, numeros, guion y guion_bajo
	nombre: /^[a-zA-ZÀ-ÿ\s]{1,40}$/, // Letras y espacios, pueden llevar acentos.
	password: /^.{4,12}$/, // 4 a 12 digitos.
	correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
	telefono: /^\d{7,14}$/, // 7 a 14 numeros. 
	correoContacto: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/
}

const campos = {
	usuario: false,
	nombre: false,
	password: false,
	correo: false,
	telefono: false,
	correoContacto: false
}

const validarFormulario = (e) => {
	switch (e.target.name) {
		case "usuario":
			validarCampo(expresiones.usuario, e.target, 'usuario');
		break;
		case "nombre":
			validarCampo(expresiones.nombre, e.target, 'nombre');
		break;
		case "password":
			validarCampo(expresiones.password, e.target, 'password');
			validarPassword2();
		break;
		case "password2":
			validarPassword2();
		break;
		case "correo":
			validarCampo(expresiones.correo, e.target, 'correo');
		break;
		case "telefono":
			validarCampo(expresiones.telefono, e.target, 'telefono');
		break;
		case "correoContacto":
			validarCampo(expresiones.correoContacto, e.target, 'correoContacto')
		break;
	}
}

const validarCampo = (expresion, input, campo) => {
	if(expresion.test(input.value)){
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos[campo] = true;
	} else {
		document.getElementById(`grupo__${campo}`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__${campo}`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__${campo} i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__${campo} i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__${campo} .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos[campo] = false;
	}
}

const validarPassword2 = () => {
	const inputPassword1 = document.getElementById('password');
	const inputPassword2 = document.getElementById('password2');

	if(inputPassword1.value !== inputPassword2.value){
		document.getElementById(`grupo__password2`).classList.add('formulario__grupo-incorrecto');
		document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-correcto');
		document.querySelector(`#grupo__password2 i`).classList.add('fa-times-circle');
		document.querySelector(`#grupo__password2 i`).classList.remove('fa-check-circle');
		document.querySelector(`#grupo__password2 .formulario__input-error`).classList.add('formulario__input-error-activo');
		campos['password'] = false;
	} else {
		document.getElementById(`grupo__password2`).classList.remove('formulario__grupo-incorrecto');
		document.getElementById(`grupo__password2`).classList.add('formulario__grupo-correcto');
		document.querySelector(`#grupo__password2 i`).classList.remove('fa-times-circle');
		document.querySelector(`#grupo__password2 i`).classList.add('fa-check-circle');
		document.querySelector(`#grupo__password2 .formulario__input-error`).classList.remove('formulario__input-error-activo');
		campos['password'] = true;
	}
}

inputs.forEach((input) => {
	input.addEventListener('keyup', validarFormulario);
	input.addEventListener('blur', validarFormulario);
});

formulario.addEventListener('submit', (e) => {
	e.preventDefault();

	const terminos = document.getElementById('terminos');
	if(campos.usuario && campos.nombre && campos.password && campos.correo && campos.telefono && terminos.checked ){
		formulario.reset();

		document.getElementById('formulario__mensaje-exito').classList.add('formulario__mensaje-exito-activo');
		setTimeout(() => {
			document.getElementById('formulario__mensaje-exito').classList.remove('formulario__mensaje-exito-activo');
		}, 5000);

		document.querySelectorAll('.formulario__grupo-correcto').forEach((icono) => {
			icono.classList.remove('formulario__grupo-correcto');
		});
	} else {
		document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
	}
});

