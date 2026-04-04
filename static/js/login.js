// ---------- LOGIN ----------
const loginForm = document.getElementById('loginForm');
document.getElementsByClassName('tab-btn')[0].classList.add('active');
document.getElementsByClassName('tab-btn')[1].classList.remove('active');

if (loginForm) {
    const loginEmail = document.getElementById('loginEmail');
    const loginPassword = document.getElementById('loginPassword');

    // Prefill demo
    if (loginEmail && loginPassword) {
        loginEmail.value = 'demo@iot.com';
        loginPassword.value = 'demo';
    }

    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const email = loginEmail.value.trim();
        const pwd = loginPassword.value.trim();

        if (!email || !pwd) {
            showMessage('Please fill all fields', true);
            return;
        }

        const user = users.find(
            u => u.email.toLowerCase() === email.toLowerCase() && u.password === pwd
        );

        if (user) {
            localStorage.setItem('iot_active_session', JSON.stringify({
                email: user.email,
                name: user.fullname,
                loggedIn: true
            }));

            showMessage(`Welcome ${user.fullname}`, false);
            showToast('Login successful');

            setTimeout(() => {
                window.location.href = "/dashboard"; // change if needed
            }, 800);

        } else {
            showMessage('Invalid credentials', true);
            showToast('Login failed', true);
        }
    });
}