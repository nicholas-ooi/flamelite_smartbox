import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.workers.onCreated(function() {

  const id = Session.get("project").project_id;
  HTTP.call("GET", SERVER+"retrieve_project_workers", {params:{project_id:id}},
  (error, result) => {
    Session.set("workers", JSON.parse(result.content));
  });

});

Template.workers.helpers({
  workers:() => {
    return Session.get("workers");
  }
});

Template.workers.events({

});
