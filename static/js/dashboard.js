document.addEventListener("DOMContentLoaded", () => {
    initializeLanguageChart();
    initializeStarsChart();
});

function initializeLanguageChart() {
    const canvas = document.getElementById("languageChart");
    if (!canvas) {
        return;
    }

    const languageData = JSON.parse(
        canvas.dataset.language
    );

    new Chart(canvas, {
        type: "doughnut",
        data: {
            labels: Object.keys(languageData),
            datasets: [
                {
                    data: Object.values(languageData)
                }
            ]
        },

        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

function initializeStarsChart() {
    const canvas = document.getElementById("starsChart");

    if (!canvas) return;

    const labels = JSON.parse(canvas.dataset.labels);
    const values = JSON.parse(canvas.dataset.values);

    new Chart(canvas, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                label: "GitHub Stars",
                data: values
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}

console.log("dashboard.js loaded");