import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.employees.onCreated(function() {
  HTTP.call("GET", "http://localhost:8080/ws/list_employees",
  (error, result) => {
    if (!error) {
      Session.set("employees", JSON.parse(result.content));
    }
  });

});

Template.employees.helpers({
  employees:() => {
    return Session.get("employees");
  }
});

Template.employees.events({

});
