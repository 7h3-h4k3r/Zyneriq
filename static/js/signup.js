
// ---------- SIGNUP ----------
const signupForm = document.getElementById('signupForm');

document.getElementsByClassName('tab-btn')[0].classList.remove('active');
document.getElementsByClassName('tab-btn')[1].classList.add('active');
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
