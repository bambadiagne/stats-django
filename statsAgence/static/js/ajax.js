const url = "{{model_name}}";
$(document).ready(function() {
    $('#example').DataTable();
} );
function showspinner(url)
 {

    event.preventDefault(); 
    let spinner= document.getElementById('spinner');
    spinner.style.display="block";
    spinner.style.width="100%";
    spinner.style.height="100%";
    document.body.style.cursor='none';
    let formData = new FormData();
    
    var csrftoken = '{{ csrf_token }}';
    formData.append("articles",document.getElementById("articles").files[0]);
    formData.append("csrfmiddlewaretoken",csrftoken)
    formData.append("crsf_token",csrftoken)
    axios.post("import/"+url,formData,).then((response) => {
            console.log(response.data);
            window.location=window.location.href
        });
             
 }
 