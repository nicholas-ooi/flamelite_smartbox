import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.header.onCreated(function() {
});

Template.header.helpers({
  pageTitle:() => {
    return Session.get("pageTitle");
  }
});

Template.header.events({

});
