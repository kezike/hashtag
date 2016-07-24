/**
 * jTinder initialization
 */
 // here is where we will handle what happens to those liked and rejected
 // liked want to match themso need to update the match table
 // rejected keep going
$("#tinderslide").jTinder({
	// dislike callback
	// $(function() {
 //    	$('button').click(function() {
 //        	var user = $('#txtUsername').val();
 //        	var pass = $('#txtPassword').val();
 //        	$.ajax({
 //            	url: '/signUpUser',
 //            	data: $('form').serialize(),
 //            	type: 'POST',
 //            	success: function(response) {
 //                	console.log(response);
 //            	},
 //            	error: function(error) {
 //                	console.log(error);
 //            	}
 //        	});
 //    	});
	// });


    onDislike: function (item) {
	    // set the status text this will change
        $('#status').html('Dislike image ' + (item.index()+1));
        //var ul = document.getElementById("foo");
		// var items = ul.getElementsByTagName("li");
		// for (var i = 0; i < items.length; ++i) {
		//   // do something with items[i], which is a <li> element
    },
	// like callback
    onLike: function (item) {
	    // set the status text
        $('#status').html('Like image ' + (item.index()+1));
    },
	animationRevertSpeed: 200,
	animationSpeed: 400,
	threshold: 1,
	likeSelector: '.like',
	dislikeSelector: '.dislike'
});

$(function() {
    $('button').click(function() {
        var user = $('#txtUsername').val();
        var pass = $('#txtPassword').val();
        $.ajax({
            url: '/chat',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

/**
 * Set button action to trigger jTinder like & dislike.
 */
$('.actions .like, .actions .dislike').click(function(e){
	e.preventDefault();
	$("#tinderslide").jTinder($(this).attr('class'));
});