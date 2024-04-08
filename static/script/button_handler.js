const logoutButton = document.getElementById('log_out_button');
const saveButton = document.getElementById('save_button');
const username = document.getElementById('username');
const password = document.getElementById('password');
const sendData = (buttonName) => {
    let formData = new FormData();
    formData.append('button', buttonName);
    formData.append('new_username', username.value);
    formData.append('password', password.value);
    fetch('profile', {
        method: 'POST',
        body: formData
    });
}
logoutButton.addEventListener('click', () => {
    sendData('logout');
});
saveButton.addEventListener('click', () => {
    sendData('save');
});