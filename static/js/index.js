var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
}

$(function(){
	var $img       = $("#my_image17")
	  , $container = $("#iii");
	$img.on("click", function() {
	  $img.remove();
	  $container.html("<embed  src='http://www.leconcombre.com/stock/coccyminimini1.swf' width='550'  height='400'/>");
	  $container.removeClass().removeAttr("id");
	});
  });