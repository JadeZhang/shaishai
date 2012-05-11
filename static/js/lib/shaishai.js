shaishai = {
	log : function(_message){
		if('console' in window && 'log' in window.console){
			console.log(_message);
		}
	}
};