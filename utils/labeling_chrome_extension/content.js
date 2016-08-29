// Set port to 'background.js'
var port = chrome.runtime.connect();

// Add click event by command input
$('img.rg_i.rg_ic').on('click', function (e) {
  $('img.rg_i.rg_ic').css('opacity', '');
  $(this).css('opacity', '0.2');
  // Send index of image to 'background.js'
  port.postMessage($(this).parent().parent().attr('data-ri'));
});
// Add click event by scroll
$(window).scroll(function (e) {
  $('img.rg_i.rg_ic').off('click').on('click', function (e) {
    $('img.rg_i.rg_ic').css('opacity', '');
    $(this).css('opacity', '0.2');
    // Send index of image to 'background.js'
    port.postMessage($(this).parent().parent().attr('data-ri'));
  });
});
