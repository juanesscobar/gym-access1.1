document.addEventListener("DOMContentLoaded", async () => {
    try {
        // Cargar estadísticas
        const statsRes = await fetch("/api/stats");
        const stats = await statsRes.json();
        document.getElementById("activeMembers").textContent = stats.active_members;
        document.getElementById("trainingsToday").textContent = stats.trainings_today;
        document.getElementById("monthlySales").textContent = `$${stats.monthly_sales}`;

        // Cargar miembros recientes
        const membersRes = await fetch("/api/members?limit=5");
        const members = await membersRes.json();
        const membersList = members.map(m => `<p>${m.name} (${m.joined_date})</p>`).join("");
        document.getElementById("recentMembers").innerHTML = membersList || "No hay registros";
    } catch (error) {
        console.error("Error cargando datos:", error);
        document.getElementById("recentMembers").textContent = "Error al cargar datos.";
    }
});
