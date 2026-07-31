//repo data intelligence for selected repo
function updateRepositoryIntel(repo) {

    const panel = document.getElementById("repositoryIntelligence");

    if (!panel) return;

    const maintenance = calculateMaintenance(repo);
    const popularity = calculatePopularity(repo);
    const activity = calculateActivity(repo);
    const health = calculateOverallHeat(maintenance, popularity, activity);

    panel.innerHTML = `
        <h3>${repo.name}</h3>
        <p>
            ${repo.description || "No description"}
        </p>
        <hr>
        <div class="row">
            <div class="col-md-3">
                <strong>Language</strong>
                <p>${repo.language || "Unknown"}</p>
            </div>
            <div class="col-md-3">
                <strong>Stars</strong>
                <p>${repo.stargazers_count}</p>
            </div>
            <div class="col-md-3">
                <strong>Forks</strong>
                <p>${repo.forks_count}</p>
            </div>
            <div class="col-md-3">
                <strong>Size</strong>
                <p>${repo.size} KB</p>
            </div>
        </div>
        <hr>
        <div class="mb-3">
            <strong>Maintenance Score</strong>
            <div class="progress">
                <div
                    class="progress-bar bg-success"
                    style="width:${maintenance}%">
                    ${maintenance}%
                </div>
            </div>
        </div>
        <div class="mb-3">
            <strong>Popularity Score</strong>
            <div class="progress">
                <div
                    class="progress-bar bg-primary"
                    style="width:${popularity}%">

                    ${popularity}%
                </div>
            </div>
        </div>
        <div class="mb-3">
            <strong>Activity Score</strong>
            <div class="progress">
                <div
                    class="progress-bar bg-warning"
                    style="width:${activity}%">

                    ${activity}%
                </div>
            </div>
        </div>
        <hr>
        <div class="row mb-4">

    <div class="col-md-6">

        <strong>Created</strong>

        <p>${repo.created_at.substring(0, 10)}</p>

    </div>

    <div class="col-md-6">

        <strong>Last Updated</strong>

        <p>${repo.updated_at.substring(0, 10)}</p>

    </div>

</div>
        <h5>

            Overall Health:
            ${health}

        </h5>

    `;
}

//calculating metrics
function calculateMaintenance(repo) {
    return repo.archived ? 20 : 90;
}

function calculatePopularity(repo) {
    return Math.min(100, repo.stargazers_count * 5);
}

function calculateActivity(repo) {
    const updated = new Date(repo.updated_at);
    const days = (Date.now() - updated) / 86400000;
    return Math.max(10, Math.round(100 - days));
}

function calculateOverallHeat(maintenance, popularity, activity) {
    const score = Math.round((maintenance + popularity + activity) / 3);

    let label;

    if (score >= 80)
        label = "Excellent"
    else if (score >= 60 && score < 80)
        label = "Good"
    else if (score >= 40 && score < 60)
        label = "Average"
    else
        label = "Needs More Attention";
    return `${score}% (${label})`;
}

