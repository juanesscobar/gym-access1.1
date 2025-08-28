document.addEventListener("DOMContentLoaded", () => {
    console.log("Gym Access cargado ✅");

    // Marcar enlace activo
    const currentPath = window.location.pathname;
    document.querySelectorAll(".nav-item").forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
        }
    });
});
