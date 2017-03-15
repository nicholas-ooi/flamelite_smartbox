import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.workers.onCreated(function() {


});

Template.workers.helpers({
  workers:() => {
    return Session.get("project").workers;
  }
});

Template.workers.events({

});
