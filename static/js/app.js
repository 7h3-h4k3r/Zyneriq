// ------------------------------
// PAGE TITLES (optional use)
// ------------------------------
const PAGE_TITLES = {
    dashboard: 'dashboard',
    tables: 'Tables',
    billing: 'Billing',
    vr: 'Virtual Reality',
    rtl: 'RTL',
    profile: 'Profile',
    signin: 'Sign In',
    signup: 'Sign Up'
};

// ------------------------------
// CHART INITIALIZATION
// ------------------------------
let chartsInit = false;

function initCharts() {
    if (chartsInit) return;

    const barCanvas = document.getElementById('barChart');
    const lineCanvas = document.getElementById('lineChart');

    // Prevent errors on pages without charts
    if (!barCanvas || !lineCanvas) return;

    chartsInit = true;

    // ----- BAR CHART -----
    const barCtx = barCanvas.getContext('2d');

    new Chart(barCtx, {
        type: 'bar',
        data: {
            labels: ['M','T','W','T','F','S','S','M','T','W','T','F'],
            datasets: [{
                data: [200,380,220,380,300,280,390,300,250,400,180,360],
                backgroundColor: 'rgba(255,255,255,0.7)',
                borderRadius: 6,
                borderSkipped: false
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                x: {
                    grid: { display: false },
                    ticks: {
                        color: 'rgba(255,255,255,0.5)',
                        font: { size: 10 }
                    },
                    border: { display: false }
                },
                y: {
                    grid: { color: 'rgba(255,255,255,0.08)' },
                    ticks: {
                        color: 'rgba(255,255,255,0.5)',
                        font: { size: 10 }
                    },
                    border: { display: false },
                    min: 0,
                    max: 500
                }
            }
        }
    });

    // ----- LINE CHART -----
    const lineCtx = lineCanvas.getContext('2d');

    const g1 = lineCtx.createLinearGradient(0, 0, 0, 200);
    g1.addColorStop(0, 'rgba(17,205,239,0.3)');
    g1.addColorStop(1, 'rgba(17,205,239,0)');

    const g2 = lineCtx.createLinearGradient(0, 0, 0, 200);
    g2.addColorStop(0, 'rgba(45,46,78,0.2)');
    g2.addColorStop(1, 'rgba(45,46,78,0)');

    new Chart(lineCtx, {
        type: 'line',
        data: {
            labels: ['Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
            datasets: [
                {
                    data: [50,100,200,450,300,360,200,300,500],
                    borderColor: '#11cdef',
                    backgroundColor: g1,
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0,
                    borderWidth: 2.5
                },
                {
                    data: [30,80,150,300,250,320,160,280,430],
                    borderColor: '#1a2332',
                    backgroundColor: g2,
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0,
                    borderWidth: 2.5
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false }
            },
            scales: {
                x: {
                    grid: { display: false },
                    ticks: {
                        color: '#8392ab',
                        font: { size: 10 }
                    },
                    border: { display: false }
                },
                y: {
                    grid: { color: '#e9ecef' },
                    ticks: {
                        color: '#8392ab',
                        font: { size: 10 }
                    },
                    border: { display: false },
                    min: 0,
                    max: 500
                }
            }
        }
    });
}

// ------------------------------
// PROFILE TABS (SAFE INIT)
// ------------------------------
function initProfileTabs() {
    const tabs = document.querySelectorAll('.profile-tab');

    if (tabs.length === 0) return;

    tabs.forEach(tab => {
        tab.addEventListener('click', function () {
            tabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
        });
    });
}

// ------------------------------
// GLOBAL INIT (SAFE FOR ALL PAGES)
// ------------------------------
window.addEventListener('DOMContentLoaded', function () {
    initCharts();
    initProfileTabs();
});