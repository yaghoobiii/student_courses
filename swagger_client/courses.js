var userId = $.cookie("user_id"), token = $.cookie("token"), tokenQuery = "token=" + token;
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
$.get("/courses", tokenQuery, function (courses) {
    $.get("/selections/" + userId, tokenQuery, function (selections) {
        loaded(courses, selections)
    })
});

function loaded(courses, selections) {
    var selected = selections.map(sel => sel.course);
    for (let i = 0; i < courses.length; i++) $("#coursesTBody").append(
        "    <tr>" +
        "      <td><input type=\"checkbox\" class=\"select\"" + ((selected.includes(courses[i].id)) ? " checked" : "") +
        " data-id='" + courses[i].id + "'></td>" +
        "      <td>" + courses[i].teacher_name + "</td>" +
        "      <td>" + courses[i].name + "</td>" +
        "      <td>" + week[courses[i].weak_day] + "</td>" +
        "      <td>" + courses[i].start_time + "</td>" +
        "      <td>" + courses[i].end_time + "</td>" +
        "    </tr>"
    )
    $(".select").change(function () {
        $.get((this.checked) ? "/selections/create" : "/selections/destroy",
            "student=" + userId + "&course=" + $(this).attr("data-id") + "&" + tokenQuery,
            function (res) {});
    });
}
