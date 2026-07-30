document.addEventListener("DOMContentLoaded", () => {
    initializeLanguageChart();
    initializeStarsChart();
    initializeForkChart();
    initializeSizeChart();
});

//chhart showing the programming languages used in number and percentage use.//
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

//chart showing stars by numbers for each repo//
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

//chart showing Forks by numbers//
function initializeForkChart() {
    const canvas = document.getElementById("forkChart")

    if (!canvas) return;

    const labels = JSON.parse(canvas.dataset.labels);
    const values = JSON.parse(canvas.dataset.values);

    new Chart(canvas, {
        type: "bar",
        data: {
            labels,
            datasets: [{
                label: "Forks",
                data: values
            }]
        },

        options: {
            responsive: true,
            mainatainAspectRatio: true
        }
    });
}

// chart for showing repository sizes
function initializeSizeChart() {
    const canvas = document.getElementById("sizeChart");
    if (!canvas) return;

    const labels = JSON.parse(canvas.dataset.labels);
    const values = JSON.parse(canvas.dataset.values);

    new Chart(canvas, {
        type: "bar",
        data: {
            labels,
            datasets: [{
                label: "Repo_Size",
                data: values
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true
        }
    });
}

//search event listener//
const search = document.getElementById("repoSearch");

search.addEventListener("input", () => {
    const term = search.value.toLowerCase();
    document.querySelectorAll(".repository-card").forEach(card => {
        const name = card.dataset.name.toLowerCase();

        card.style.display = 
        name.includes(term) ? "" : "none";
    });
});
