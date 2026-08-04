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
