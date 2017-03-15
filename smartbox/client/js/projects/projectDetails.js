import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.projectDetails.onCreated(function() {
  const id = parseInt(FlowRouter.getParam("id"));
  Session.set("project",_.findWhere(Session.get("projects"), {project_id: id}));
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
    return Session.get("project").company.name;
  },
  pocName:() => {
    return Session.get("project").poc_name;
  },
  pocContact:() => {
    return Session.get("project").poc_contact;
  }
});

Template.projectDetails.events({

});
