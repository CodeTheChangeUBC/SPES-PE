
//Calender//////////////
var today = new Date();

$('#calender1').calendar({
	startMode: 'month',
	minDate: new Date(today.getFullYear(), today.getMonth(), today.getDate() - 1),
});

$('#calender2').calendar({
	startMode: 'month',
	minDate: new Date(today.getFullYear(), today.getMonth(), today.getDate() - 1),
});
/////////////////////////


//Masking////////////////
$('#phone').mask('(000) 000-0000');
$('#contact-p').mask('(000) 000-0000');
$('#pcode').mask('AA AAA-AAA');
////////////////////////////

//Text Area/////////////////
function limitWords(id) {
	var maxWords=3;
	var d=document.getElementById(id);
	if ( d.value.split(' ').length > maxWords ) {
		$('#details').css('background-color','#ffd6d6');
		setInterval(function(){ $('#details').css('background-color','#fff');}, 1000);
		t=d.value.split(' ').slice(0,maxWords).join(' ');
		d.value=t;
	}
}
//////////////////////////////


//Auto completion/////////////
$("#add1").keyup(function(){
	if(this.value == "Stanley Park Dining Pavilion"){
		$("#street").val("2nd floor 610 Pipeline Rd");
		$("#city").val("Vancouver");
		$("#pcode").val("BC V6G 1Z4");
	}

	if(this.value == "Stanley Park Nature House on Lost Lagoon"){
		$("#street").val("712 Lost Lagoon Path");
		$("#city").val("Vancouver");
		$("#pcode").val("BC V6G 2S1");
	}

	if(this.value == "#19 Stanley Park Bus Loop"){
		$("#street").val("610 Pipeline Rd");
		$("#city").val("Vancouver");
		$("#pcode").val("BC V6G 1Z4");
	}

});
//////////////////////////////////

//Tags script//////////////
$('.chips-placeholder').material_chip({
	placeholder: 'Enter a tag',
	secondaryPlaceholder: '+Tag',
});
///////////////////////////


//Form Functionality//////
$(function() {
	$("#formSubmit").click(function() {
		var form = $("#dataForm").serializeJSON();
		var tag= $('.chips-placeholder').material_chip('data');
		var tagArr = [];
		for (var i = 0; i < tag.length; i++) {
			tagArr.push(tag[i].tag);
		}
		form["event_tags"] = tagArr ;

		form["event_organizer_phone_number"]=$('#phone').cleanVal();
		form["event_contact_number"]=$('#contact-p').cleanVal();
		form["event_postal_code"]=$('#pcode').cleanVal();

		submitForm(form);
	});

});

function displayResults(data){
	openNav();
	
	console.log(data)
	for(var i =0 ; i < data.successful.length ; i++ ){
		$("#successful-web").prepend('<li class="li-items">'+data.successful[i]+"</li>");
	} 

	for(var i =0 ; i < data.captcha.length ; i++ ){
		$("#captcha-web").prepend('<li class="li-items">'+data.captcha[i]+"</li>");
	} 


	for(var i =0 ; i < data.unsuccessful.length ; i++ ){
		$("#unsuccessful-web").prepend('<li class="li-items">'+data.unsuccessful[i]+"</li>");
	} 

}

function submitForm(formData){
	if ($("#dataForm")[0].checkValidity()){
		loadScreen();
		$.ajax({
			type: 'POST',
			cache : false,
			data: formData,
			url: 'http://localhost:8000/form', 
			error:function(){
				//error
			},                     
			success: function(data) {
				unloadScreen();
				displayResults(data);
			}
		});  
	}
	else
		$("#dataForm")[0].reportValidity();
}


function loadScreen(){
	document.getElementById("loaddiv").className = "loading style-2";
}

function unloadScreen(){
	document.getElementById("loaddiv").className = "";
}


function openNav() {
	document.getElementById("myNav").style.height = "100%";
}
function closeNav() {
	document.getElementById("myNav").style.height = "0%";
}
///////////////////////////////////////////////////

