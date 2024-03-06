users= [
	{email:"carla@gmail.com", password: "qwerty"}, 
	{email:"john@gmail.com", password: "password"},
	{email: "mike@gmail.com", password: "qwerty"}
]

function checkCredentials(){
	let passwordCin = document.getElementById("passwordInput").value;
	let emailCin = document.getElementById("emailInput").value;
	let messageDiv = document.getElementById( "message" );
	try{
		let user = users.find(user => user.email === emailCin);
		if( user.password ===  passwordCin){
			messageDiv.innerHTML= `Bienvenido ${user.email}!`;
		}else {
			messageDiv.innerHTML= "Contraseña o email incorrectos"
		}
	}catch (e) {
		messageDiv.innerHTML= "Contraseña o email incorrectos"
	}
		
}

