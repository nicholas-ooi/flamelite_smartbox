import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.recordWorkHours.onCreated(function() {
});

Template.recordWorkHours.helpers({
});

Template.recordWorkHours.events({
  "submit #recordWorkHours":(e)=>
  {
      e.preventDefault();
      FlowRouter.go("/recordWorkHours2");
  }
});
