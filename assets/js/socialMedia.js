jQuery(document).ready(function() {
    var btn = $('#social-media');
    $(window).scroll(function() {
      if ($(window).scrollTop() > 300) {
        btn.show();
      } else {
        btn.hide();
      }
    });
  
  });