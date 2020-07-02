<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>jQuery Bind Click Event to Dynamically added Elements</title>
<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
<script>
  	var id = 1;
    $(document).ready(function(){
        $("button").click(function(){
            $("ol").append("<li value='" + id +"'>list item <a href='javascript:void(0);' class='remove' >&times; " + id + " </a></li>");
          id = id +1;
        });
        $(document).on("click", "a.remove" , function() {
          	alert($(this).parent().val())
            $(this).parent().remove();
        });
    });
</script>
</head>
<body>
    <button>Add new list item</button>
    <p>Click the above button to dynamically add new list items. You can remove it later.</p>
    <ol>
        <li>list item</li>
        <li>list item</li>
        <li>list item</li>
    </ol>
</body> 
</html>