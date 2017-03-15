import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.projects.onCreated(function() {

  HTTP.call("GET", "http://localhost:8080/ws/list_projects",
  (error, result) => {
    if (!error) {
      Session.set("projects", JSON.parse(result.content));
      console.log(JSON.parse(result.content));
    }
  });

});

Template.projects.helpers({
  projects:() => {
    return Session.get("projects");
  }
});

Template.projects.events({

});
