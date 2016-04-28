$(document).ready(function(){
	time=setInterval(update,60000);
	

	// function for update share price
	function update(){
		console.log('request send')
		$.ajax({
			url: "/nse/",
			type : "POST",
			data : {action : "update"} ,
			success: function(shares){
				console.log(shares.length)
				for (var i = 0; i < shares.length; i++) {
					id = i+1;
					$('#share_'+ id.toString() + ' td[2]').text(shares[i].name)
					$('#share_'+ id.toString() + ' td[3]').text(shares[i].price)
					$('#share_'+ id.toString() + ' td[4]').text(shares[i].max)
					console.log(shares[i])
				}
        	},
        	error : function(xhr,errmsg,err){
        		console.log('error')
        		console.log(xhr.responseText);
        	}
    });
	}
})