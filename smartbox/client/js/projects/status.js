import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.status.onRendered(function() {

  $('body').off("click").on('click', '.accordian-title', function() {
    let $this = $(this);
    let $drawer = "#" + $this.data("accordian-drawer");
    $drawer = $($drawer);

    if (!$drawer.hasClass("closed")) {
      TweenLite.to($drawer, 0.5, {
        height: 0,
        ease: Cubic.easeOut
      });
      $drawer.addClass("closed");
      TweenLite.to($this.find(".accordion-drawer-icon"), 0.6, {
        rotation: 0,
        ease: Cubic.easeOut
      });

    } else {
      TweenLite.set($drawer, {
        height: "auto"
      })
      TweenLite.from($drawer, 0.5, {
        height: 0,
        ease: Cubic.easeOut
      });
      $drawer.removeClass("closed");
      TweenLite.to($this.find(".accordion-drawer-icon"), 0.6, {
        rotation: 90,
        ease: Cubic.easeOut
      });
    }
  });

});

Template.status.onCreated(function() {

  const id = Session.get("project").project_id;
  HTTP.call("GET", SERVER+"retrieve_project_statuses", {params:{project_id:id}},
  (error, result) => {
    Session.set("statuses", JSON.parse(result.content));
  });

  HTTP.call("GET", SERVER+"retrieve_project_complaints", {params:{project_id:id}},
  (error, result) => {
    if (!error) {
      Session.set("complaints", JSON.parse(result.content));
    }
    else {
      alert(error);
    }
  });



});

Template.status.helpers({
  past_statuses:() => {
    return Session.get("statuses").past_statuses;
  },
  current_status:() => {
    return Session.get("statuses").current_status;
  },
  resolvedSize:() => {
    return Session.get("complaints").resolved.length;
  },
  unresolvedSize:() => {
    return Session.get("complaints").unresolved.length;
  },
  reviewedSize:() => {
    return Session.get("complaints").reviewed.length;
  },
  resolved:() => {
    return Session.get("complaints").resolved;
  },
  unresolved:() => {
    return Session.get("complaints").unresolved;
  },
  reviewed:() => {
    return Session.get("complaints").reviewed;
  },
});

Template.status.events({

});
