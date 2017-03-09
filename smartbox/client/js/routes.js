import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';


const layout = "body";

FlowRouter.route('/', {
  name: 'Projects.show',
  action() {
    Session.set("pageTitle","Projects");
    BlazeLayout.render(layout, {main: 'main'});
  }
});

FlowRouter.route('/users', {
  name: 'Users.show',
  action() {
    Session.set("pageTitle","Users");
    BlazeLayout.render(layout, {main: 'users'});
  }
});

FlowRouter.route('/companies', {
  name: 'Companies.show',
  action() {
    Session.set("pageTitle","Companies");
    BlazeLayout.render(layout, {main: 'companies'});
  }
});

FlowRouter.route('/employees', {
  name: 'Employess.show',
  action() {
    Session.set("pageTitle","Employees");
    BlazeLayout.render(layout, {main: 'employees'});
  }
});
