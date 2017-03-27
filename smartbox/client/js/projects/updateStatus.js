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

    // faking base64 image data
    // let data = "type:image/jepg;base,ZmFrZQ==";
    // upload(data);

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
    upload(Session.get("photoData"));
  }

});


function upload(data)
{
  alert(data);
  const file = dataToFile(data);
  var formData = new FormData();
  formData.append('file', file);
  $.ajax({
    type: 'POST',
    url:  SERVER+"upload_file",
    data: formData,
    contentType: false,
    cache: false,
    processData: false,
    async: false,
    success: function(data) {
      console.log(data);
      alert(data);
    }
  });


}


function dataToFile(dataURI) {
  alert(dataURI.split(',')[1]);
  let byteString = atob(dataURI.split(',')[1]);
  let ab = new ArrayBuffer(byteString.length);
  let ia = new Uint8Array(ab);
  let ext = "jpg";
  const fileType = dataURI.split(',')[0].split(";")[0].split(":")[1];
  const d = new Date();

  for (let i = 0, length = byteString.length; i < length; i++) {
    ia[i] = byteString.charCodeAt(i);
  }
  switch(fileType)
  {
    case "image/jpeg":
    ext = "jpg";
    break;
    case "image/png":
    ext = "png";
    break;
  }
  return new File([ab], d.getTime()+"."+ext, { type: fileType });
};
