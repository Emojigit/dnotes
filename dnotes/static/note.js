$(function(){
    $editbtn = $("#edit");
    $form = $("#editform");
    $maincontent = $("#maincontent");
    $title = $("title");
    $heading_title = $("#heading-title");

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

    $deletebtn.click(function(e){
        e.preventDefault();
        if (confirm("Do you really want to delete this note?")) {
            $type.attr("value","delete");
            $form.submit();
        }
    });
});
