const loginForm = document.getElementById('loginForm');
$('.tab-btn').eq(0).addClass('active');
$('.tab-btn').eq(1).removeClass('active');
alreadyLogin().then(data => {
    if (data && data.username) {
        window.location.href = "/dashboard"; // change if needed

    }
})
async function getUser(user) {
    try {
        const response = await fetch('/auth/login' , {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        });
        if (!response.ok) {
            return null;
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}
if (loginForm) {
    const loginUser = document.getElementById('loginUser');
    const loginPassword = document.getElementById('loginPassword');


    loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();

        const username = loginUser.value.trim();
        const pwd = loginPassword.value.trim();

        if (!username || !pwd) {
            showMessage('Please fill all fields', true);
            return;
        }

        const user = {
            username: username,
            password: pwd
        }
        const in_user = await getUser(user);
    
        if (in_user) {
            showMessage(`Welcome ${in_user.username}`, false);
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

