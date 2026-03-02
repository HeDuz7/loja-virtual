(function () {
  // ===== Quantidade =====
  const qtyEl = document.getElementById("qtyValue");
  const qtyBox = document.querySelector(".dp-qtyBox");

  function setQty(newQty) {
    const safeQty = Math.max(1, newQty); // mínimo 1
    qtyEl.textContent = String(safeQty);
  }

  if (qtyEl && qtyBox) {
    qtyBox.addEventListener("click", (e) => {
      const btn = e.target.closest("button[data-action]");
      if (!btn) return;

      const action = btn.getAttribute("data-action");
      const current = parseInt(qtyEl.textContent || "1", 10) || 1;

      if (action === "decrease") setQty(current - 1);
      if (action === "increase") setQty(current + 1);
    });
  }

  // ===== Tamanhos (somente 1 selecionado) =====
  const sizeGroup = document.getElementById("sizeGroup");
  const selectedSize = document.getElementById("selectedSize");

  if (sizeGroup) {
    sizeGroup.addEventListener("click", (e) => {
      const btn = e.target.closest(".dp-size");
      if (!btn) return;

      // remove active de todos
      sizeGroup.querySelectorAll(".dp-size").forEach(b => b.classList.remove("is-active"));

      // ativa o clicado
      btn.classList.add("is-active");

      // salva no hidden
      if (selectedSize) selectedSize.value = btn.dataset.size || btn.textContent.trim();
    });
  }

  // ===== Avaliação por estrelas =====
  const starsWrap = document.getElementById("ratingStars");
  const selectedRating = document.getElementById("selectedRating");

  function setRating(value) {
    const v = Math.max(1, Math.min(5, value));
    if (selectedRating) selectedRating.value = String(v);

    // pinta até a estrela escolhida
    starsWrap.querySelectorAll(".dp-starBtn").forEach((btn) => {
      const starVal = parseInt(btn.dataset.value || "0", 10);
      btn.classList.toggle("is-on", starVal <= v);
    });
  }

  if (starsWrap) {
    // define estado inicial (se tiver hidden, usa ele; senão usa 4)
    const initial = parseInt((selectedRating && selectedRating.value) || "4", 10) || 4;
    setRating(initial);

    starsWrap.addEventListener("click", (e) => {
      const btn = e.target.closest(".dp-starBtn");
      if (!btn) return;
      setRating(parseInt(btn.dataset.value || "1", 10));
    });
  }
})();