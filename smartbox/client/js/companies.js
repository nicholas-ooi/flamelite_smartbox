import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.companies.onCreated(function() {
  HTTP.call("GET", "http://localhost:8080/ws/list_companies",
  (error, result) => {
    if (!error) {
      Session.set("companies", JSON.parse(result.content));
    }
  });

});

Template.companies.helpers({
  companies:() => {
    return Session.get("companies");
  }
});

Template.companies.events({

});
