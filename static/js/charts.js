let languageChart;
let starsChart;
let forksChart;
//initializing the charts for every repo selected//
function initializeCharts(data) {
    const repositories = data.repositories || window.devWorld.repositories;

    drawLanguageChart(repositories);
    drawStarsChart(repositories);
    drawForkChart(repositories);
}
//function meant to display the stars num in bar chart
function drawStarsChart(repositories) {
    const canvas = document.getElementById("starsChart");

    if (!canvas) return;

    const labels = repositories.map(repo => repo.name);
    const values = repositories.map(repo => repo.stargazers_count);

    if (starsChart) {
        starsChart.destroy();
    }

    starsChart = new Chart(canvas, {
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
            maintainAspectRatio: true
        }
    });
}

// draw fork chart
function drawForkChart(repositories) {
    const canvas = document.getElementById("forkChart");

    if (!canvas) return;
    const labels = repositories.map(repo => repo.name);
    const values = repositories.map(repo => repo.forks_count);

    if (forksChart) {
        forksChart.destroy();
    }

    forksChart = new Chart(canvas, {
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
            maintainAspectRatio: true
        }
    });
}

//language chart

function drawLanguageChart(repositories) {
    const canvas = document.getElementById("languageChart");

    if (!canvas) return;

    const languages = {};

    repositories.forEach(repo => {
        const lang = repo.language || "Unknown";
        languages[lang] = (languages[lang] || 0) + 1;
    });

    if (languageChart) {
        languageChart.destroy();
    }

    languageChart = new Chart(canvas, {
        type: "doughnut",
        data: {
            labels: Object.keys(languages),
            datasets: [{
                data: Object.values(languages)
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true
        }
    });
}
//refreshes the charts for the selected repo chart display
function updateCharts(repositories) {

    drawLanguageChart(repositories);
    drawStarsChart(repositories);
    drawForkChart(repositories);

}
//load charts upon page first load or refresh
document.addEventListener("DOMContentLoaded", () => {

    initializeCharts({
        repositories: window.devWorld.repositories
    });

});
