$(document).ready(function (){
    var publisher_id = window.location.pathname.match(/\/([^\/]+?)\/(?:\?|$)/i)[1];
    $('#publisher_form fieldset:first-child').append('<div>' +
        '<div class="form-row">' +
            '<label for="parse_all">Parse all:</label>' +
            '<img class="loading" src="/static/img/loading.gif" alt="loading" style="display:none;" /><a id="parse_all"><img src="/static/img/utils.parse.png" style="cursor:pointer;" /></a>' +
        '</div>'+
    '</div>');
    $('#parse_all').click(function(){
        var image = $(this).find('img'),
            loading = $(this).parent().find('.loading');
        $.ajax({
            type: "GET",
            data: ({'publisher_id': publisher_id}),
            url: "/admin/iati_synchroniserp/publisher/parse-publisher/",
            beforeSend: function() {
                image.hide();
                loading.show();
            },
            statusCode: {
                200: function() {
                    loading.hide();
                    image.attr('src', '/static/img/utils.parse.success.png');
                    image.show();
                },
                404: function() {
                    loading.hide();
                    image.attr('src', '/static/img/utils.parse.error.png');
                    image.show();
                },
                500: function() {
                    loading.hide();
                    image.attr('src', '/static/img/utils.parse.error.png');
                    image.show();
                }
            }
        });
    });

    $('#count-publisher-activities').click(function(){
       $.ajax({
           type: "GET",
           url: "/admin/iati_synchroniserp/publisher/count-publisher-activities/",
           beforeSend: function() {
               $('#count-publisher-activities').text("Updating...");
           },
           statusCode: {
               200: function() {
                   $('#count-publisher-activities').text("Updated");
               },
               404: function() {
                   $('#count-publisher-activities').text("404 error...");
               },
               500: function() {
                   $('#count-publisher-activities').text("500 error...");
               }
           }
       });
   });
});