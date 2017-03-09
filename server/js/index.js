function load_projects(){
    $.getJSON("ws/list_projects", function(data){
        content = "<table cellspacing='10px'>";
        $.each(data, function (index, project) {
            content += "<tr><td>Project ID</td><td>:</td><td>" + project.project_id + "</td></tr>";
            content += "<tr><td>Project Title</td><td>:</td><td>" + project.project_title + "</td></tr>";
        	content += "<tr><td>Project Description</td><td>:</td><td>" + project.project_description + "</td></tr>";
        	content += "<tr><td>Company</td><td>:</td><td>" + project.company.name + "</td></tr>";
            content += "<tr><td valign='top'>Materials</td><td valign='top'>:</td><td>";
            for(var i=0; i<project.materials_qty.length; i++){
                var material_qty = project.materials_qty[i];
                content += material_qty.material.name + ": " + material_qty.quantity + "<br/>";
            }
            content += "</td></tr>";
            content += "<tr><td valign='top'>Timelines</td><td valign='top'>:</td><td>";
            for(var i=0; i<project.timelines.length; i++){
                var timeline = project.timelines[i];
                content += timeline.name + ", " + timeline.start_date + " to " + timeline.end_date + "<br/>";
            }
            content += "</td></tr>";
        	content += "<tr><td>Site Manager</td><td>:</td><td>" + project.site_manager.name + "</td></tr>";
            content += "<tr><td valign='top'>Workers</td><td valign='top'>:</td><td>";
            for(var i=0; i<project.workers.length; i++){
                var worker = project.workers[i];
                for(var j=0; j<worker.work_half_hours.length; j++){
                    var half_hours = worker.work_half_hours[j];
                    pay_calcuation = calculate_pay(worker, half_hours);
                    hourly_pay = pay_calcuation[0];
                    num_of_hours = pay_calcuation[1];
                    OT_hours = pay_calcuation[2];
                    OT_pay = pay_calcuation[3];
                    total_pay = pay_calcuation[4];
        			content += worker.name + ", " + half_hours.date + ", hourly pay = $" + hourly_pay + ", " + num_of_hours + " hrs worked";
        			content += ", OT " + OT_hours + " hours, OT pay = $" + OT_pay;
        			content += ", total pay = $" + total_pay + "<br/>";
                }
            }
        	content += "</td></tr>";
            content += "<tr><td valign='top'>Complaints</td><td valign='top'>:</td><td>";
            for(var i=0; i<project.complaints.length; i++){
                var complaint = project.complaints[i];
                if (complaint.resolution_status === 'unresolved'){
                    content += complaint.date_added + " - " + complaint.complaint + " | " + complaint.resolution_status + "<br/>"
                } else {
                    content += complaint.date_added + " - " + complaint.complaint + " | " + complaint.resolution_status + " - " + complaint.action_taken + "<br/>"
                }
            }
        	content += "</td></tr>"
        	content += "<tr><td colspan='3'><hr/></td></tr>"
        });
        $('#container').html(content)
    });
}

function calculate_pay(worker, half_hours){
    var normal_work_hours = 8
    var OT_rate = 1.5

    var hourly_pay = worker.salary/24/8;
    var num_of_hours = half_hours.num_of_half_hours/2;
    var OT_hours = (num_of_hours - normal_work_hours > 0) ? num_of_hours - normal_work_hours : 0;
    var OT_pay = OT_hours * hourly_pay * OT_rate;
    var total_pay = hourly_pay * num_of_hours + OT_pay;
    return [hourly_pay.toFixed(2), num_of_hours.toFixed(1), OT_hours.toFixed(1), OT_pay.toFixed(2), total_pay.toFixed(2)];
}

$(document).ready(load_projects);
