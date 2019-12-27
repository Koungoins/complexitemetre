(function(){

	let windowFileProtocolChange = function(c){
		window.location.href = window.location.href.replace('index.html', c);
		console.log(window.location.href)
	}
})();