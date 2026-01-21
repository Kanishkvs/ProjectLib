// const app = require('express') ();
// const {sha} = require('crypto');

// import crypto from 'crypto';

const serverApi = "http://localhost:4000";

let my_form = document.getElementById("login_form");

const things = document.getElementsByTagName("form");
const register = document.getElementById("register");
// console.log(JSON.stringify(my_form));
// console.log(things);

// Source: https://mojoauth.com/hashing/sha-256-in-javascript-in-browser#implementing
async function hashString(message) {
    // Encode the string as a Uint8Array
    const msgBuffer = new TextEncoder().encode(message);

    // Hash the message using SHA-256
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);

    // Convert the ArrayBuffer to a hex string
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => ('00' + b.toString(16)).slice(-2)).join('');
}

register.addEventListener("click",  (event) => {
    event.preventDefault();
    window.location.replace("/register");
})

my_form.addEventListener("submit", async (e) => {

    e.preventDefault();

    let loginAttempt = {};
    loginAttempt.username = document.getElementById("username").value;
    loginAttempt.password = document.getElementById("password").value;

    await hashString(loginAttempt.password).then(hash => loginAttempt.password = hash);

    console.log(JSON.stringify(loginAttempt));

    // fetch((serverApi+"/login"),
    //     {
    //     method: 'GET',
    //         body: JSON.stringify (loginAttempt)
    //     })
    // .then(response => response.json())
    // .then(data => {})


})
