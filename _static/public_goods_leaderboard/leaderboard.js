document.addEventListener('DOMContentLoaded', function () {
    function updateLeaderboard() {
        fetch(window.location.href)
            .then(response => response.text())
            .then(html => {
                // Parse the returned HTML string
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, "text/html");

                // Extract the tbody from the fetched page
                const newTbody = doc.querySelector("#leaderboard-body");

                // Replace current tbody with the new one
                const oldTbody = document.querySelector("#leaderboard-body");
                if (newTbody && oldTbody) {
                    oldTbody.innerHTML = newTbody.innerHTML;
                }
            })
            .catch(err => console.error("Error refreshing leaderboard:", err));
    }

    // Auto-refresh every 15 seconds (adjust timing as needed)
    setInterval(updateLeaderboard, 15000);
});
