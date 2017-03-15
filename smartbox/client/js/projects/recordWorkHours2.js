import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.recordWorkHours2.onCreated(function() {
});

Template.recordWorkHours2.helpers({
});

Template.recordWorkHours2.events({
  "submit #recordWorkHours":(e)=>
  {
    e.preventDefault();
    FlowRouter.go("/workers");
  }
});
