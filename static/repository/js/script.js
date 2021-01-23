const form_1 = document.getElementById('f1');
const form_2 = document.getElementById('f2');


form_1.addEventListener('submit', e => {
    e.preventDefault();
    
    const xhr = (window.XMLHttpRequest)? 
        new XMLHttpRequest:
        new ActiveXObject("Microsoft.XMLHTTP");
        
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            let status = xhr.status;
            
            if (status === 0 || (status >= 200 && status < 400)) {
                document.getElementById('submit-fav-id').value = xhr.responseText;
            
            }
        }
    };
    
    let url = document.getElementById('urlId').value 
    
    //xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    //xhr.setRequestHeader("Access-Control-Allow-Origin", "http://localhost:8000/");
    xhr.open("GET", url, true);
    xhr.send(null);   
});

form_2.addEventListener('submit', e => {
    e.preventDefault();
    
    const xhr = (window.XMLHttpRequest)? 
        new XMLHttpRequest:
        new ActiveXObject("Microsoft.XMLHTTP");
        
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            let status = xhr.status;
            
            if (status === 0 || (status >= 200 && status < 400)) {
                document.getElementById('submit-vms-id').value = xhr.responseText;
            }
        }
    };
    
    let url = document.getElementById("urlId-vms").value 
    
    //xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    //xhr.setRequestHeader("Access-Control-Allow-Origin", "http://localhost:8000/");
    xhr.open("GET", url, true);
    xhr.send(null);   
});
