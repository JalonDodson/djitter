let btn = document.getElementById("login")
let usr = document.getElementById("usr")
let pw = document.getElementById("pw")

usr.oninput = () => this.value ? btn.disabled = true : btn.disabled = false; 