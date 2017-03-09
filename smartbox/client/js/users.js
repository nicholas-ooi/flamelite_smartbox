import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.users.onCreated(function() {
  HTTP.call("GET", "http://localhost:8080/ws/list_users",
  (error, result) => {
    if (!error) {
      Session.set("users", JSON.parse(result.content));
    }
  });

});

Template.users.helpers({
  users:() => {
    return Session.get("users");
  }
});

Template.users.events({

});
