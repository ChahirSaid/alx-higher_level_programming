$(document).ready(function() {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    success: function(data) {
      $('div#hello').text(data.hello);
    },
    error: function() {
      $('div#hello').text('Failed to fetch translation');
    }
  });
});
