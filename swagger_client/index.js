$("#login").click(() => {
    $.get("/login", $("#login_form").serialize(), function (data) {
        alert(JSON.stringify(data));
    });
});
