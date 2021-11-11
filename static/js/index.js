var loadFile = function(event) {
	var image = document.getElementById('output');
	image.src = URL.createObjectURL(event.target.files[0]);
}

$(function(){
	var $img       = $("#my_image17")
	  , $container = $("#iii");
	$img.on("click", function() {
	  $img.remove();
	  $container.removeClass().removeAttr("id");
	});
  });