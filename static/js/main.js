"use strict"

const getbyid = (id) => {
    return document.getElementById(id).value
};

const fname = getbyid('fname'),lname = getbyid('lname'),username = getbyid('username'),email = getbyid('email');

const button = document.getElementById('change')
console.log(button)

// button.addEventListener('click', (e) => {
//     e.preventDefault();
//     const form = document.getElementById('my-change-form')
//     let nfname = getbyid('fname'),nlname = getbyid('lname'),nusername = getbyid('username'),nemail = getbyid('email');

//     if (nfname!=fname || nlname!=lname || nusername!=username || nemail!=email) {
//         form.submit()
//     }else{
//         alert("You have made no change")
//     }

// }, false);
let alert = document.querySelector('div.alert')

setTimeout(() => {
    alert.style.display = "None";
}, 2000)