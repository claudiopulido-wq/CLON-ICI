document.addEventListener('DOMContentLoaded', () => {
    // Evita registrar los listeners dos veces si el script se incluye más de una vez
    if (window.__iciMainLoaded) return;
    window.__iciMainLoaded = true;

    // Debe coincidir con el breakpoint de navegación móvil en css/style.css
    const NAV_BREAKPOINT = 1150;
    const isMobileNav = () => window.innerWidth <= NAV_BREAKPOINT;

    // Scroll effect for navbar
    const header = document.querySelector('header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                header.style.boxShadow = '0 4px 15px rgba(0,0,0,0.1)';
            } else {
                header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.08)';
            }
        }, { passive: true });
    }

    // Mobile Menu Toggle
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const navLinks = document.querySelector('.nav-links');
    if (!mobileBtn || !navLinks) return;
    const mobileIcon = mobileBtn.querySelector('i');

    // El botón es un <div>; lo hacemos accesible por teclado y lector de pantalla
    mobileBtn.setAttribute('role', 'button');
    mobileBtn.setAttribute('tabindex', '0');
    mobileBtn.setAttribute('aria-label', 'Abrir menú');
    mobileBtn.setAttribute('aria-expanded', 'false');

    function setMenuOpen(open) {
        navLinks.classList.toggle('active', open);
        mobileIcon.classList.toggle('fa-bars', !open);
        mobileIcon.classList.toggle('fa-xmark', open);
        mobileBtn.setAttribute('aria-expanded', String(open));
        mobileBtn.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    }

    mobileBtn.addEventListener('click', () => {
        setMenuOpen(!navLinks.classList.contains('active'));
    });

    mobileBtn.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            setMenuOpen(!navLinks.classList.contains('active'));
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && navLinks.classList.contains('active')) {
            setMenuOpen(false);
            mobileBtn.focus();
        }
    });

    // Al volver a escritorio, cerrar el menú móvil y los submenús abiertos
    window.addEventListener('resize', () => {
        if (!isMobileNav()) {
            setMenuOpen(false);
            document.querySelectorAll('.dropdown.active').forEach(d => d.classList.remove('active'));
        }
    });

    // Mobile Dropdown Toggle: solo el enlace principal abre/cierra el submenú
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(dropdown => {
        const trigger = dropdown.querySelector(':scope > a');
        if (!trigger) return;
        trigger.addEventListener('click', (e) => {
            if (trigger.getAttribute('href') === '#') {
                e.preventDefault();
            }
            if (isMobileNav()) {
                dropdown.classList.toggle('active');
            }
        });
    });
});
