(function () {
  const drawer = document.querySelector("[data-drawer]");
  const backdrop = document.querySelector("[data-backdrop]");
  const openButton = document.querySelector("[data-open-menu]");
  const closeButton = document.querySelector("[data-close-menu]");
  const printButton = document.querySelector("[data-print]");

  function setDrawer(open) {
    if (!drawer || !backdrop || !openButton) return;
    document.body.classList.toggle("drawer-open", open);
    drawer.setAttribute("aria-hidden", open ? "false" : "true");
    openButton.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) {
      const active = drawer.querySelector(".nav-link.active");
      if (active) active.scrollIntoView({ block: "center" });
    }
  }

  if (openButton) openButton.addEventListener("click", () => setDrawer(true));
  if (closeButton) closeButton.addEventListener("click", () => setDrawer(false));
  if (backdrop) backdrop.addEventListener("click", () => setDrawer(false));
  if (printButton) printButton.addEventListener("click", () => window.print());

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") setDrawer(false);
  });
})();
