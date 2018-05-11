
//Add to app.js
app.post('/form', function(req, res) {
	//call nadeems scripts
    res.send('This is the result nadeem should return');
});

//Add as the last script in html page , add the load and unload
<script type="text/javascript">
    function submitForm(){
    	//data is the data to be sent
    	//loadScreen();
    $.ajax({
        type: 'POST',
        data: JSON.stringify(data),
        url: 'http://localhost:8000/form',                      
        success: function(data) {
            //unloadScreen();
            //displayResults(data);
            console.log('success');
            console.log(JSON.stringify(data));
        }
    });  
    }

</script>

