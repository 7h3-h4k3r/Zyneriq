
// ---------- SIGNUP ----------
const signupForm = document.getElementById('signupForm');
$('.tab-btn').eq(0).removeClass('active');
$('.tab-btn').eq(1).addClass('active');

//TODO : After finished authentication ,we must add the obfuscation for the password and also we must add the email verification for the user to make sure that the email is valid and also we must add the password strength checker to make sure that the password is strong enough to protect the user account from being hacked.

if (signupForm) {
    const signupName = document.getElementById('signupName');
    const signupEmail = document.getElementById('signupEmail');
    const signupPassword = document.getElementById('signupPassword');

    signupForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const name = signupName.value.trim();
        const email = signupEmail.value.trim();
        const pwd = signupPassword.value.trim();

        if (!name || !email || !pwd) {
            showMessage('All fields required', true);
            return;
        }

        if (pwd.length < 3) {
            showMessage('Password too short', true);
            return;
        }

        const exists = users.find(u => u.email.toLowerCase() === email.toLowerCase());

        if (exists) {
            showMessage('Email already exists', true);
            return;
        }

        users.push({ fullname: name, email, password: pwd });
        saveUsers();

        showMessage('Signup successful! Redirecting...', false);
        showToast('Account created');

        setTimeout(() => {
            window.location.href = "/login";
        }, 1000);
    });
}
