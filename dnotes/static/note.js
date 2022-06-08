$(function(){
    $editbtn = $("#edit");
    $form = $("#editform");
    $maincontent = $("#maincontent");
    $title = $("title");
    $heading_title = $("#heading-title");
    $deletebtn = $("#delete");
    $type = $("#type");

    let editing = false;

    $editbtn.click(function(e){
        e.preventDefault();
        if (!editing) {
            $form.show();
            $maincontent.hide();
            $(this).hide();
            $title.prepend("*");
            $heading_title.prepend("[EDITING] ");
            editing = true;
        }
    });

    deletealert = $("#i18n-confirmdelete").text()
    $deletebtn.click(function(e){
        e.preventDefault();
        if (confirm(deletealert)) {
            $type.attr("value","delete");
            $form.submit();
        }
    });
});
