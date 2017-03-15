import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.userProfile.onCreated(function() {


});

Template.userProfile.helpers({

  name:()=>
  {
    return Session.get("user").username;
  }
  ,
  title:()=>
  {
    return Session.get("user").role;
  }

});
