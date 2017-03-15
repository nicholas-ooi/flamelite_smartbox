import { Template } from 'meteor/templating';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.login.onCreated(function() {


});

Template.login.helpers({



});

Template.login.events({

  "submit #login":(e) =>
  {
    e.preventDefault();
    const username = e.target.username.value;
    const password = e.target.password.value;
    HTTP.call("POST", "http://localhost:8080/ws/login",{data: {username:username,password:password}},
    (error, result) => {
      const res = result.content;
      if (res != "None") {
        Session.set("user", JSON.parse(res));
        FlowRouter.go("/projects");
      }
      else {
        Session.set("errorMsg","Username and password does not exist.");
      }
    });

  }

});
