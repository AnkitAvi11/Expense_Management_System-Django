"use strict"

const getTarget = (e) => {
    if (!e) {
        e = window.event;
    }
    return e.srcElement || e.target;
}

window.addEventListener('DOMContentLoaded', () => {

    let wallet_container = document.getElementById('all-wallets')
    
    wallet_container.addEventListener('click', (e) => {
        let tar = getTarget(e);
        let csrf_token = document.querySelector("#exampleModal > div > div > div.modal-body > form > input[type=hidden]").value
        
        if (tar.id == 'wallet-setting') {
            let wallet_id = parseInt(tar.parentNode.id);
            let form = new FormData()
            form.append('wallet_id', wallet_id)
            fetch('http://127.0.0.1:8000/api/wallet/', {
                method : 'POST', 
                body : form,
                headers: {
                    "X-CSRFToken": csrf_token
                },
            }).then(res => res.json())
            .then(data => {
                data = JSON.parse(data)[0].fields
                console.log(data);
                document.getElementById('exampleModalLabel').textContent=data.name
                document.getElementById('wname').value = data.name
                document.getElementById('description').value = data.description
            }).catch(err => {
                console.log(err)
            })
        }
    });

}, false);
