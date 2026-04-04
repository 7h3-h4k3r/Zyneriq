// ---------- SIMPLE CLASSIC AUTH LOGIC ----------
let users = [];

// Load users from localStorage
function loadUsers() {
    const stored = localStorage.getItem('iot_simple_users');

    if (stored) {
        try {
            users = JSON.parse(stored);
        } catch (e) {
            users = [];
        }
    }

    const defaultUsers = [
        { fullname: "John Michael", email: "john@creative-tim.com", password: "1234" },
        { fullname: "Alexa Liras", email: "alexa@creative-tim.com", password: "1234" },
        { fullname: "Laurent Perrier", email: "laurent@creative-tim.com", password: "1234" },
        { fullname: "Michael Levi", email: "michael@creative-tim.com", password: "1234" },
        { fullname: "Richard Gran", email: "richard@creative-tim.com", password: "1234" },
        { fullname: "Miriam Eric", email: "miriam@creative-tim.com", password: "1234" },
        { fullname: "Demo User", email: "demo@iot.com", password: "demo" }
    ];

    let updated = false;

    defaultUsers.forEach(defUser => {
        if (!users.find(u => u.email === defUser.email)) {
            users.push(defUser);
            updated = true;
        }
    });

    if (updated) saveUsers();
}

function saveUsers() {
    localStorage.setItem('iot_simple_users', JSON.stringify(users));
}

// ---------- UI HELPERS ----------
function showMessage(msg, isError = true) {
    const msgDiv = document.getElementById('formMessage');
    if (!msgDiv) return;

    msgDiv.innerText = msg;
    msgDiv.className = 'message-area ' + (isError ? 'error-msg' : 'success-msg');

    setTimeout(() => {
        msgDiv.innerText = '';
        msgDiv.className = 'message-area';
    }, 2800);
}

function showToast(text, isError = false) {
    const toast = document.getElementById('toastMsg');
    if (!toast) return;

    toast.innerText = isError ? `⚠️ ${text}` : `✓ ${text}`;
    toast.style.backgroundColor = isError ? '#b91c1c' : '#1e2a36';
    toast.style.display = 'block';

    setTimeout(() => {
        toast.style.display = 'none';
    }, 2200);
}

// ---------- INIT ----------
loadUsers();




// ---------- SESSION CHECK ----------
const session = localStorage.getItem('iot_active_session');

if (session) {
    try {
        const sess = JSON.parse(session);
        if (sess.loggedIn) {
            showMessage(`Already logged in as ${sess.name}`, false);
        }
    } catch (e) {}
}

// ---------- OPTIONAL LOGOUT ----------
const header = document.querySelector('.dashboard-header');

if (header) {
    header.addEventListener('dblclick', () => {
        localStorage.removeItem('iot_active_session');
        showToast('Logged out');

        setTimeout(() => {
            window.location.reload();
        }, 500);
    });
}

// ---------- EXTRA UI ----------
const panel = document.querySelector('.form-panel');

if (panel) {
    const salesLine = document.createElement('div');
    salesLine.style.padding = '8px 24px';
    salesLine.style.fontSize = '0.7rem';
    salesLine.style.borderTop = '1px solid #eef2f6';
    salesLine.style.background = '#fafcff';
    salesLine.style.color = '#2c4e6e';

    salesLine.innerHTML = '📊 <strong>Sales Overview</strong> 4% more in 2026';

    panel.before(salesLine);
}