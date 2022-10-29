$(function () {
    // counter js
       $('.counter').counterUp({
                delay: 10,
                time: 1000
            });
    
    // wow js
     new WOW().init();
    
  /* about part start */
  $('.about_slider').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    dots: false,
    arrows: false,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
        }
    },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1
        }
    },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
    }
  ]
  });
  /* about part end */

  /* video part start */
  $('.venobox_custom').venobox({
    framewidth: '800px', // default: ''
    frameheight: '500px', // default: ''
    border: '5px', // default: '0'
    bgcolor: '#ddd', // default: '#fff'
    titleattr: 'data-title', // default: 'title'
    numeratio: false, // default: false
    infinigall: false, // default: false
  });
  /* video part End */

  /* gallary part start */
  $(document).ready(function () {
    $('.venobox').venobox();
  });
  /* gallary part end */

  /* doctor part start */
  $('.doctor_slider').slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    dots: false,
    arrows: false,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
        }
    },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1
        }
    },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
    }
  ]
  });
  /* doctor part end */



  //animation scroll js
  var html_body = $('html, body');
  $('nav a').on('click', function () {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
      if (target.length) {
        html_body.animate({
          scrollTop: target.offset().top - 50
        }, 1500);
        return false;
      }
    }
  });

  /* Back to Top Button start */
  $(window).scroll(function () {
    var sticky = $("#menu_part");
    var $scrolling = $(this).scrollTop();
    var bc2top = $(".back2top");
    if ($scrolling > 150) {
      bc2top.fadeIn(1000);
    } else {
      bc2top.fadeOut(1000);
    }

    if ($scrolling > 80) {
      sticky.addClass("navbg"); // navbg is a sticky menu class only for css
    } else {
      sticky.removeClass("navbg");
    }
  });

  // Closes responsive menu when a scroll link is clicked
  $('.nav-link').on('click', function () {
    $('.navbar-collapse').collapse('hide');
  });


  $('.back2top').click(function (e) {
    e.preventDefault();
    $('html,body').animate({
      scrollTop: 0
    }, 1500);
  });
  /* Back to Top Button End */
});
