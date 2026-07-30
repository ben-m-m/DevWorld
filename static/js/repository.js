
let displayedRepositories = [];
// function to render repo stats upon filter or select

function renderRepositories(repositories) {
    displayedRepositories = repositories;

    const container = document.getElementById("repositoryContainer");

    if (!container) return;

    container.innerHTML = "";

    repositories.forEach(repo => {
        container.innerHTML += `
        <div class="col-md-6 mb-4 repository-card"
             data-name="${repo.name}"
             data-language="${repo.language || "Unknown"}"
             data-stars="${repo.stargazers_count}"
             data-forks="${repo.forks_count}"
             data-size="${repo.size}"
             data-created="${repo.created_at}"
             data-updated="${repo.updated_at}">

             <div class="card h-100 shadow-sm">
                <div class="card-body">
                    <h4>${repo.name}<h4>
                    <p class="text-muted">
                    ${repo.description || "No description available!"}
                    </p>
                    <p>
                    <strong>Language:</strong
                    <span class="badge bg-primary">
                        ${repo.language || "Unknown"}
                    </span>
                    </p>
                    <div class="d-flex flex-wrap gap-3 my-2">
                        <span>⭐ ${repo.stargazers_count}</span>

                        <span>🍴 ${repo.forks_count}</span>

                        <span>👀 ${repo.watchers_count}</span>

                        <span>🐞 ${repo.open_issues_count}</span>
                    </div>
                    <p>
                        Size: ${repo.size} KB
                    </p>
                    <small class="text-muted">
                        Updated: ${repo.updated_at.substring(0, 10)}
                    </small>
                    <br></br>
                    <button class="btn btn-primary btn-sm mt-3 viewRepoStats" data-repo="${repo.name}"> View Analytics </button>
                    <a href="${repo.html_url}" target="_blank" class="btn btn-outline-dark"> View on GitHub </a>
                </div>
             </div>
        </div>
        `;

    });
    attachRepositoryEvents();
}

//attaches the events to the repo
function attachRepositoryEvents() {
    document.querySelectorAll(".viewRepoStats").forEach(button => {
        button.addEventListener("click", () => {
            document.querySelectorAll(".repository-card").forEach(card => card.classList.remove("selected"));
            const card = button.closest(".repository-card");
            card.classList.add("selected");

            const repoName = button.dataset.repo;
            const repo = displayedRepositories.find(r => r.name === repoName);

            if (!repo) return;

            updateCharts([repo]);
            updateRepositorySummary(repo);

            window.scrollTo({
                top: 350,
                behavior: "smooth"
            });
        });
    });
}

function updateRepositorySummary(repo) {

    const summary = document.getElementById("repositorySummary");

    if (!summary) return;
    summary.innerHTML = `
        <h4>${repo.name}</h4>

        <p>${repo.description || "No description available."}</p>

        <hr>

        <div class="row">

            <div class="col">
                ⭐ Stars
                <h3>${repo.stargazers_count}</h3>
            </div>

            <div class="col">
                🍴 Forks
                <h3>${repo.forks_count}</h3>
            </div>

            <div class="col">
                📦 Size
                <h3>${repo.size} KB</h3>
            </div>

            <div class="col">
                💻 Language
                <h3>${repo.language || "Unknown"}</h3>
            </div>

        </div>

    `;
}

document.addEventListener("DOMContentLoaded", () => {
    renderRepositories(window.devWorld.repositories);
});


const button = document.getElementById("showAllRepos");
if (button) {
    button.addEventListener("click", () => {
        document.querySelectorAll(".repository-card").forEach(card => card.classList.remove("selected"));
        updateCharts(window.devWorld.repositories);
    });
}
