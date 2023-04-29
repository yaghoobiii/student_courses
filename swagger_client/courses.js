var userId = $.cookie("user_id"), token = $.cookie("token");
if (!userId || !token) location.assign("/");

// Load courses
const week = {
    0: "شنبه",
    1: "یک شنبه",
    2: "دو شنبه",
    3: "سه شنبه",
    4: "چهارشنبه",
    5: "پنجشنبه",
    6: "جمعه",
};
$.get("/courses", "token=" + token, function (courses) {
    for (let i = 0; i < courses.length; i++) $("#coursesTBody").append(
        "    <tr>" +
        "      <td><input type=\"checkbox\" class=\"select\" name=\"\"></td>" +
        "      <td>" + courses[i].teacher_name + "</td>" +
        "      <td>" + courses[i].name + "</td>" +
        "      <td>" + week[courses[i].weak_day] + "</td>" +
        "      <td>" + courses[i].start_time + "</td>" +
        "      <td>" + courses[i].end_time + "</td>" +
        "    </tr>"
    )
    $(".select").change(function () {
        if (this.checked) {
            // TODO
        }
    });
});

$("#SelectAll").click(() => {
    let select = document.getElementsByClassName('select');
    if ($("#SelectAll").checked === true) {
        for (let i = 0; i < select.length; i++) {
            select[i].checked = true;
            document.querySelector('button').style.display = 'block';
        }
    } else {
        for (let i = 0; i < select.length; i++) {
            select[i].checked = false;
            document.querySelector('button').style.display = 'none';
        }
    }
});
