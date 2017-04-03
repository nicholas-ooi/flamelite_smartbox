import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.updateStatus.onCreated(function() {
});

Template.updateStatus.helpers({
});

Template.updateStatus.events({

  'click .takePhoto': function(e, instance) {
    e.preventDefault();
    var cameraOptions = {
      width: 800,
      height: 600
    };

    MeteorCamera.getPicture(cameraOptions, function (error, data) {
      if (!error) {
        instance.$('.photo').attr('src', data);
        Session.set("photoData",data);
      }
    });
  }
  ,
  'submit #updateStatus':(e) =>
  {
    e.preventDefault();
    upload(Session.get("photoData"));

    var formData = new FormData();
    formData.append('project_id',Session.get("project").project_id);
    formData.append('comments', e.target.comments.value);
    $.ajax({
      type: 'POST',
      url:  SERVER+"submit_project_installed_update",
      data: formData,
      contentType: false,
      cache: false,
      processData: false,
      async: false,
      success: function(data) {

      }
    });


  }

});


function upload(data)
{
  var base64ImageContent = data.replace(/^data:image\/(png|jpg|jpeg);base64,/, "");
  var blob = base64ToBlob(base64ImageContent, 'image/jpeg');
  var formData = new FormData();
  formData.append('file', blob);
  formData.append('status_id',Session.get("statuses").current_status.status_id);
  $.ajax({
    type: 'POST',
    url:  SERVER+"add_status_photo",
    data: formData,
    contentType: false,
    cache: false,
    processData: false,
    async: false,
    success: function(data) {
      FlowRouter.go("/status");

    }
  });


}


function base64ToBlob(base64, mime)
{
    mime = mime || '';
    var sliceSize = 1024;
    var byteChars = window.atob(base64);
    var byteArrays = [];

    for (var offset = 0, len = byteChars.length; offset < len; offset += sliceSize) {
        var slice = byteChars.slice(offset, offset + sliceSize);

        var byteNumbers = new Array(slice.length);
        for (var i = 0; i < slice.length; i++) {
            byteNumbers[i] = slice.charCodeAt(i);
        }

        var byteArray = new Uint8Array(byteNumbers);

        byteArrays.push(byteArray);
    }

    return new Blob(byteArrays, {type: mime});
}
