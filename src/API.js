//constructor
function API () {
	this.token = "";
	this.endpoint = "https://api.robinhood.com"
	this.UserAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3";
	jQuery.ajaxSetup({ jsonp: null, jsonpCallback: null});
}


//use this to set the token
API.prototype.login = function(username, password){
	/*$http.post(this.endpoint + "/api-token-auth", {"username": username, "password": password})
		 .success(function(data, status, headers, config){
		 	console.log("Data: " + data);
		 	console.log("Status: " + status);
		 	console.log("Headers: " + headers);
		 	console.log("Config: " + config);
		 })
		 .error(function(data, status, headers, config){
		 	console.log("TODO: error");
		 });*/
	
	$.ajax({
		type: "POST",
		url: this.endpoint + "/api-token-auth",
		crossDomain: true,
		beforeSend: function(request){
			request.setRequestHeader("User-Agent", this.UserAgent)

		},
		data: JSON.stringify({"username": username, "password": password}),
		contentType: "application/x-www-form-urlencoded; charset=utf-8",
		dataType: "json",
		success: function(data){
			console.log(data);
		},
		failure: function(errMsg){
			console.log(errMsg)
		}
	});
}