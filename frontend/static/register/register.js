const myform = document.getElementById("register-form");
const login = document.getElementById("login");

async function hashString(message) {
    // Encode the string as a Uint8Array
    const msgBuffer = new TextEncoder().encode(message);

    // Hash the message using SHA-256
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);

    // Convert the ArrayBuffer to a hex string
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => ('00' + b.toString(16)).slice(-2)).join('');
}

myform.addEventListener("submit", (e) => {
    e.preventDefault();
    console.log("Submitted");
})

login.addEventListener("click", (e) => {
    e.preventDefault();
    console.log("login attempted");
    window.location.replace("/login");
})