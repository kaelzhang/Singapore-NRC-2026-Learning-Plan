(function () {
  const drawer = document.querySelector("[data-drawer]");
  const backdrop = document.querySelector("[data-backdrop]");
  const openButton = document.querySelector("[data-open-menu]");
  const closeButton = document.querySelector("[data-close-menu]");
  let hideTimer = 0;

  function setMenuEntryVisible(visible) {
    if (!openButton) return;
    document.body.classList.toggle("menu-entry-visible", visible);
    openButton.tabIndex = visible ? 0 : -1;
  }

  function menuVisible() {
    return document.body.classList.contains("menu-entry-visible")
      || document.body.classList.contains("drawer-open");
  }

  function hideMenu() {
    window.clearTimeout(hideTimer);
    hideTimer = 0;
    setDrawer(false, false);
    setMenuEntryVisible(false);
  }

  function scheduleHide() {
    window.clearTimeout(hideTimer);
    if (!menuVisible()) return;
    hideTimer = window.setTimeout(hideMenu, 5000);
  }

  function showMenuEntry() {
    setMenuEntryVisible(true);
    scheduleHide();
  }

  function setDrawer(open, keepEntry) {
    if (!drawer || !backdrop || !openButton) return;
    document.body.classList.toggle("drawer-open", open);
    if (open) setMenuEntryVisible(true);
    if (!open && keepEntry === false) setMenuEntryVisible(false);
    drawer.setAttribute("aria-hidden", open ? "false" : "true");
    openButton.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) {
      const active = drawer.querySelector(".nav-link.active");
      if (active) active.scrollIntoView({ block: "center" });
    }
    scheduleHide();
  }

  if (openButton) openButton.addEventListener("click", () => setDrawer(true));
  if (closeButton) closeButton.addEventListener("click", () => setDrawer(false));
  if (backdrop) backdrop.addEventListener("click", () => setDrawer(false));

  document.addEventListener("click", (event) => {
    if (!drawer || !openButton) return;
    const target = event.target;
    const insideDrawer = drawer.contains(target);
    const onMenuButton = openButton.contains(target);
    if (!insideDrawer && !onMenuButton) showMenuEntry();
  });

  ["mousemove", "mousedown", "touchstart"].forEach((eventName) => {
    document.addEventListener(eventName, () => {
      if (menuVisible()) scheduleHide();
    }, { passive: true });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      hideMenu();
    } else if (!menuVisible()) {
      showMenuEntry();
    } else {
      scheduleHide();
    }
  });

  setMenuEntryVisible(false);
})();
