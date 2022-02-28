(function($) {

	"use strict";


})(jQuery);

$('input[type="checkbox"]').on('change', function() {
    $('input[type="checkbox"]').not(this).prop('checked', false);
 });