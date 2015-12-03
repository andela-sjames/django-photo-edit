$.ajaxSetup({
    headers: {
        "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val()
    },
    beforeSend:function(){
        $("#preloader").show();
    },
    complete:function(){
        $("#preloader").hide();
    }
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
        login: "#facebook",
        fb_id: '12345678910'
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


$(document).ready(function(){    
    facebookLogin.init({
        login: "#facebookLogin",
        fb_id: "1098970130135656"
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
    

})

