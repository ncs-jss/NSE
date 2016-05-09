$(document).ready(function(){
	update()
	$("#tabs").tabs();
	var value;
	$("#sell_button").click(function(){
		event.preventDefault();
		quant = $(this).prev().val()
		code  = value
		sell(code,quant)
	})
	$("#buy_button").click(function(){
		event.preventDefault();
		quant = $(this).prev().val()
		code  = value
		buy(code,quant)
	})
	$("button.trade").click(function(){
		value = $(this).nextAll('input').val()
		$('#buy_error').text("")
		$('#sell_error').text("")
		$("#buy_button").prev().val("");
		$("#sell_button").prev().val("");
		name = $(this).attr('name')
		if (name == "buy"){
			a = $("#buy_dailog").dialog({autoOpen:false,title:"Nibble Stock exchange"});
		}
		else {
			a = $("#sell_dailog").dialog({autoOpen:false,title:"Nibble Stock exchange"});
		}
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
					if (parseFloat(shares[i].price) >  parseFloat(old_value)){
						$('#stocks ' + '#share_'+ id.toString()).removeClass('danger')
						$('#stocks ' + '#share_'+ id.toString()).addClass('sucess')
					}
					else if (parseFloat(shares[i].price) <  parseFloat(old_value)) {
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
			url: "/nse/buy/",
			type:"POST",
			data : {code : code, quant : quant},
			success : function(response){
				if (response.status == "sucess") {
					$("#buy_dailog").dialog('close');
					$("#blnce").text(response.blnce)
				}
				else {
					$('#buy_error').text(response.status)
				}
			},
			error : function(xhr,errmsg,err){
        		console.log('error')
        		console.log(xhr.responseText);
        	}
		})
	}
	function sell(code,quant){
		$.ajax({
			url: "/nse/sell/",
			type:"POST",
			data : {code : code, quant : quant},
			success : function(response){
				if (response.status == "sucess") {
					$("#sell_dailog").dialog('close');
					$("#blnce").text(response.blnce)
				}
				else {
					$('#sell_error').text(response.status)
				}
			},
			error : function(xhr,errmsg,err){
        		console.log('error')
        		console.log(xhr.responseText);
        	}
		})
	}
})