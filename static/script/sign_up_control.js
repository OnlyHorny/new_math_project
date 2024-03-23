const isValidPassword = (password) => {
    const regex = /^[a-zA-Z0-9!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]*$/
    return regex.test(password)
}

const isValidLogin = (login) => {
    const regex = /^[a-zA-z0-9_]*$/
    return regex.test(login)
}

const check = () => {
    const login = document.getElementById('username').value
    const password = document.getElementById('password').value
    if (login.length > 2 && password.length > 4 && isValidLogin(login) && isValidPassword(password)) {
        document.getElementById('reg').removeAttribute('disabled')
    }
    else {
        document.getElementById('reg').setAttribute('disabled', '')
    }
}
const login = document.getElementById('username')
const password = document.getElementById('password')
login.addEventListener('blur', check)
password.addEventListener('blur', check)