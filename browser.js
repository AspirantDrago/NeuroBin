var host = 'http://127.0.0.1:8000'

document.getElementsByClassName("pin_text")[0].addEventListener("DOMSubtreeModified", function() {
	var s1 = document.getElementsByClassName("pin_text")[0].textContent;
	var s2;
	if(document.getElementsByClassName("sentiment--text sentiment--text__down").length > 0)
	{
		s2 = document.getElementsByClassName("sentiment--text sentiment--text__down")[0].textContent;
	}else{
		s2 = '50';
	}
	var s3;
	if(document.querySelector(".add-btn__text") != null)
	{
		s3 = document.querySelector(".add-btn__text").textContent;
	}else{
		s3 = document.querySelector("li.pair-tab_selected span.title").textContent;
	}
	s3 = s3.replace(' ', '_');
	var x = new XMLHttpRequest();
	x.open("GET", host + '/api/add/' + s3 + '/val=' + s1 + '&prop=' + s2, true);
	x.send(null);
});