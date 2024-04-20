
$(function () {

  ///نمایش زیر منو
  $(".showSubMenu").click(function () {
    $(this).nextAll("ul").toggleClass("show");
    $(this).toggleClass('open');
  })

  ///نمایش مگامنو آپدیدت جدید
  $(".main-menu-head").hover(function(){
    $(this).children().find(".main-menu-sub").first().addClass('main-menu-sub-active');
    $(this).children().addClass('active');
  })
  $(".main-menu-head").mouseleave(function(){
    $(this).children().find(".main-menu-sub").first().removeClass('main-menu-sub-active');
    $(this).children().removeClass('active');
  })
  $(".main-menu li").mouseover(function () {

    $(".main-menu li").removeClass("main-menu-sub-active-li");
    $(this).addClass("main-menu-sub-active-li");
    $(".main-menu-sub").removeClass('main-menu-sub-active');
    $(this).children('ul').removeClass('main-menu-sub-active');
    $(this).children('ul').addClass('main-menu-sub-active');
  });
  $(".main-menu-sub-active").mouseleave(function(){
    $(".main-menu-sub-active").removeClass("main-menu-sub-active");
  })

  ///شمارنده محصول برای اضافه کردن به سبد خرید
  $("input[name='count']").TouchSpin({
    min: 1,
    max: '1000000000000000',
    buttondown_class: "btn-counter waves-effect waves-light",
    buttonup_class: "btn-counter waves-effect waves-light"
  });

  ///انتخاب گر رنگ
  $(".category-sort .form-checks .form-check").click(function () {
    $(".category-sort .form-checks .form-check").removeClass("active");
    $(this).addClass('active');
    $(".category-sort .form-checks .form-check").children("input[type=radio]").attr('checked', false);
    $(this).children("input[type=radio]").attr('checked', true);
  })


  ///انتخاب زمان ارسال
  $(".send-item").click(function () {
    $(".send-item").removeClass("active");
    $(this).addClass('active');
  })

  ///انتخاب روش پستی
  $(".shipping-item").click(function () {
    $(".shipping-item").removeClass("active");
    $(this).addClass('active');
  })

  ///انتخاب روش پرداخت
  $(".bank-item").click(function () {
    $(".bank-item").removeClass("active");
    $(this).addClass('active');
  })



  jQuery('[data-bs-toggle="tooltip"]').tooltip();
  jQuery('[data-bs-toggle="modal"][title]').tooltip();

});



// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}
