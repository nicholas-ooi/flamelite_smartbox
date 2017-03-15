import { Template } from 'meteor/templating';
import { Session } from 'meteor/session';

Template.bottomnav.events({

});

Template.bottomnav.helpers({
  isActive:(link) => {
    return FlowRouter.current().path.includes(link)?"active":"";
  },
  pid:()=>
  {
    return Session.get("project").project_id;
  }
});
