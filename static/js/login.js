const loginForm = document.getElementById('loginForm');
$('.tab-btn').eq(0).addClass('active');
$('.tab-btn').eq(1).removeClass('active');

async function getUser(user) {
    try {
        const response = await fetch('/api/v1/auth' , {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(user)
        });
        if (!response.ok) {
            const data = await response.json();
            
            return data;
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
            password: pwd,
            redirect: false
        }
        const in_user = await getUser(user);
        
        if (in_user.authenticated!=false) {
            showMessage(`Welcome ${in_user.username} ${in_user.message}`, false);
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

