$(document).ready(function(){
	$("#tabs").tabs();
	var value;
	$("#buy_button").click(function(){
		event.preventDefault();
		quant = $(this).prev().val()
		code  = value
		buy(code,quant)
	})
	$("button").click(function(){
		value = $(this).next().val()
		a = $("#buy_dailog").dialog({autoOpen:false,title:"Nibble Stock exchange"});
		a.dialog('open');
	})
	time=setInterval(update,10000);
	// function for update share price
	function update(){
		console.log('request send')
		$.ajax({
			url: "/nse/",
			type : "POST",
			data : {action : "update"},
			success: function(shares){
				for (var i = 0; i < shares.length; i++) {
					id = i+1;
					var old_value = $('#stocks ' +'#share_' + id.toString() + ' td:nth-child(3)').text()
					if (parseFloat(shares[i].price) >=  parseFloat(old_value)){
						$('#stocks ' + '#share_'+ id.toString()).removeClass('danger')
						$('#stocks ' + '#share_'+ id.toString()).addClass('sucess')
					}
					else {
						$('#stocks ' + '#share_'+ id.toString()).removeClass('sucess')
						$('#stocks ' + '#share_'+ id.toString()).addClass('danger')
					}
					$('#stocks ' + '#share_'+ id.toString() + " td:nth-child(2)").text(shares[i].name)
					$('#stocks ' + '#share_'+ id.toString() + ' td:nth-child(3)').text(shares[i].price)
					$('#stocks ' + '#share_'+ id.toString() + ' td:nth-child(4)').text(shares[i].max)
					//console.log(shares[i])
				}
        	},
        	error : function(xhr,errmsg,err){
        		console.log('error')
        		console.log(xhr.responseText);
        	}
    });
	}

	function buy(code,quant){
		$.ajax({
			url: "/nse/",
			type:"POST",
			data : {action : "buy",code : code, quant : quant},
			success : function(response){
				if (response.status == "sucess") {
					$("#buy_dailog").dialog('close');
				}
				else {
					$('#error').text(response.status)
					console.log(response)
				}
			},
			error : function(xhr,errmsg,err){
        		console.log('error')
        		console.log(xhr.responseText);
        	}
		})
	}
})