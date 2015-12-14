$.ajaxSetup({
    headers: {
        "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val()
    },
});

function socialLogin(user) {
    console.log(user)
    var ajaxinfo = {
        url: "/photoapp/login/",
        type: "POST",
        data: user,
        success: function(data) {
            if (data == "success") {
                location.href= "/photoapp/photos/";
            }
        },
        error: function(error) {
            console.log(error.responseText)
        },
    headers: {
        "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val()
    },
    };
    $.ajax(ajaxinfo);
}

var facebookLogin = {
    config: {
        login: "#facebookLogin", //production value
        fb_id: '1098970130135656'
    },
    init: function(config) {
        $(facebookLogin.config.login).attr("disabled", true);
        if (config && typeof(config) == 'object') {
            $.extend(facebookLogin.config, config);
        }
        $.getScript("//connect.facebook.net/en_US/sdk.js", function() {
            FB.init({
                appId: facebookLogin.config.fb_id,
                version: "v2.5"
            });
            $(facebookLogin.config.login).attr("disabled", false);
        });
        $(facebookLogin.config.login).click(function(e) {
            e.preventDefault();
            facebookLogin.login();
        });
    },
    login: function() {
        FB.login(function(response) {
            if (response.authResponse) {
                console.log("Welcome!  Fetching your information.... ");
                FB.api("/me?fields=email,first_name,last_name,picture", socialLogin);
            } else {
                console.log("Not logged in");
            }
        }, {
            scope: "email,user_likes"
        });
    },
};

function showTable() {
    $('#once').show();
    localStorage.setItem('show', 'true'); //store state in localStorage
}

$(document).ready(function(){
    facebookLogin.init({
        login: "#facebookLogin", //test value
        fb_id: "1105396756159660"
    });
    //FB.getLoginStatus(updateStatusCallback);

    // $(".share").click(function(e){
    //     e.preventDefault();
    //     picture = $("#largeImage").find("img").attr("src");
    //     name = $("#largeImage").find("p").text();
    //     console.log(picture);
    //     console.log(location.href);

    //     FB.ui({
    //       method: 'feed',
    //       name: name,
    //       display: 'popup',
    //       link: location.href,
    //       caption:"Gentle Edit",
    //       picture: picture,
    //       description: 'I just used GentleEdit to edit my Photo.'
    //     }, function(response){

    //     });
    // })

    $(".share").click(function(e){
        e.preventDefault();

        var data = canvas.toDataURL('image/png');
        var resp = $('.image_upload').fileupload()
     $.cloudinary.image('image.jpg', {}, function(){

     })

        console.log(resp)




    })



    $('#editpicture-modal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var imageId = button.data('imageId')
        var imagePublicId = button.data('title')
        var imgdiv = $(this).find('img')
        var href = $(this).find('a')
        var getroute = "/photoapp/edit/" + imagePublicId + "/default"

        imgdiv.attr( "src", imageId );
        href.attr( "href", getroute );
    })



    //upload button
    $('.btn-file :file').change(function(event) {
        label = $(this).val().split('\\');
        $(this).closest('span').after('<p>' + label[label.length -1] +' </p>')
    });

     $('.object').click(function (e) {
        e.preventDefault();
        console.log("This is cliked")
        var url = $(this).data("effectUrl");

        $("#largeImage").load(url + " #largeImage")
     });

     $('.save').click(function (){

        var title = $('.pix').find('p').html()
        var image_src = $('.pix').find('img').attr("src")
        var save = $(this).find('a')
        save.attr('href', image_src);

     });

    var show = localStorage.getItem('show');
        if(show === 'true'){
            $('#once').show();
        }

    $('#uploadform').on('submit', function(event) {
            var $form = $(this);
            event.preventDefault();
            $('#fileupload-modal').hide();
            $('.modal').modal('hide');

            var fd = new FormData();

            var file_data = $form.find('input[type="file"]')[0].files[0];
            fd.append("image", file_data);
            var other_data = $form.serializeArray();
            $.each(other_data, function(key, input) {
                fd.append(input.name, input.value);
            });

            $.ajax({
                type: "POST",
                url: $form.attr('action'),
                data: fd,
                contentType:false,
                processData: false,

                success: function(data) {
                if (data == "success") {
                    var url = "/photoapp/photos/"
                    $("#reload").load(url + " #reload")
                }
            },
                error: function(error) {
                    console.log(error.responseText)
                },

                headers: {
                    "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val()
                    },

            });

        });


})

