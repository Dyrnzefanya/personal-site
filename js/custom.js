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
