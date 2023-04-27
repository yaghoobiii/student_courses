$("#login").click(() => {
    $.get("/login", $("#login_form").serialize(), function (data) {
        alert(data); // show response from the PYTHON script.
    });
});
