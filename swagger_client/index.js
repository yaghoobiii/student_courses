if ($.cookie("user_id") && $.cookie("token"))
    signedIn();

$("#login").click(() => {
    $.get("/login", $("#login_form").serialize(), function (loginStatus) {
        if (loginStatus.token == null || loginStatus.user == null) {
            alert("Wrong username or password!");
            return;
        }

        $.cookie("user_id", loginStatus.user.id, {expires: 10});
        $.cookie("token", loginStatus.token, {expires: 10, secure: true});
        signedIn();
    });
});

function signedIn() {
    location.assign("courses.html");
}
