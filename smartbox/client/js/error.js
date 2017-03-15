import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.error.onCreated(function() {
});

Template.error.helpers({
  errorMsg:() => {
    return Session.get("errorMsg");
  }
});

Template.error.events({

});
