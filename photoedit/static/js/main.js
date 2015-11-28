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

function chooseFile() {
        $("#fileInput").click();
    }

function handleFileSelect(evt) {
    var files = evt.target.files; // FileList object

    // files is a FileList of File objects. List some properties.
    var output = [];
    for (var i = 0, f; f = files[i]; i++) {
      output.push('<li><strong>', escape(f.name), '</strong> (', f.type || 'n/a', ') - ',
                  f.size, ' bytes, last modified: ',
                  f.lastModifiedDate ? f.lastModifiedDate.toLocaleDateString() : 'n/a',
                  '</li>');
    }
    document.getElementById('list').innerHTML = '<ul>' + output.join('') + '</ul>';
  }


function imageHandler(e2) 
{ 
  var store = document.getElementById('imgstore');
  store.innerHTML='<img src="' + e2.target.result +'">';
}



$(document).ready(function(){    
    facebookLogin.init({
        login: "#facebookLogin",
        fb_id: "1098970130135656"
    })

    $("#fileInput").change(handleFileSelect);

})