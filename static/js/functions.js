document.addEventListener("DOMContentLoaded", () => {
    //////////----- VALIDACAO DO E-MAIL ----->>
    const emailLink = document.getElementById("emailLink");
    if (emailLink) {
        emailLink.addEventListener("click", function (e) {
            e.preventDefault();
            const email = "jonnywwwpedro@gmail.com";
            window.location.href = `mailto:${email}`;
            setTimeout(() => {
                window.open(
                    `https://mail.google.com/mail/?view=cm&fs=1&to=${email}`,
                    "_blank"
                );
            }, 500);
        });
    }


    //////////----- TROCA DE TEMA ESCURO E CLARO ----->>
    const toggle = document.querySelector(".dark-mode-toggle");
    const savedTheme = localStorage.getItem("theme") || "dark";
    body.classList.toggle("light-mode", savedTheme === "light");
    if (toggle) {
        toggle.addEventListener("click", () => {
            const isLight = body.classList.toggle("light-mode");
            localStorage.setItem("theme", isLight ? "light" : "dark");
        });
    }


    //////////----- OPCAO DE RECOLHER E MOSTRAR CURSOS ----->>
    const btnMostrar = document.getElementById('mostrarTodos');
    const btnRecolher = document.getElementById('recolher');
    const cursosExtras = document.querySelectorAll('.extra-curso');
    btnMostrar.addEventListener('click', () => {
        cursosExtras.forEach(curso => curso.style.display = '');
        btnMostrar.style.display = 'none';
        btnRecolher.style.display = 'block';
    });

    btnRecolher.addEventListener('click', () => {
        cursosExtras.forEach(curso => curso.style.display = 'none');
        btnMostrar.style.display = 'block';
        btnRecolher.style.display = 'none';
    });
    cursosExtras.forEach(curso => curso.style.display = 'none');


});

