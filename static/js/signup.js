
// ---------- SIGNUP ----------
const signupForm = document.getElementById('signupForm');
$('.tab-btn').eq(0).removeClass('active');
$('.tab-btn').eq(1).addClass('active');
async function setUser(user) {
    try {
        const response = await fetch('/auth/signup' , {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        });
        const data = await response.json();
        if (!response.ok) {
            showMessage('Signup failed: ' + data['error'], true);
            return;
        }
        
        return data.message;
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}
//TODO : After finished authentication ,we must add the obfuscation for the password and also we must add the email verification for the user to make sure that the email is valid and also we must add the password strength checker to make sure that the password is strong enough to protect the user account from being hacked.

const emailInput = document.getElementById('signupEmail');

emailInput.addEventListener('input', () => {
    const value = emailInput.value;
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!regex.test(value)) {
        emailInput.style.border = "2px solid red";
    } else {
        emailInput.style.border = "2px solid green";
    }
});
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

        user = {
            username: name,
            email: email,
            password: pwd
        }

        const res = setUser(user);
       
        if (res){
            showMessage('Signup successful! Redirecting...', false);
            showToast('Account created');

            setTimeout(() => {
                window.location.href = "/login";
            }, 1000);
        }

        
    });
}
