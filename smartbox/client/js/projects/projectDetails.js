import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.projectDetails.onCreated(function() {
  const id = parseInt(FlowRouter.getParam("id"));
  HTTP.call("GET", SERVER+"retrieve_project_details", {params:{project_id:id}},
  (error, result) => {
    Session.set("project", JSON.parse(result.content));
  });

  console.log(Session.get("project"));

});

Template.projectDetails.helpers({
  title:() => {
    return Session.get("project").project_title;
  },
  id:() => {
    return Session.get("project").project_id;
  },
  description:() => {
    return Session.get("project").project_description;
  },
  company:() => {
    return Session.get("project").company_name;
  },
  pocName:() => {
    return Session.get("project").poc_name;
  },
  pocContact:() => {
    return Session.get("project").poc_contact;
  },
  project_materials:() => {
    return Session.get("project").project_materials;
  },
  project_timelines:() => {
    return Session.get("project").project_timelines;
  },
});

Template.projectDetails.events({

});
