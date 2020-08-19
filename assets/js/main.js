jQuery(document).ready(function() {
    var btn = $('#scroll');
    $(window).scroll(function() {
      if ($(window).scrollTop() > 500) {
        btn.show();
      } else {
        btn.hide();
      }
    }); 
    btn.click(function(){ 
        $("html, body").animate({ scrollTop: 0 }, 500); 
        return false; 
    }); 
  
  });