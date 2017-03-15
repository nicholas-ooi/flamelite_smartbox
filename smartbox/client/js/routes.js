import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

const layout = "body";

FlowRouter.route('/', {
  name: 'Login.show',
  action() {
    Session.set("pageTitle","Flamelite SmartBox");
    BlazeLayout.render(layout, {isBottomNav:false,main: 'login'});
  }
});

FlowRouter.route('/projects', {
  name: 'Projects.show',
  action() {
    Session.set("pageTitle","Projects");
    Session.set("error", null);

    BlazeLayout.reset();
    BlazeLayout.render(layout, {isBottomNav:false,main: 'projects'});
  }
});

FlowRouter.route('/status', {
  name: 'Status.show',
  action() {
    Session.set("pageTitle","Status");
    Session.set("error", null);
    BlazeLayout.reset();
    BlazeLayout.render(layout, {isBottomNav:true,main: 'status'});
  }
});

FlowRouter.route('/updateStatus', {
  name: 'UpdateStatus.show',
  action() {
    Session.set("pageTitle","Update Status");
    Session.set("error", null);
    BlazeLayout.reset();
    BlazeLayout.render(layout, {isBottomNav:true,main: 'updateStatus'});
  }
});

FlowRouter.route('/recordWorkHours', {
  name: 'RecordWorkHours.show',
  action() {
    Session.set("pageTitle","Record Work Hours");
    Session.set("error", null);
    BlazeLayout.reset();
    BlazeLayout.render(layout, {isBottomNav:true,main: 'recordWorkHours'});
  }
});

FlowRouter.route('/recordWorkHours2', {
  name: 'RecordWorkHours2.show',
  action() {
    Session.set("pageTitle","Record Work Hours");
    Session.set("error", null);
    BlazeLayout.reset();
    BlazeLayout.render(layout, {isBottomNav:true,main: 'recordWorkHours2'});
  }
});

FlowRouter.route('/projectDetails/:id', {
  name: 'Projects.show',
  action() {
    Session.set("pageTitle","Project");
    Session.set("error", null);
    BlazeLayout.reset();
    BlazeLayout.render(layout, {isBottomNav:true,main: 'projectDetails'});
  }
});



FlowRouter.route('/workers', {
  name: 'Workers.show',
  action() {
    Session.set("pageTitle","Workers");
    Session.set("error", null);

    BlazeLayout.reset();
    BlazeLayout.render(layout, {isBottomNav:true,main: 'workers'});
  }
});

// FlowRouter.route('/users', {
//   name: 'Users.show',
//   action() {
//     Session.set("pageTitle","Users");
//     Session.set("error", null);
//     BlazeLayout.reset();
//     BlazeLayout.render(layout, {isBottomNav:true,main: 'users'});
//   }
// });
//
// FlowRouter.route('/companies', {
//   name: 'Companies.show',
//   action() {
//     Session.set("pageTitle","Companies");
//     Session.set("error", null);
//
//     BlazeLayout.render(layout, {isBottomNav:true,main: 'companies'});
//   }
// });
