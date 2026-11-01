/* ===========================================================
   Dyrn Zefanya — site behaviour
   Kept separate from app.js so the template stays updatable.
   =========================================================== */

(function () {
  "use strict";

  // The "Visit live site" links sit inside the portfolio cards, and each card
  // is itself a Magnific Popup trigger. Without this, clicking the link would
  // open the case-study popup as well as following the href.
  document.addEventListener(
    "click",
    function (event) {
      var link = event.target.closest(".project-visit");
      if (link) {
        event.stopPropagation();
      }
    },
    true // capture, so this runs before the popup handler on the card
  );
})();

/* -----------------------------------------------------------
   Contact form → Formspree

   The template ships its own jQuery submit handler pointed at mail.php, which
   GitHub Pages cannot run. It also only implements .done(): a failed request
   does nothing visible at all, so the visitor thinks the message was sent.

   This replaces it. Registering inside a later $(function) means jQuery runs
   this after app.js has bound its handler, so .off() actually has something
   to remove.
   ----------------------------------------------------------- */
jQuery(function ($) {
  var $form = $("#contact-form");
  if (!$form.length) {
    return;
  }

  $form.off("submit");

  var $panel = $form.closest(".contact");
  var $error = $("#form-error");
  var $button = $form.find('button[type="submit"]');
  var $caption = $button.find(".btn-caption");
  var idleLabel = $caption.text();

  function showError(message) {
    $error.text(message).prop("hidden", false);
  }

  function clearError() {
    $error.prop("hidden", true).text("");
  }

  function setBusy(busy) {
    $button.prop("disabled", busy);
    $caption.text(busy ? "Sending…" : idleLabel);
  }

  function showSuccess() {
    $panel.find(".form").addClass("is-hidden");
    $panel.find(".form__reply").addClass("is-visible");
    window.setTimeout(function () {
      $panel.find(".form__reply").removeClass("is-visible");
      $panel.find(".form").delay(300).removeClass("is-hidden");
      $form.trigger("reset");
    }, 5000);
  }

  // Formspree returns its errors as an array of { field, message } objects.
  function describe(payload) {
    if (payload && Array.isArray(payload.errors) && payload.errors.length) {
      return payload.errors
        .map(function (e) {
          return e.message;
        })
        .join(" ");
    }
    return null;
  }

  $form.on("submit", function (event) {
    event.preventDefault();
    clearError();

    // Belt and braces. The honeypot is display:none so nothing should reach it,
    // but a password manager that ignores that would get the whole submission
    // rejected by Formspree with "Honeypot field _gotcha is not empty" — and the
    // visitor would have no idea why.
    var honeypot = $form.find('[name="_gotcha"]');
    if (honeypot.length && honeypot.val()) {
      honeypot.val("");
    }

    setBusy(true);

    fetch($form.attr("action"), {
      method: "POST",
      body: new FormData($form[0]),
      // Without this Formspree replies with a redirect to its own thank-you
      // page instead of JSON, which would defeat the whole point of the fetch.
      headers: { Accept: "application/json" }
    })
      .then(function (response) {
        return response.json().then(
          function (payload) {
            return { ok: response.ok, payload: payload };
          },
          function () {
            return { ok: response.ok, payload: null };
          }
        );
      })
      .then(function (result) {
        if (result.ok) {
          showSuccess();
          return;
        }
        showError(
          describe(result.payload) ||
            "That did not go through. Please email dryndarmawan@gmail.com instead."
        );
      })
      .catch(function () {
        showError(
          "No connection to the form service. Please check your network, or " +
            "email dryndarmawan@gmail.com instead."
        );
      })
      .then(function () {
        setBusy(false);
      });
  });
});

/* -----------------------------------------------------------
   Service cards → detail popups

   The cards are Magnific Popup triggers like the portfolio cards. Enter and
   Space open them from the keyboard, and "Discuss a project" inside a popup
   closes it before the page scrolls to the contact form.
   ----------------------------------------------------------- */
jQuery(function ($) {
  $(document).on("keydown", ".service-card", function (event) {
    if (event.key === "Enter" || event.key === " ") {
      event.preventDefault();
      $(this).trigger("click");
    }
  });

  // Capture phase: the click never bubbles up to document from inside the popup.
  document.addEventListener(
    "click",
    function (event) {
      if (event.target.closest(".popup-to-contact")) {
        $.magnificPopup.close();
      }
    },
    true
  );
});

/* -----------------------------------------------------------
   "How I work" stepper

   The markup lists every step as a tab plus a panel, all visible, so it reads
   fine without JavaScript. This hides all but the current panel, wires the
   tabs (click, arrow keys, prev/next), fills the progress bar, and moves one
   card across the mini Trello board to the list the step belongs to.
   ----------------------------------------------------------- */
(function () {
  "use strict";

  var root = document.querySelector("[data-process]");
  if (!root) {
    return;
  }

  var tabs = Array.prototype.slice.call(root.querySelectorAll(".process__tab"));
  var panels = Array.prototype.slice.call(root.querySelectorAll(".process__panel"));
  var lists = root.querySelectorAll(".process__list");
  var bar = root.querySelector(".process__progress span");
  var count = root.querySelector(".process__count b");
  var prev = root.querySelector('[data-step="-1"]');
  var next = root.querySelector('[data-step="1"]');
  var card = document.createElement("div");
  card.className = "process__card";
  var current = 0;

  root.classList.add("is-enhanced");

  function show(i, focus) {
    current = Math.max(0, Math.min(tabs.length - 1, i));
    tabs.forEach(function (tab, k) {
      var on = k === current;
      tab.setAttribute("aria-selected", on ? "true" : "false");
      tab.tabIndex = on ? 0 : -1;
      tab.classList.toggle("is-done", k < current);
      panels[k].hidden = !on;
    });
    var tab = tabs[current];
    card.innerHTML = "<span>" + tab.querySelector(".process__num").textContent + "</span>" +
      tab.querySelector(".process__name").textContent;
    var list = lists[+tab.getAttribute("data-board")];
    Array.prototype.forEach.call(lists, function (l) {
      l.classList.toggle("is-active", l === list);
    });
    list.querySelector(".process__slot").appendChild(card);
    card.classList.remove("is-moving");
    void card.offsetWidth; // restart the drop-in animation
    card.classList.add("is-moving");
    bar.style.width = ((current + 1) / tabs.length * 100) + "%";
    count.textContent = current + 1;
    prev.disabled = current === 0;
    next.disabled = current === tabs.length - 1;
    if (focus) {
      tab.focus();
    }
  }

  tabs.forEach(function (tab, k) {
    tab.addEventListener("click", function () { show(k); });
    tab.addEventListener("keydown", function (event) {
      var to = { ArrowRight: k + 1, ArrowDown: k + 1, ArrowLeft: k - 1, ArrowUp: k - 1,
                 Home: 0, End: tabs.length - 1 }[event.key];
      if (to !== undefined) {
        event.preventDefault();
        show(to, true);
      }
    });
  });

  [prev, next].forEach(function (btn) {
    btn.addEventListener("click", function () {
      show(current + (+btn.getAttribute("data-step")));
    });
  });

  show(0);
})();
