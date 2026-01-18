const app = require('express') ();

const {sha} = require('crypto').createHash ('sha256');

const serverApi = "http://localhost:4000";

const form = document.getElementById("login-form");
form.addEventListener("submit", (e) => {
    let loginAttempt = {};
    loginAttempt.username = document.getElementById("username").value;
    loginAttempt.password = document.getElementById("password").value;
    fetch((serverApi+"/login"), {method: 'GET'})
    .then(response => response.json())
    .then(data => {})

})