import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';

import '../html/body.html';

Template.main.onCreated(function() {
  this.counter = new ReactiveVar(0);

  // get JSON from python  display all projects?


});

Template.main.helpers({
  counter() {
    return Template.instance().counter.get();
  }
});

Template.main.events({
  'click button'(event, instance) {
    instance.counter.set(instance.counter.get() + 1);
  },
});
