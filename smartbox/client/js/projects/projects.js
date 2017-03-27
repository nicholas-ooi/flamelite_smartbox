import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.projects.onCreated(function() {

  Session.setDefault("projects",null);
  Session.setDefault("pastProjects",null);
  Session.setDefault("project",null);
  Session.setDefault("workers",null);
  Session.setDefault("statuses",null);
  Session.setDefault("complaints",null);

  const user = Session.get("user");
  HTTP.call("GET", SERVER+"list_site_manager_projects", {params:{site_manager_id:user.user_id}},
  (error, result) => {
    Session.set("projects", JSON.parse(result.content));
  });

  HTTP.call("GET", SERVER+"list_site_manager_projects", {params:{site_manager_id:user.user_id}},
  (error, result) => {
    Session.set("pastProjects", JSON.parse(result.content));
  });

});

Template.projects.helpers({
  projects:() => {
    return Session.get("projects");
  },
  pastProjects:() => {
    return _.filter(Session.get("pastProjects"), function(p){ return p.status=="completed"; });
  }
});

Template.projects.events({

});
