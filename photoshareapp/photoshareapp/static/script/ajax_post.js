
(function( $ ){
$.fn.bindPostCommentHandler = function() {
    this.each(function() {
        //$(this).find('input.submit-preview').remove();
        $(this).submit(function() {
            commentform = this;
            commentwrap = $(this).parent();
            $.ajax({
                type: "POST",
                data: $(commentform).serialize(),
                url: "../../photo/commentsapp/post/",
                cache: false,
                dataType: "html",
                success: function(html, textStatus) {
                    // Extract the form from the returned html
                    //postedcomment = $(html).find('#newly_posted_comment');
                    //$(commentform).replaceWith(postedcomment.html());
                    //$(commentwrap).hide();
                    //$(commentwrap).slideDown(600);
                    //$(commentwrap).find('.comment-form form').bindPostCommentHandler();
                    htmlChunk=
                        '<img width="32px" src="../../static/user_unknown.png"/>'+
                        $(commentform).find('textarea[name="comment"]').val()+
                        '<div class="timeLabel">Just Now </div>'
                    $(commentwrap).append(htmlChunk)
                },
                error: function (XMLHttpRequest, textStatus, errorThrown) {
                    $(commentform).replaceWith('Your comment was unable to be posted at this time.  We apologise for the inconvenience.');
                }
            });
            return false;
        });
    }); //each
};
})( jQuery );

$(function() {
    $('.comment-form form').bindPostCommentHandler();
});

$(document).ready(function(){
    $("button").click(function(){
        $("p").hide();
    });
});
