
// 默认聚焦账户
jQuery(function() {
	jQuery('input[name=email]').focus();
});

$(document).ready(function() {
	// Check if JavaScript is enabled
	$('body').addClass('js');
	// Make the checkbox checked on load
	$('.login-form span').addClass('checked').children('input').attr('checked', true);
	// Click function
	$('.login-form span').on('click', function() {
		if ($(this).children('input').attr('checked')) {
			$(this).children('input').attr('checked', false);
			$(this).removeClass('checked');
		}
		else {
			$(this).children('input').attr('checked', true);
			$(this).addClass('checked');
		}
	});
	//shake the login form
	if($('.error')[0]){
		$('#login-form').effect('shake', null, 100, null );
	}	
});

// 提交检查
jQuery(function() {
	var form = jQuery('form[name=login]'),
		emailReg = /^([\w-])+(\.\w+)*@([\w-])+((\.\w+)+)$/,
		emailInput = form.find('input[name=email]'),
		passwordInput = form.find('input[name=password]');
	
	form.submit(function() {
		// 获取用户填写的账户信息
		var email = jQuery.trim(emailInput.val()),
			password = jQuery.trim(passwordInput.val());
		
		// 检查email
		if(emailReg.test(email) === false) {
			emailInput.focus();
			return false;
		}		
		
		// 检查密码
		if(!(password.length >=6&&password.length<=20)) {			
			passwordInput.focus();
			return false;
		}
		
		// 加密密码
		var ciphertext = calcMD5(password);
		form.append('<input type="hidden" name="password" value="' + ciphertext + '" />');
		form.append('<input type="hidden" name="isCipher" value="true" />');
		passwordInput.removeAttr('name');
		
		return true;;
	});
});