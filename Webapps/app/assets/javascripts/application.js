// This is a manifest file that'll be compiled into application.js, which will include all the files
// listed below.
//
// Any JavaScript/Coffee file within this directory, lib/assets/javascripts, vendor/assets/javascripts,
// or any plugin's vendor/assets/javascripts directory can be referenced here using a relative path.
//
// It's not advisable to add code directly here, but if you do, it'll appear at the bottom of the
// compiled file.
//
// Read Sprockets README (https://github.com/rails/sprockets#sprockets-directives) for details
// about supported directives.
//
//= require jquery
//= require jquery_ujs
//= require twitter/bootstrap
//= require turbolinks
//= require jquery.turbolinks
//= require_tree .



function remove_fields(link) {
  $(link).prev("input[type=hidden]").val("1");
  $(link).closest(".form-group").remove();
}

function add_fields(link, association, content) {
  var new_id = new Date().getTime();
  var regexp = new RegExp("new_" + association, "g")
  content = content.replace(regexp, new_id)
  $(content).hide()
  $("#" + link).append($(content))
}

$(document).ready(function() {

    $('#match_table tbody tr').click(function() {
        var match_id = $(this).find("#match_id").attr("value");
        window.location = "/matches/" + match_id
    });

    $('#league_table tbody tr').click(function() {
        var league_id = $(this).find("#league_id").attr("value");
        window.location = "/leagues/" + league_id
    });
    
    $( "#new_league" ).submit(function( event ) {
      var l = $('#competitor_fields > div').length
      if(l < 2) {
        alert("There must be at least 2 competitors")
        event.preventDefault();
        return false;
      }
      if($("#league_fixture_tournament").is(':checked')) {
         if(l == 0 || l & (l - 1) != 0){
           alert("Competitors of a tournament must be a power of 2");
           event.preventDefault();
           return false;
         }
      }
      event.submit();
    });    

});