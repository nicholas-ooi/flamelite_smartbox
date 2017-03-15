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
         }
      });
  }

});
