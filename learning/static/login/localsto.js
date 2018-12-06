document.getElementById("email").value = localStorage.getItem("email");
function login(ev){
	ev.preventDefault()
	var data={
		email: document.forms["myform"]["email"].value,
		password:document.forms["myform"]["password"].value
	}
$.post('/update_session/', function(data) {
    alert(data);
});
	var token = document.getElementsByName("csrfmiddlewaretoken")[0].value ;
    // alert("token: "+x);

    //  "Content-Type": "application/json; charset=utf-8",
	console.log(data)
	// fetch('http://127.0.0.1:8000/login/', {
	fetch("/login/", {	
	        method: "POST", 
	        headers: {
	        	"X-CSRFToken":token,
	            "Content-Type": "application/json; charset=utf-8",
	        },
	      	body: JSON.stringify(data), // body data type must match "Content-Type" header
	    })
	    .then(response => response.json())
	    .then(response => {
	    
	    	console.log(response.status)//{status: 200, userId: 27, message: "Dear gudal sharma, we successfully mailed your password"}
	    	console.log(response)
	    	if (response.status==200){//user found
	    		localStorage.clear()
	    		var email=response.email
	    		if (response.active==true)
	    			alert("user login")
	    		else
	    			alert("user decitvated")
	    		
	    		//save user id in localstorage
	    		if (typeof(Storage) !== "undefined") {
				    // Store
				   sessionStorage.setItem("userId", response.userId);
				   alert(response.userId);
				    console.log("userId successfully saved into localstorage..")
				    console.log('login/home/')
				    window.location.href = 'home/';
				    return true;
				} else {
				    alert("Sorry, your browser does not support Web Storage...")
				}
			}

	    	else{
	    		alert("user does not exist")
	    		return false
	    	}
	    	// else{
	    	// 	alert("user is decitvated")
	    	// 	return false
	    	// }

	    })
	    .catch(err => {
	    	console.log("error: " + err)
	    	return false
	    });
}





