var account;

get_credentials = function(){
	account_id = account.replace(/\s/g, "_")
	strId ="#" + account_id + "_form"
	credentials = {}	
	$(strId + " input").each(function( index ) {		
		strIndexId = "#" + account_id + "_" + index
		input = $(strIndexId)
		credentials['name'] = account
		credentials[input.attr('name')] = input.val()
	});	
	validate_credentials(credentials)	
}

validate_credentials = function(credentials){
	account_id = credentials['name'].replace(/\s/g, "_")
	$.ajax({
	    // la URL para la petición
	    url : '/credentials',
	 
	    // la información a enviar
	    // (también es posible utilizar una cadena de datos)
	    data : credentials,
	 
	    // especifica si será una petición POST o GET
	    type : 'POST',
	 
	    // el tipo de información que se espera de respuesta
	    dataType : 'json',
	 
	    // código a ejecutar si la petición es satisfactoria;
	    // la respuesta es pasada como argumento a la función
	    success : function(json) {
	       	accounts_table.show()
			location.reload()	       
	    },
	 
	    // código a ejecutar si la petición falla;
	    // son pasados como argumentos a la función
	    // el objeto de la petición en crudo y código de estatus de la petición
	    error : function(xhr, status) {	        
	        return false;
	    },
	 
	    // código a ejecutar sin importar si la petición falló o no
	    complete : function(xhr, status) {}
	});
}

syncAccount = function(token, name){
	$.ajax({
	    // la URL para la petición
	    url : '/sync_account',
	 
	    // la información a enviar
	    // (también es posible utilizar una cadena de datos)
	    data : {'token': token, 'name': name},
	 
	    // especifica si será una petición POST o GET
	    type : 'POST',
	 
	    // el tipo de información que se espera de respuesta
	    dataType : 'json',
	 
	    // código a ejecutar si la petición es satisfactoria;
	    // la respuesta es pasada como argumento a la función
	    success : function(json) {	       		       		       	
	    },
	 
	    // código a ejecutar si la petición falla;
	    // son pasados como argumentos a la función
	    // el objeto de la petición en crudo y código de estatus de la petición
	    error : function(xhr, status) {	        
	        return false;
	    },
	 
	    // código a ejecutar sin importar si la petición falló o no
	    complete : function(xhr, status) {	        
	    }
	});
}

//// BUTTONS LOGIC:
$('.btn-xs').click(function() {
	// reference clicked button via: $(this)
	var account_reference = $(this).attr('id');	
	var button_type = $(this).attr('name');
	var id_site = $(this).attr('value');
	var input = $("#" + account_reference.replace(/\s/g, "_") + "_token");
	if(~button_type.indexOf('_sync')){		
		syncAccount(input.val(), account_reference)
	}else if(~button_type.indexOf('_see')){
		var url = '/accounts/' + id_site
		window.location.href = url
		//get_accounts(id_site)
	}
});	

// GET ACCOUNT FROM DROPDOWN:
$("#accounts li").click(function() {
	account = $(this).text().trim()    
});

// HIDE TABLE:
var accounts_table = $("#accounts_table");
var tbody = $("#accounts_table tbody");
if (tbody.children().length == 0) {	
	accounts_table.hide()    
}



