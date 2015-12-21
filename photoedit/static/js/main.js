var timeout;
$.ajaxSetup({
    headers: {
        "X-CSRFToken": $("meta[name='csrf-token']").attr("content"),
        'Cache-Control': 'no-store'
    },
});
$.ajaxSetup({ cache: false });

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

function BindEvents()
{
    $("body").on('click', ".editpix", function(e){
        e.preventDefault();
        $('#begin').hide();
        var imageUrl = $(this).find('img').attr('src');
        var imgDiv = $('#pixedit').find('img');
        var effectsDiv = $('.effects').find('button');

        var imagePath = $(this).attr('data-image-id')
        var imageName = $(this).attr('data-name')
        var imageidentity = $(this).attr('data-title')

        imgDiv.attr( "src", imageUrl );
        imgDiv.attr('data-name', imageName)
        imgDiv.attr('data-title', imageidentity)
        effectsDiv.attr('data-image-id', imagePath)

        $(".flex").show();
        $('#fbk').show();
        $('.save').show();

    })
}

function UploadForm()
{
    $('#uploadform').on('submit', function(event) {
            event.preventDefault();
            var notify = $.notify('<strong>Upload</strong> in progress ...', {
                allow_dismiss: true,
                showProgressbar: false
                });

            var $form = $(this);
            $('#fileupload-modal').hide();
            $('.modal').modal('hide');
            $form.find('p').remove();

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

                $(".welcome1").hide();

                clearTimeout(timeout);
                timeout = setTimeout(function() {
                notify.update({'type': 'success', 'message': '<strong>Success</strong> Upload complete!', 'progress': 25});
                }, 3000);

                if (data == "success") {
                    var url = "/photoapp/photos/"
                    $("#reload").load(url + " #reload")
                }
            },
                error: function(error) {
                    console.log(error.responseText)

                    if (error.status == 405) {
                        //alert badrequest
                        alert("File size should not exceed 10MB")
                    } else {
                        //alert file toolarge
                        alert("An Error Occurred While Uploading File.")

                    }
                },

                headers: {
                    "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val()
                    },
            });
        });
}

function Uploadbutton() {
    $('.btn-file :file').change(function(event) {
        label = $(this).val().split('\\');
        $(this).closest('span').after('<p>' + label[label.length -1] +' </p>')
    });
}

function ApplyEffects()
    {
        $("body").on('click', ".setup", function(e){
        e.preventDefault();
        var image = $(this).find('button').attr('data-image-id')
        var imgeffect = $(this).attr('data-effect')
        $(".loader").show();//preloader show

        $.ajax({
            type: "GET",
            url: "/photoapp/addeffects/",
            data: {'image': image, 'effect': imgeffect },
            success: function(data) {
               var avatatr = $("#avatar").attr("src", '/'+ data + "?" + new Date().getTime());
                $("#frameid").html(avatar);
                $(".loader").hide();

            },

            error: function(error) {
                    console.log(error.responseText)
                },
        });
    });
}

function DeleteImage()
    {
        $("body").on('click', "#confirmdelete", function(e){
            e.preventDefault();
            var imagePath = $(this).attr('data-image-id')
            var imageId = $(this).attr('data-title')

            $.ajax({
                type: "GET",
                url: "/photoapp/delete/",
                data: {'path': imagePath, 'id': imageId },
                success: function(data) {
                    if (data == "success") {

                        var notify = $.notify('<strong>Image</strong> successfully deleted...', {
                                type: 'success',
                                allow_dismiss: true,
                                showProgressbar: false
                            });

                        $('#delete-modal').hide();
                        $('.modal').modal('hide');

                        var url = "/photoapp/photos/"
                        $("#reload").load(url + " #reload")
                        var img_id = $('.frame').find('img').attr('data-title')

                        if (img_id == imageId) {
                            $("#avatar").hide();
                            $("#repeat").show();
                        }
                    }
                },

                error: function(error) {
                        console.log(error.responseText)
                    },
        });//end ajax
    })//end
}

function SaveImage(){

     $("body").on("click", ".save", function (){

        var title = $('.pix').find('p').html()
        var image_src = $('.pix').find('img').attr("src")
        var save = $(this).find('a')
        save.attr('href', image_src);

     });
}

function DeleteModalProperty(){

    $('#delete-modal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget) // Button that triggered the modal
        var imagePath = button.closest(".editpix").attr('data-image-id')
        var imageId = button.closest(".editpix").attr('data-title')

        var deleteDiv = $('#photodeletediv').find('button');
        deleteDiv.attr('data-image-id', imagePath)
        deleteDiv.attr('data-title', imageId)

    })
}

function FacebookShare() {

     $("body").on('click', ".share", function(e){
        e.preventDefault();
        picture = $(".frame").find("img").attr("src");
        name = $(".frame").find("img").attr('data-name');
        console.log(picture);
        console.log(name);

        FB.ui({
          method: 'feed',
          name: name,
          display: 'popup',
          link: location.protocol + '//' + location.host,
          caption:"Gentle Edit",
          picture: "http://" + location.host + picture,
          description: 'I just used GentleEdit to edit my Photo.'
        }, function(response){

        });


    })

}

function KeepUploadButton() {
    var show = localStorage.getItem('show');
        if(show === 'true'){
            $('#once').show();
        }
}

function DownloadFile() {

    $("body").on('click', ".save", function(){
        var link = document.createElement('a');
        link.href = $('.pix').find('img').attr("src")
        link.download = $('.frame').find('img').attr('data-name')
        document.body.appendChild(link);
        link.click();
    });
}

$(document).ready(function(){
    facebookLogin.init({
        // login: "#facebookLogin", //test value
        // fb_id: "1105396756159660"
    })

    BindEvents();
    ApplyEffects();
    UploadForm();
    Uploadbutton();
    SaveImage();
    DeleteImage();
    DeleteModalProperty();
    FacebookShare();
    DownloadFile();

})

