import { Template } from 'meteor/templating';
import { ReactiveVar } from 'meteor/reactive-var';
import { Session } from 'meteor/session';
import { HTTP } from 'meteor/http';

Template.status.onCreated(function() {


  $('body').on('click', '.accordian-title', function() {
  	var $this = $(this);
  	var $drawer = "#" + $this.data("accordian-drawer");
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

Template.status.helpers({
  complaints:() => {
    return Session.get("project").complaints;
  },
  statuses:() => {
    return Session.get("project").timelines;
  }
});

Template.status.events({

});
