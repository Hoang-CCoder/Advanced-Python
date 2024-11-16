function changeTypePassword() {
    const passwordInput = document.getElementById('password');
    const type = passwordInput.type === 'text' ? 'password' : 'text';
    passwordInput.type = type;
}

function changeTypePassword2() {
    const confirmPasswordInput = document.getElementById('confirm-password');
    const type = confirmPasswordInput.type === 'text' ? 'password' : 'text';
    confirmPasswordInput.type = type;
}

