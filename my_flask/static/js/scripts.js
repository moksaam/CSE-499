$("form[name=signup_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/signup",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            window.location.href = "/index/";
        },
        error: function(resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});

$("form[name=login_form").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/user/login",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            window.location.href = "/index/";
        },
        error: function(resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});

$("form[name=saveCharacter").submit(function(e) {

    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/character/save",
        type: "POST",
        data: data,
        dataType: "json",
        success: function(_resp) {
            console.log();
        },
        error: function(resp) {
            $error.text(resp.responseJSON.error).removeClass("error--hidden");
        }
    });

    e.preventDefault();
});