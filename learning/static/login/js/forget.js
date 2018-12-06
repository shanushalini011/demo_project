document.getElementById("email").value = localStorage.getItem("email");
function requestPassword(event) {
		event.preventDefault();

		var email = document.forms["myform"]["email"].value;
		console.log(email)

		var token = document.getElementsByName("csrfmiddlewaretoken")[0].value ;

		fetch("/forgot-password/", {
			method: "POST",
			headers: {
				"X-CSRFToken":token,
				"Content-Type": "application/json;"-
			},
			body: JSON.stringify(email),
			})
		
		.then(response => response.json())
		.then(response => {
			console.log(response.message)
			console.log(response)
			alert(response.message)

			if(response.status == 200) {
				location.href = "/login/"
			} else {
				location.reload()
				return false
			}
			return true
		})
		.catch(error => {
			console.log("Login error: ", error)
			alert(error)
			return false
		})
	}