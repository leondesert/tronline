!(function ($) {
  "use strict";

  var SweetAlert = function () {};

  //examples
  (SweetAlert.prototype.init = function () {


    $("#sa-confirm").click(function () {
      Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!",
      }).then((result) => {
        if (result.value) {
          Swal.fire("Deleted!", "Your file has been deleted.", "success");
        }
      });
    });



  }),
    //init
    ($.SweetAlert = new SweetAlert()),
    ($.SweetAlert.Constructor = SweetAlert);
})(window.jQuery),
  //initializing
  (function ($) {
    "use strict";
    $.SweetAlert.init();
  })(window.jQuery);
