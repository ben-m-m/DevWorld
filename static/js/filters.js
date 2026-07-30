//filter func initializer for listening to changes and preferences //

let filteredRepositories = [];

//search and language filter
function applyFilters() {
    let repositories = [...window.devWorld.repositories];

    const searchInput = document.getElementById("repoSearch");
    const searchTerm = searchInput.value.toLowerCase();

    if (searchTerm) {
        repositories = repositories.filter(repo => repo.name.toLowerCase().includes(searchTerm));
    }

    //language
    const languageFilter = document.getElementById("languageFilter");
    const selectedLanguage = languageFilter.value;

    if (selectedLanguage !== "all") {
        repositories = repositories.filter(repo => (repo.language || "Unknown") === selectedLanguage);
    }

    //sort

    const sort = document.getElementById("repoSort").value;

    switch(sort) {
        case "updated_desc":
            repositories.sort((a,b)=> new Date(b.updated_at)-new Date(a.updated_at));
            break;
        case "updated_asc":
            repositories.sort((a,b)=> new Date(a.updated_at)-new Date(b.updated_at));
            break;
        
        case "created_desc":
            repositories.sort((a,b)=> new Date(b.created_at)-new Date(a.created_at));
            break;

        case "created_asc":
            repositories.sort((a,b)=> new Date(a.created_at)-new Date(b.created_at));
            break;

        case "name_asc":
            repositories.sort((a,b)=> a.name.localeCompare(b.name));
            break;

        case "name_desc":
            repositories.sort((a,b)=> b.name.localeCompare(a.name));
            break;

        case "stars_desc":
            repositories.sort((a,b)=> b.stargazers_count-a.stargazers_count);
            break;

        case "stars_asc":
            repositories.sort((a,b)=> a.stargazers_count-b.stargazers_count);
            break;

        case "forks_desc":
            repositories.sort((a,b)=> b.forks_count-a.forks_count);
            break;

        case "forks_asc":
            repositories.sort((a,b)=> a.forks_count-b.forks_count);
            break;

        case "size_desc":
            repositories.sort((a,b)=> b.size-a.size);
            break;

        case "size_asc":
            repositories.sort((a,b)=> a.size-b.size);
         
           break;    
    }

    filteredRepositories = repositories;
    //update UI
    renderRepositories(repositories);
    //updateCharts
    updateCharts(repositories);
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("repoSearch").addEventListener("input", applyFilters);
    document.getElementById("repoSort").addEventListener("change", applyFilters);
    document.getElementById("languageFilter").addEventListener("change", applyFilters);
    document.getElementById("resetFilters").addEventListener("click", () => {
        document.getElementById("repoSearch").value="";
        document.getElementById("repoSort").value="update_desc";
        document.getElementById("languageFilter").value="all";

        applyFilters();
    }
);
}
);

//generate languages from repso
function populateLanguageFilter(){
    const select = document.getElementById("languageFilter");

    if (!select) return;

    const languages = [...new Set( window.devWorld.repositories.map(repo => repo.language || "Unknown"))];

    languages.forEach(language=>{
        const option = document.createElement("option");

        option.value = language;
        option.textContent = language;
        select.appendChild(option);
    });
}

document.addEventListener("DOMContentLoaded", populateLanguageFilter);

